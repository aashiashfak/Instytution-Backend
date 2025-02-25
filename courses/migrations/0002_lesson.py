# Generated by Django 5.1.1 on 2024-09-11 06:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('chapter', models.ManyToManyField(related_name='lessons', to='courses.lessonpdf')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_lessons', to=settings.AUTH_USER_MODEL)),
                ('image', models.ManyToManyField(related_name='lessons', to='courses.lessonimage')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updated_lessons', to=settings.AUTH_USER_MODEL)),
                ('video', models.ManyToManyField(related_name='lessons', to='courses.lessonvideo')),
            ],
        ),
    ]
