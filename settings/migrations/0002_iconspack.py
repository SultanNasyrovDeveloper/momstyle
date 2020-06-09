# Generated by Django 2.1.3 on 2018-11-15 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IconsPack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('navbar_vk', models.FileField(upload_to='icons/', verbose_name='Вконтакте(навигация)')),
                ('navbar_instagram', models.FileField(upload_to='icons/', verbose_name='Инстаграм(навигация)')),
                ('navbar_cart', models.FileField(upload_to='icons/', verbose_name='Корзина(навигация)')),
            ],
        ),
    ]