# Generated by Django 2.2.4 on 2019-12-08 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_answerinformation_visit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visit',
            old_name='page',
            new_name='question',
        ),
    ]
