# Generated by Django 4.1.7 on 2023-04-03 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_alter_menuitem_options_remove_menuitem_active_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='label',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menu'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='url',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]