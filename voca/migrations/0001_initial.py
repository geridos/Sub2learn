# Generated by Django 2.2.16 on 2020-10-16 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=126)),
            ],
        ),
        migrations.CreateModel(
            name='MidnightOil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=52)),
                ('burnt', models.BooleanField(default=False)),
                ('learnt_date', models.DateTimeField(null=True, verbose_name='learnt_date')),
                ('added_word_date', models.DateTimeField(auto_now_add=True, verbose_name='added_date')),
                ('number_of_tries', models.IntegerField(default=0)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voca.Profile')),
            ],
        ),
    ]