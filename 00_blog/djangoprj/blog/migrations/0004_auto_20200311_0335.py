# Generated by Django 3.0.4 on 2020-03-11 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='public',
            new_name='publish',
        ),
    ]