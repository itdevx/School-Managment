# Generated by Django 4.1.2 on 2023-08-28 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Student', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('date_time_class', models.DateTimeField()),
                ('classes', models.ManyToManyField(to='Student.class')),
            ],
        ),
    ]
