# Generated by Django 2.2.6 on 2019-10-16 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=8)),
                ('avatar', models.ImageField(upload_to='')),
                ('about', models.CharField(max_length=1000)),
                ('slogan', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('category', models.CharField(choices=[('GD', 'Graphics & Design'), ('DM', 'Digital & Marketing'), ('VA', 'Video & Animation'), ('MA', 'Music & Audio'), ('PT', 'Programming & Tech')], max_length=2)),
                ('description', models.CharField(max_length=1000)),
                ('price', models.IntegerField(default=5)),
                ('photo', models.ImageField(upload_to='')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
