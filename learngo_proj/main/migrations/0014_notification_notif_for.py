# Generated by Django 4.1.6 on 2023-03-03 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_notification_notif_text_notification_student_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='notif_for',
            field=models.CharField(max_length=100, null=True, verbose_name='Notification For'),
        ),
    ]
