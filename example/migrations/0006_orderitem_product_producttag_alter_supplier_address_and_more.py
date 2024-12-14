# Generated by Django 4.2.5 on 2023-11-21 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0005_toy_supplier'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('discount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'Заказанный продукт',
                'verbose_name_plural': 'Заказанные продукты',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('creator_name', models.CharField(max_length=100, null=True)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/%Y/%m/%d')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('exist', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фотографии',
                'ordering': ['name', '-price', 'creator_name'],
            },
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='example.product')),
            ],
            options={
                'verbose_name': 'Тег продукта',
                'verbose_name_plural': 'Теги продуктов',
            },
        ),
        migrations.AlterField(
            model_name='supplier',
            name='address',
            field=models.CharField(verbose_name='Адресс'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='name',
            field=models.CharField(verbose_name='Название поставщика'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='telephone',
            field=models.CharField(verbose_name='Телефон'),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('products', models.ManyToManyField(through='example.ProductTag', to='example.product')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.AddField(
            model_name='producttag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='example.tag'),
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('delivery_address', models.TextField()),
                ('client_phone', models.CharField(max_length=20)),
                ('client_name', models.CharField(max_length=100)),
                ('products', models.ManyToManyField(through='example.OrderItem', to='example.product')),
            ],
            options={
                'verbose_name': 'Заказ фотографии',
                'verbose_name_plural': 'Заказы фотографий',
            },
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='example.orderproduct'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='example.product'),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('products', models.ManyToManyField(related_name='categories', to='example.product')),
            ],
            options={
                'verbose_name': 'Катерогия',
                'verbose_name_plural': 'Категории',
            },
        ),
    ]
