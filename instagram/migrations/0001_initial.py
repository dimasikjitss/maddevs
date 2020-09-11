# Generated by Django 3.1.1 on 2020-09-11 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstagramUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, verbose_name='Username')),
            ],
        ),
        migrations.CreateModel(
            name='PostInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField()),
                ('comment_count', models.BigIntegerField()),
                ('like_count', models.BigIntegerField()),
                ('description', models.TextField()),
                ('instagram_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='instagram.instagramuser')),
            ],
        ),
    ]