# Generated by Django 2.0.3 on 2018-03-28 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180317_1421'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='major',
            options={'ordering': ['name']},
        ),
    ]
