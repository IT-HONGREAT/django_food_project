# Generated by Django 3.2.9 on 2021-11-27 16:25

import django.core.validators
from django.db import migrations, models
import posts.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('food_img', models.ImageField(upload_to='food_img/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('feeling', models.CharField(default='', max_length=80)),
                ('score', models.IntegerField(default=0)),
                ('content', models.TextField(validators=[django.core.validators.MinLengthValidator(3, '음식의 설명이나 기분을 3글자 이상 적어주세요!'), posts.validators.validate_numbers])),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
