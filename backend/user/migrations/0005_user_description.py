# Generated by Django 3.1 on 2020-08-29 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200826_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]