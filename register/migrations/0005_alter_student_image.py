# Generated by Django 4.0.4 on 2022-05-22 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_alter_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(default='profil.jpg', upload_to='register/'),
        ),
    ]
