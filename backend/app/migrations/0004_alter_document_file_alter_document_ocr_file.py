# Generated by Django 5.1.2 on 2024-12-01 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_documentchunk_embedding_vector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='ocr_file',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
