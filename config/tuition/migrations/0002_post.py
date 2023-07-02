# Generated by Django 4.2.2 on 2023-07-02 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuition', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.CharField(default='title', max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('salary', models.FloatField()),
                ('details', models.TextField()),
                ('available', models.BooleanField()),
                ('catagory', models.CharField(choices=[('Student', 'Student'), ('Teacher', 'Teacher')], max_length=50)),
            ],
        ),
    ]