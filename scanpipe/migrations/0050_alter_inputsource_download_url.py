from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("scanpipe", "0077_merge_20251111_0923"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inputsource",
            name="download_url",
            field=models.TextField(
                blank=True,
                help_text="Download URL of the input file.",
            ),
        ),
    ]

