# Generated by Django 4.2.8 on 2024-03-26 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0006_alter_subscription_options_alter_lesson_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='логотип'),
        ),
    ]
