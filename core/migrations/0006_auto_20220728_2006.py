# Generated by Django 2.2.15 on 2022-07-29 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20220728_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telefono',
            field=models.SmallIntegerField(null=True),
        ),
    ]
