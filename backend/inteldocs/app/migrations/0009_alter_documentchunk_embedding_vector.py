# Generated by Django 5.1.2 on 2024-12-02 04:51

import pgvector.django
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_document_processing_task_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentchunk',
            name='embedding_vector',
            field=pgvector.django.VectorField(blank=True, dimensions=3072, editable=False, null=True),
        ),
    ]
