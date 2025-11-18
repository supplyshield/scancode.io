# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import uuid

class Accounts(models.Model):
    id = models.CharField(primary_key=True, max_length=12)
    name = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'accounts'


class ActionablePackageAvailableVersions(models.Model):
    uuid = models.CharField(primary_key=True, default=uuid.uuid4, editable=False)
    scan_status = models.CharField(max_length=20)
    package_url = models.CharField(max_length=300)
    version = models.CharField(max_length=100)
    is_latest = models.BooleanField(default=False)
    vulns_count = models.IntegerField(blank=True, null=True)
    scan_output = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    actionable = models.ForeignKey('SafeActionable', models.DO_NOTHING, blank=True, null=True)
    scancode_project_uuid = models.CharField(max_length=36, blank=True, null=True)
    is_version_in_use = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actionable_package_available_versions'
        unique_together = (('package_url', 'version'),)

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class CompanyPackages(models.Model):
    purl = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'company_packages'


class CronJobs(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512, blank=True, null=True)
    command = models.CharField(max_length=512)
    timeout = models.IntegerField(blank=True, null=True)
    interval = models.IntegerField(blank=True, null=True)
    is_weekly = models.BooleanField(blank=True, null=True)
    last_run = models.DateTimeField(blank=True, null=True)
    last_run_output = models.TextField(blank=True, null=True)
    is_active = models.BooleanField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cron_jobs'


class DeploymentCheckpoints(models.Model):
    active = models.IntegerField()
    checkpoint = models.DateTimeField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deployment_checkpoints'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ImagePackageAssociation(models.Model):
    image = models.OneToOneField('Images', models.DO_NOTHING, primary_key=True)  # The composite primary key (image_id, package_id) found, that is not supported. The first column is selected.
    package = models.ForeignKey('Packages', models.DO_NOTHING)
    metadata = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image_package_association'
        unique_together = (('image', 'package'),)


class Images(models.Model):
    name = models.CharField(max_length=100)
    backend_tech = models.CharField(max_length=24, blank=True, null=True)
    account = models.ForeignKey(Accounts, models.DO_NOTHING)
    digest = models.CharField(max_length=72)
    tag = models.CharField(max_length=128, blank=True, null=True)
    commit = models.CharField(max_length=128, blank=True, null=True)
    platform = models.CharField(max_length=24)
    parent_image = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    base_image = models.ForeignKey('self', models.DO_NOTHING, related_name='images_base_image_set', blank=True, null=True)
    repository = models.ForeignKey('Repositories', models.DO_NOTHING, blank=True, null=True)
    wasp = models.ForeignKey('Wasps', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'images'
# Unable to inspect table 'kong_unfixed'
# The error was: permission denied for table kong_unfixed


class LatestImages(models.Model):
    image = models.OneToOneField(Images, models.DO_NOTHING, primary_key=True)  # The composite primary key (image_id, account_id) found, that is not supported. The first column is selected.
    account = models.ForeignKey(Accounts, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'latest_images'
        unique_together = (('image', 'account'),)


class Layers(models.Model):
    id = models.CharField(primary_key=True, max_length=64)  # The composite primary key (id, image_id, seq) found, that is not supported. The first column is selected.
    image = models.ForeignKey(Images, models.DO_NOTHING)
    seq = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'layers'
        unique_together = (('id', 'image', 'seq'),)


class LicenseFamily(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'license_family'
# Unable to inspect table 'months'
# The error was: permission denied for table months


class PackageLicenseAssociation(models.Model):
    package = models.OneToOneField('Packages', models.DO_NOTHING, primary_key=True)  # The composite primary key (package_id, license_id) found, that is not supported. The first column is selected.
    license = models.ForeignKey(LicenseFamily, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'package_license_association'
        unique_together = (('package', 'license'),)


class Packages(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=150, blank=True, null=True)
    language = models.CharField(max_length=20, blank=True, null=True)
    purl = models.CharField(unique=True, max_length=300, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'packages'


class Repositories(models.Model):
    provider = models.CharField(max_length=200)
    org = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    is_public = models.BooleanField()
    pod = models.CharField(max_length=200, blank=True, null=True)
    subpod = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'repositories'


class RepositoryActionablePackageAvailableVersionsAssociation(models.Model):
    uuid = models.CharField(primary_key=True, default=uuid.uuid4)
    wasp_uuid = models.CharField(blank=False, null=False, max_length=200)
    repository = models.ForeignKey(Repositories, models.DO_NOTHING, blank=True, null=True)
    environment = models.CharField(max_length=255, blank=True, null=True)
    actionable_package_available_version = models.ForeignKey(
        ActionablePackageAvailableVersions, 
        models.DO_NOTHING, 
        blank=True, 
        null=True,
        db_column='actionable_package_version_id')

    class Meta:
        managed = False
        db_table = 'repository_actionable_package_versions_association'


class SafeActionable(models.Model):
    uuid = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4, editable=False)
    package_url = models.CharField(unique=True, max_length=300)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = False
        db_table = 'safe_actionable'


class SastLobMetadata(models.Model):
    module = models.CharField(max_length=1024)
    sub_module = models.CharField(max_length=1024)
    repository = models.ForeignKey(Repositories, models.DO_NOTHING, blank=True, null=True)
    bugcounts = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sast_lob_metadata'


class SastResult(models.Model):
    id = models.CharField(primary_key=True, max_length=150)
    lob = models.ForeignKey(SastLobMetadata, models.DO_NOTHING, blank=True, null=True)
    extras = models.TextField(blank=True, null=True)  # This field type is a guess.
    vulnsnippet = models.TextField(blank=True, null=True)
    githubpath = models.CharField(max_length=1024, blank=True, null=True)
    secbugurl = models.CharField(max_length=1024, blank=True, null=True)
    file_path = models.CharField(max_length=1024, blank=True, null=True)
    priority = models.CharField(max_length=20, blank=True, null=True)
    confidence = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    public_initial_point = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=200, blank=True, null=True)
    isactive = models.BooleanField(blank=True, null=True)
    wasp = models.ForeignKey('Wasps', models.DO_NOTHING, blank=True, null=True)
    fixed_date = models.DateTimeField(blank=True, null=True)
    validated = models.IntegerField(blank=True, null=True)
    validate_date = models.DateTimeField(blank=True, null=True)
    secbug_created_date = models.DateTimeField(blank=True, null=True)
    mean_solve_time = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sast_result'


class ScanpipeCodebaserelation(models.Model):
    uuid = models.UUIDField(primary_key=True)
    extra_data = models.JSONField()
    map_type = models.CharField(max_length=30)
    from_resource = models.ForeignKey('ScanpipeCodebaseresource', models.DO_NOTHING)
    project = models.ForeignKey('ScanpipeProject', models.DO_NOTHING)
    to_resource = models.ForeignKey('ScanpipeCodebaseresource', models.DO_NOTHING, related_name='scanpipecodebaserelation_to_resource_set')

    class Meta:
        managed = False
        db_table = 'scanpipe_codebaserelation'
        unique_together = (('from_resource', 'to_resource', 'map_type'),)


class ScanpipeCodebaseresource(models.Model):
    path = models.CharField(max_length=2000)
    size = models.BigIntegerField(blank=True, null=True)
    sha1 = models.CharField(max_length=40)
    md5 = models.CharField(max_length=32)
    sha256 = models.CharField(max_length=64)
    sha512 = models.CharField(max_length=128)
    copyrights = models.JSONField()
    holders = models.JSONField()
    authors = models.JSONField()
    emails = models.JSONField()
    urls = models.JSONField()
    rootfs_path = models.CharField(max_length=2000)
    status = models.CharField(max_length=50)
    type = models.CharField(max_length=10)
    extra_data = models.JSONField()
    name = models.CharField(max_length=255)
    extension = models.CharField(max_length=100)
    programming_language = models.CharField(max_length=50)
    mime_type = models.CharField(max_length=100)
    file_type = models.CharField(max_length=1024)
    project = models.ForeignKey('ScanpipeProject', models.DO_NOTHING)
    compliance_alert = models.CharField(max_length=10)
    is_archive = models.BooleanField()
    is_binary = models.BooleanField()
    is_text = models.BooleanField()
    is_key_file = models.BooleanField()
    is_media = models.BooleanField()
    tag = models.CharField(max_length=50)
    package_data = models.JSONField()
    detected_license_expression = models.TextField()
    detected_license_expression_spdx = models.TextField()
    license_detections = models.JSONField()
    license_clues = models.JSONField()
    percentage_of_license_text = models.FloatField(blank=True, null=True)
    is_legal = models.BooleanField()
    is_manifest = models.BooleanField()
    is_readme = models.BooleanField()
    is_top_level = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'scanpipe_codebaseresource'
        unique_together = (('project', 'path'),)


class ScanpipeDiscovereddependency(models.Model):
    dependency_uid = models.CharField(max_length=1024)
    extracted_requirement = models.CharField(max_length=256)
    scope = models.CharField(max_length=64)
    datasource_id = models.CharField(max_length=64)
    is_runtime = models.BooleanField()
    is_optional = models.BooleanField()
    is_resolved = models.BooleanField()
    datafile_resource = models.ForeignKey(ScanpipeCodebaseresource, models.DO_NOTHING, blank=True, null=True)
    for_package = models.ForeignKey('ScanpipeDiscoveredpackage', models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey('ScanpipeProject', models.DO_NOTHING)
    affected_by_vulnerabilities = models.JSONField()
    resolved_to_package = models.ForeignKey('ScanpipeDiscoveredpackage', models.DO_NOTHING, related_name='scanpipediscovereddependency_resolved_to_package_set', blank=True, null=True)
    is_direct = models.BooleanField()
    name = models.CharField(max_length=100)
    namespace = models.CharField(max_length=255)
    qualifiers = models.CharField(max_length=1024)
    subpath = models.CharField(max_length=200)
    type = models.CharField(max_length=16)
    version = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'scanpipe_discovereddependency'
        unique_together = (('project', 'dependency_uid'),)


class ScanpipeDiscoveredpackage(models.Model):
    type = models.CharField(max_length=16)
    namespace = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    qualifiers = models.CharField(max_length=1024)
    subpath = models.CharField(max_length=200)
    uuid = models.UUIDField(unique=True)
    filename = models.CharField(max_length=255)
    primary_language = models.CharField(max_length=50)
    description = models.TextField()
    release_date = models.DateField(blank=True, null=True)
    homepage_url = models.CharField(max_length=1024)
    download_url = models.CharField(max_length=2048)
    size = models.BigIntegerField(blank=True, null=True)
    sha1 = models.CharField(max_length=40)
    md5 = models.CharField(max_length=32)
    bug_tracking_url = models.CharField(max_length=1024)
    code_view_url = models.CharField(max_length=1024)
    vcs_url = models.CharField(max_length=1024)
    copyright = models.TextField()
    declared_license_expression = models.TextField()
    extracted_license_statement = models.TextField()
    notice_text = models.TextField()
    missing_resources = models.JSONField()
    modified_resources = models.JSONField()
    keywords = models.JSONField()
    source_packages = models.JSONField()
    project = models.ForeignKey('ScanpipeProject', models.DO_NOTHING)
    extra_data = models.JSONField()
    package_uid = models.CharField(max_length=1024)
    api_data_url = models.CharField(max_length=1024)
    file_references = models.JSONField()
    parties = models.JSONField()
    repository_download_url = models.CharField(max_length=1024)
    repository_homepage_url = models.CharField(max_length=1024)
    sha256 = models.CharField(max_length=64)
    sha512 = models.CharField(max_length=128)
    declared_license_expression_spdx = models.TextField()
    holder = models.TextField()
    license_detections = models.JSONField()
    other_license_detections = models.JSONField()
    other_license_expression = models.TextField()
    other_license_expression_spdx = models.TextField()
    affected_by_vulnerabilities = models.JSONField()
    compliance_alert = models.CharField(max_length=10)
    tag = models.CharField(max_length=50)
    datasource_ids = models.JSONField()
    datafile_paths = models.JSONField()
    is_private = models.BooleanField()
    is_virtual = models.BooleanField()
    notes = models.TextField()

    class Meta:
        managed = False
        db_table = 'scanpipe_discoveredpackage'
        unique_together = (('project', 'package_uid'),)


class ScanpipeDiscoveredpackageCodebaseResources(models.Model):
    discoveredpackage = models.ForeignKey(ScanpipeDiscoveredpackage, models.DO_NOTHING)
    codebaseresource = models.ForeignKey(ScanpipeCodebaseresource, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'scanpipe_discoveredpackage_codebase_resources'
        unique_together = (('discoveredpackage', 'codebaseresource'),)


class ScanpipeInputsource(models.Model):
    uuid = models.UUIDField(primary_key=True)
    download_url = models.CharField(max_length=4000)
    filename = models.CharField(max_length=255)
    is_uploaded = models.BooleanField()
    tag = models.CharField(max_length=50)
    project = models.ForeignKey('ScanpipeProject', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'scanpipe_inputsource'


class ScanpipeProject(models.Model):
    uuid = models.UUIDField(primary_key=True)
    created_date = models.DateTimeField()
    name = models.CharField(unique=True, max_length=100)
    work_directory = models.CharField(max_length=2048)
    extra_data = models.JSONField()
    is_archived = models.BooleanField()
    notes = models.TextField()
    settings = models.JSONField()
    slug = models.CharField(unique=True, max_length=110)
    wasp_uuid_id = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scanpipe_project'


class ScanpipeProjectmessage(models.Model):
    uuid = models.UUIDField(primary_key=True)
    severity = models.CharField(max_length=10)
    description = models.TextField()
    model = models.CharField(max_length=100)
    details = models.JSONField()
    traceback = models.TextField()
    created_date = models.DateTimeField()
    project = models.ForeignKey(ScanpipeProject, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'scanpipe_projectmessage'


class ScanpipeRun(models.Model):
    task_id = models.UUIDField(blank=True, null=True)
    task_start_date = models.DateTimeField(blank=True, null=True)
    task_end_date = models.DateTimeField(blank=True, null=True)
    task_exitcode = models.IntegerField(blank=True, null=True)
    task_output = models.TextField()
    uuid = models.UUIDField(primary_key=True)
    pipeline_name = models.CharField(max_length=256)
    created_date = models.DateTimeField()
    description = models.TextField()
    project = models.ForeignKey(ScanpipeProject, models.DO_NOTHING)
    log = models.TextField()
    scancodeio_version = models.CharField(max_length=100)
    current_step = models.CharField(max_length=256)
    selected_groups = models.JSONField(blank=True, null=True)
    selected_steps = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scanpipe_run'


class ScanpipeUuidtaggeditem(models.Model):
    object_id = models.UUIDField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    tag = models.ForeignKey('TaggitTag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'scanpipe_uuidtaggeditem'


class ScanpipeVulnerablepaths(models.Model):
    repository_id = models.IntegerField()
    path = models.JSONField()
    action_item = models.CharField(max_length=255, blank=True, null=True)
    project_name = models.CharField(max_length=255)
    has_commons_in_path = models.BooleanField()
    vulnerable_package_id = models.IntegerField(blank=True, null=True)
    environment = models.CharField(max_length=25, blank=True, null=True)
    wasp_uuid = models.UUIDField(blank=True, null=True)
    uuid = models.UUIDField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'scanpipe_vulnerablepaths'


class ScanpipeWebhookdelivery(models.Model):
    uuid = models.UUIDField(primary_key=True)
    target_url = models.CharField(max_length=1024)
    sent_date = models.DateTimeField()
    payload = models.JSONField()
    response_status_code = models.IntegerField(blank=True, null=True)
    response_text = models.TextField()
    delivery_error = models.TextField()
    project = models.ForeignKey(ScanpipeProject, models.DO_NOTHING)
    run = models.ForeignKey(ScanpipeRun, models.DO_NOTHING, blank=True, null=True)
    webhook_subscription = models.ForeignKey('ScanpipeWebhooksubscription', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scanpipe_webhookdelivery'


class ScanpipeWebhooksubscription(models.Model):
    uuid = models.UUIDField(primary_key=True)
    target_url = models.CharField(max_length=1024)
    created_date = models.DateTimeField()
    project = models.ForeignKey(ScanpipeProject, models.DO_NOTHING)
    include_results = models.BooleanField()
    include_summary = models.BooleanField()
    is_active = models.BooleanField()
    trigger_on_each_run = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'scanpipe_webhooksubscription'
# Unable to inspect table 'secbugs'
# The error was: permission denied for table secbugs


class TaggitTag(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'taggit_tag'


class TaggitTaggeditem(models.Model):
    object_id = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    tag = models.ForeignKey(TaggitTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'taggit_taggeditem'
        unique_together = (('content_type', 'object_id', 'tag'),)

class Vulnerabilities(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    description = models.CharField(max_length=500, blank=True, null=True)
    severity = models.CharField(max_length=10, blank=True, null=True)
    related = models.CharField(max_length=200, blank=True, null=True)
    nvd_cvss_base_score = models.FloatField(db_column='nvd-cvss.base_score', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nvd_cvss_exploitability_score = models.FloatField(db_column='nvd-cvss.exploitability_score', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nvd_cvss_impact_score = models.FloatField(db_column='nvd-cvss.impact_score', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'vulnerabilities'


class VulnerabilityPackageAssociation(models.Model):
    vulnerability = models.OneToOneField(Vulnerabilities, models.DO_NOTHING, primary_key=True)  # The composite primary key (vulnerability_id, package_id) found, that is not supported. The first column is selected.
    package = models.ForeignKey(Packages, models.DO_NOTHING)
    fix = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vulnerability_package_association'
        unique_together = (('vulnerability', 'package'),)


class Wasps(models.Model):
    uuid = models.CharField(unique=True, max_length=36)
    repository = models.ForeignKey(Repositories, models.DO_NOTHING, blank=True, null=True)
    tag = models.CharField(max_length=128, blank=True, null=True)
    commit = models.CharField(max_length=128, blank=True, null=True)
    environment = models.CharField(max_length=128, blank=True, null=True)
    jenkins_url = models.CharField(max_length=256, blank=True, null=True)
    raw_message = models.CharField(max_length=2048)
    ate_successfully = models.BooleanField()
    complaints = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wasps'
