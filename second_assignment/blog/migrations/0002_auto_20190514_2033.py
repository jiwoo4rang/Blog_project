# Generated by Django 2.2.1 on 2019-05-14 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='pub_date',
            new_name='pub_data',
        ),
    ]
