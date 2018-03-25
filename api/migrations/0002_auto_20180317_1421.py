# Generated by Django 2.0.3 on 2018-03-17 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='course',
        ),
        migrations.AlterField(
            model_name='user',
            name='major',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Major'),
        ),
        migrations.AddField(
            model_name='user',
            name='course',
            field=models.ManyToManyField(to='api.Course'),
        ),
    ]