# Generated by Django 5.1.1 on 2024-09-10 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='register_mode',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('user', 'User'), ('instructor', 'Instructor'), ('course_admin', 'Course Admin'), ('shop_admin', 'Shop Admin')], default='user', max_length=20),
        ),
    ]
