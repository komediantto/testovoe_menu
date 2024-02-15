# Generated by Django 4.1.7 on 2023-04-03 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_remove_menuitem_menu_menuitem_menu_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название меню')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
            },
        ),
        migrations.AlterModelOptions(
            name='menuitem',
            options={'verbose_name': 'Элемент меню', 'verbose_name_plural': 'Элементы меню'},
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='title',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='name',
            field=models.CharField(default=1, max_length=100, verbose_name='Название'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='menu.menuitem', verbose_name='Родитель'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='url',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='menu_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menu', verbose_name='Название меню'),
        ),
    ]