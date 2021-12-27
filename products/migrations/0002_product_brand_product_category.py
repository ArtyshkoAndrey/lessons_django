# Generated by Django 4.0 on 2021-12-27 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0001_initial'),
        ('categories', '0002_category_description_alter_category_name'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='brands.brand'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.category'),
        ),
    ]
