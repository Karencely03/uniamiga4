# Generated by Django 3.1.7 on 2021-04-03 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UniamigaApp', '0005_auto_20210403_1151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutor',
            name='telefono',
        ),
    ]
