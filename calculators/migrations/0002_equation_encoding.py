# Generated by Django 4.0.5 on 2022-06-07 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculators', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equation',
            name='encoding',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
