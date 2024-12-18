# Generated by Django 5.1.3 on 2024-11-24 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_customuser_email_alter_customuser_field_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='field',
            field=models.CharField(choices=[('fashion', 'Fashion'), ('food', 'Food'), ('health', 'Health'), ('other', 'Other')], max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='nickname',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='position',
            field=models.CharField(choices=[('influencer', 'Influencer'), ('advertiser', 'Advertiser')], max_length=50),
        ),
    ]
