# Generated by Django 5.1.1 on 2024-09-25 05:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_remove_course_lesson_remove_lesson_course_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='course',
        ),
        migrations.AddField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Lesson', to='courses.course'),
        ),
    ]
