# Generated by Django 4.1.2 on 2022-10-19 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0006_remove_attendance_zang_attendanceclass_zang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendanceclass',
            name='zang',
            field=models.CharField(choices=[('1', '1'), ('2', '2')], default=1, max_length=1),
        ),
    ]