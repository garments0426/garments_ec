# Generated by Django 3.1.3 on 2020-11-09 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goods',
            old_name='is_home',
            new_name='is_hot',
        ),
    ]