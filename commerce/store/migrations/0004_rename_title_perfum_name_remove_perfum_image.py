# Generated by Django 5.0.2 on 2024-03-08 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_perfum_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfum',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='perfum',
            name='image',
        ),
    ]