# Generated by Django 4.1.7 on 2023-04-03 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_menu_alter_menuitem_options_remove_menuitem_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
