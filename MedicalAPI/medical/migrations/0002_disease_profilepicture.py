# Generated by Django 2.2.1 on 2019-06-20 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='profilePicture',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]