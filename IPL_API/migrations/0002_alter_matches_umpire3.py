# Generated by Django 4.2.1 on 2023-06-03 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IPL_API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matches',
            name='umpire3',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
