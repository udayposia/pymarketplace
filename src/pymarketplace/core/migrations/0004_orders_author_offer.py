# Generated by Django 2.2.6 on 2019-10-17 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20191017_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='author_offer',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]