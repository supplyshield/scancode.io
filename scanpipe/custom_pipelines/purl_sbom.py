import logging
import os
import subprocess
import traceback
import json

from packageurl import PackageURL
from django.conf import settings

from scanpipe.pipelines import Pipeline
from scanpipe.models import DiscoveredPackage

logger = logging.getLogger("scanpipe.pipes")
NPM_CONFIG_PREFIX = "/opt/scancodeio/etc/thirdparty/node_modules"
CDXGEN_BIN = "/opt/scancodeio/etc/thirdparty/node_modules/.bin/cdxgen"
ENV = os.environ.copy()
ENV.update({
    "PATH": os.environ["PATH"],
    "HOME": os.environ["HOME"],
    # "GOPATH": os.environ["GOPATH"], FIXME: it might altually be requried
    "GOPRIVATE": settings.GO_PRIVATE,
    "CDXGEN_DEBUG_MODE": "debug",
    "NPM_CONFIG_PREFIX": NPM_CONFIG_PREFIX,
    "CDXGEN_PLUGINS_DIR": NPM_CONFIG_PREFIX + "/@cyclonedx/cdxgen-plugins-bin/plugins/",
    # "PIP_CONFIG_FILE": str(repo_dir / "pip.conf"),
    "MVN_CMD": "/root/.sdkman/candidates/maven/3.9.8/bin/mvn",
    "PREFER_MAVEN_DEPS_TREE": "false",
    "JAVA_HOME": "/root/.sdkman/candidates/java/current",
})


def subprocess_run(args, **kwargs):
    logger.info(f"[+] Executing sub_process: {args}")
    try:
        stats = subprocess.run(
            args=args,
            shell=False,
            check=True,
            capture_output=True,
            text=True,
            timeout=300,
            **kwargs,
        )
        if stats.stderr:
            logger.debug(f"[+] Got Error from subprocess: {stats.stderr}")
        logger.info(f"[+] Got Out from subprocess: {stats.stdout}")
        return stats
    except subprocess.CalledProcessError as e:
        print("Error occurred while executing the subprocess command:")
        traceback.print_exc()
        print(f"Command: {e.cmd}")
        print(f"Return Code: {e.returncode}")
        print(f"Output: {e.output}")
        print(f"Error Output: {e.stderr}")
        return e


class GenerateSbomFromPurl(Pipeline):
    """
    Generate CycloneDX Software Bill of Materials (SBOM) using cdxgen
    """

    purl = ""

    @classmethod
    def steps(cls):
        return (
            cls.clear_output,
            cls.fetch_required_purl,
            cls.run_cdxgen_scan,
            cls.move_sbom_to_input,
        )

    def clear_output(self):
        """
        Remove the output directory if it exists
        """
        logger.info("[*] Running clear_output")
        if self.project.output_path.exists():
            subprocess_run(["rm", "-rf", self.project.output_path])
        self.project.output_path.mkdir(parents=True, exist_ok=True)

    def fetch_required_purl(self):
        """
        Fetch all required purls from project input. Filename must be "dependencies.json"
        """
        logger.info("[*] Running fetch_required_purl")
        dependencies_file = self.project.input_path / "dependencies.json"

        if dependencies_file.exists():
            try:
                data = json.loads(dependencies_file.read_text())
                packages = data.get("packages", [])
                if packages:
                    self.package_url = PackageURL(**packages[0])
                    logger.info(f"Successfully loaded package: {self.package_url}")
                else:
                    logger.warning("No packages found in dependencies.json")
            except (json.JSONDecodeError, TypeError, KeyError) as e:
                logger.error(f"Error parsing dependencies.json: {e}")
        else:
            logger.warning("No dependencies file found")

    def run_cdxgen_scan(self):
        """
        Run Cdxgen to generate SBOM
        """
        logger.info("[*] Running run_cdxgen_scan")
        output_filename = "output.cdx.json"
        command = [
            CDXGEN_BIN,
            "--inspect-purl",
            self.package_url.to_string(),
            "-o",
            output_filename,
        ]
        subprocess_run(command, env=ENV, cwd=self.project.output_path)

    def move_sbom_to_input(self):
        """
        Move the generated sbom to the input directory
        """
        logger.info("[*] Running move_sbom_to_input")
        output_filename = "output.cdx.json"
        output_path = self.project.output_path / output_filename
        input_path = self.project.input_path / output_filename
        output_path.rename(input_path)
