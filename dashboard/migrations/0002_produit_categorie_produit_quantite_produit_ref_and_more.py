# Generated by Django 5.1.7 on 2025-03-28 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='categorie',
            field=models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme'), ('Enfant', 'Enfant')], default='Homme', max_length=10),
        ),
        migrations.AddField(
            model_name='produit',
            name='quantite',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='produit',
            name='ref',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produit',
            name='taille',
            field=models.CharField(default=2, max_length=10),
            preserve_default=False,
        ),
    ]
