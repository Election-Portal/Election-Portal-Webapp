# Generated by Django 2.0.7 on 2018-07-12 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('political_divisions', '0002_district'),
        ('electoral_constituencies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sabha',
            name='district',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='SabhaDistrictSet', to='political_divisions.District'),
            preserve_default=False,
        ),
    ]