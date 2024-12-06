# Generated by Django 5.1.2 on 2024-12-02 03:58

import pgvector.django
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_documentchunk_vector_index'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='processing_task_id',
        ),
        migrations.AddField(
            model_name='document',
            name='no_of_chunks',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='documentchunk',
            name='embedding_vector',
            field=pgvector.django.VectorField(blank=True, dimensions=4096, editable=False, null=True),
        ),
    ]
