# Generated by Django 2.0 on 2020-02-17 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('amount', models.IntegerField()),
                ('rate', models.FloatField()),
                ('tag', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='instance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Instance'),
        ),
    ]
