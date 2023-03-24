# Generated by Django 4.1.7 on 2023-03-22 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('JHR', 'Johor'), ('KDH', 'Kedah'), ('KTN', 'Kelantan'), ('KUL', 'Kuala Lumpur'), ('LBN', 'Labuan'), ('MLK', 'Melaka'), ('NSN', 'Negeri Sembilan'), ('PHG', 'Pahang'), ('PRK', 'Perak'), ('PLS', 'Perlis'), ('SBH', 'Sabah'), ('SGR', 'Selangor'), ('TRG', 'Terengganu')], default=None, max_length=3)),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('mobilenum', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('district', models.CharField(blank=True, max_length=50, null=True)),
                ('assigned_truck', models.CharField(max_length=50, unique=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='truckdriverapi.city')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='truckdriverapi.language')),
            ],
        ),
    ]