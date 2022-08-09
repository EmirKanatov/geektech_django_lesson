# Generated by Django 4.0.6 on 2022-08-09 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('rating', models.IntegerField(default=10)),
                ('text', models.TextField(blank=True, null=True)),
                ('contact', models.CharField(max_length=255, verbose_name='Номер или почта для связи')),
            ],
        ),
    ]
