# Generated by Django 5.0.6 on 2024-07-09 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='vote',
            name='user',
        ),
    ]
