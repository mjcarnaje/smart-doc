# Generated by Django 5.1.2 on 2024-12-02 15:30

import pgvector.django
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_documentchunk_embedding_vector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentchunk',
            name='embedding_vector',
            field=pgvector.django.VectorField(blank=True, dimensions=768, editable=False, null=True),
        ),
    ]
