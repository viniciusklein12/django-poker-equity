# Generated by Django 3.0.4 on 2020-03-10 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Hand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=1)),
                ('suit', models.CharField(choices=[('D', 'Diamonds'), ('S', 'Spades'), ('H', 'Hearts'), ('C', 'Clubs')], default='D', max_length=1)),
                ('flop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equity.Flop')),
                ('hand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equity.Hand')),
            ],
        ),
    ]
