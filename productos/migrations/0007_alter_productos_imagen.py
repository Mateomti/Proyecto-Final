# Generated by Django 5.0.3 on 2024-03-15 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0006_alter_productos_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]
