# Generated by Django 3.2.7 on 2021-12-31 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0007_alter_item_theme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='theme',
        ),
        migrations.AddField(
            model_name='theme',
            name='itens',
            field=models.ManyToManyField(related_name='themes', to='rent.Item'),
        ),
    ]
