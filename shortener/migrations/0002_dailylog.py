# Generated by Django 3.0.6 on 2020-05-31 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_date', models.DateField()),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shortener.Site')),
            ],
        ),
    ]
