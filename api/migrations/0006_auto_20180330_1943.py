# Generated by Django 2.0.3 on 2018-03-30 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20180330_1911'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['value']},
        ),
        migrations.AlterModelOptions(
            name='major',
            options={'ordering': ['value']},
        ),
        migrations.RenameField(
            model_name='course',
            old_name='name',
            new_name='value',
        ),
        migrations.RenameField(
            model_name='major',
            old_name='name',
            new_name='value',
        ),
    ]
