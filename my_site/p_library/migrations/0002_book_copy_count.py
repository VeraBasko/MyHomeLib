# Generated by Django 3.0.6 on 2020-05-24 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='copy_count',
            field=models.IntegerField(default=1),
        ),
    ]