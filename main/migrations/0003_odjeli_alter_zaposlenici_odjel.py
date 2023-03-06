# Generated by Django 4.1.7 on 2023-03-02 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_zaposlenici_vrsta_ugovora'),
    ]

    operations = [
        migrations.CreateModel(
            name='Odjeli',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('odjeli_org', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='zaposlenici',
            name='odjel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.odjeli'),
        ),
    ]
