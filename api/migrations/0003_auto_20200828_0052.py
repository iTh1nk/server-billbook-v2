# Generated by Django 3.0.5 on 2020-08-28 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200828_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statements',
            name='cycle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cycle_statements', to='api.Cycles'),
        ),
    ]
