# Generated by Django 4.1.7 on 2023-03-30 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0008_alter_addvert_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='about/')),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
            },
        ),
    ]
