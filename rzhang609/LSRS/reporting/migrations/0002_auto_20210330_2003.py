# Generated by Django 3.1.7 on 2021-03-31 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='holiday',
            name='Id',
        ),
        migrations.AlterField(
            model_name='holiday',
            name='Name',
            field=models.CharField(db_column='Name', max_length=50, primary_key=True, serialize=False),
        ),
    ]