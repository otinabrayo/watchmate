# Generated by Django 5.1 on 2024-08-19 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('binge', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=30)),
                ('about', models.CharField(max_length=150)),
                ('website', models.URLField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
