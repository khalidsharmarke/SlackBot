# Generated by Django 3.2.5 on 2021-07-24 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210720_1115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='client_message_id',
            new_name='message_id',
        ),
    ]