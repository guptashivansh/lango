# Generated by Django 2.0.4 on 2018-04-15 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translators', '0003_auto_20180415_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='translatorprofile',
            name='Languages_Known',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
