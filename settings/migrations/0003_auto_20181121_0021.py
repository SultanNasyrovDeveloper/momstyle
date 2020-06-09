# Generated by Django 2.1.3 on 2018-11-20 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_iconspack'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'ordering': ['position'], 'verbose_name': '', 'verbose_name_plural': ''},
        ),
        migrations.AddField(
            model_name='banner',
            name='image_mini',
            field=models.ImageField(default='', upload_to='banner/', verbose_name='Изображение(миниатюра), размер ~ 70 КБ'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='banner',
            name='paragraph',
            field=models.TextField(blank=True, default='', verbose_name='Параграф'),
        ),
        migrations.AddField(
            model_name='banner',
            name='position',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Позиция'),
        ),
        migrations.AddField(
            model_name='banner',
            name='tagline',
            field=models.CharField(blank=True, default='', max_length=500, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(upload_to='banner/', verbose_name='Изображение, размер ~ 300 КБ'),
        ),
    ]
