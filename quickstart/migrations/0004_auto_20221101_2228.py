# Generated by Django 3.1.7 on 2022-11-01 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0003_auto_20221101_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='relation',
            name='t',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='relation',
            name='blog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='brelation', to='quickstart.blog'),
        ),
        migrations.AlterField(
            model_name='relation',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='srelation', to='quickstart.student'),
        ),
    ]