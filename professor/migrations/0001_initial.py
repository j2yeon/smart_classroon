# Generated by Django 3.2.3 on 2021-05-26 01:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('day_lecture', models.CharField(choices=[('mon', 'mon'), ('tue', 'tue'), ('wed', 'wed'), ('thu', 'thu'), ('fri', 'fri'), ('sat', 'sat'), ('sun', 'sun')], max_length=50)),
                ('period', models.IntegerField()),
                ('student', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]