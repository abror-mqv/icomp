# Generated by Django 3.2.5 on 2021-07-27 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BodyMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=127, verbose_name='Материал корпуса')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=127, verbose_name='Страна произодства')),
            ],
        ),
        migrations.CreateModel(
            name='Cpu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63, verbose_name='Процессор')),
                ('core', models.IntegerField(verbose_name='Кол-во ядер')),
                ('cache', models.IntegerField(verbose_name='Кэш-память')),
            ],
        ),
        migrations.CreateModel(
            name='Ddr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ddr', models.PositiveSmallIntegerField(verbose_name='ddr')),
            ],
        ),
        migrations.CreateModel(
            name='DisplaySize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_size', models.CharField(max_length=127, verbose_name='Диагональ дисплея')),
            ],
        ),
        migrations.CreateModel(
            name='Garancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('months', models.PositiveIntegerField(verbose_name='Срок гарантии в месяцах')),
            ],
        ),
        migrations.CreateModel(
            name='Graph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63, verbose_name='Видеокарта')),
                ('mem', models.IntegerField(verbose_name='Видеопамять')),
            ],
        ),
        migrations.CreateModel(
            name='Mem_hdd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mem_hdd', models.PositiveIntegerField(verbose_name='Обём хддшника')),
            ],
        ),
        migrations.CreateModel(
            name='Mem_ssd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mem_ssd', models.PositiveIntegerField(verbose_name='Обём ссдшника')),
            ],
        ),
        migrations.CreateModel(
            name='OS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, verbose_name='Наименование ОС')),
                ('x', models.PositiveIntegerField(verbose_name='Разряд ОС')),
            ],
        ),
        migrations.CreateModel(
            name='Produccer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63, verbose_name='Имя производителя')),
            ],
        ),
        migrations.CreateModel(
            name='Ram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ram', models.PositiveIntegerField(verbose_name='Оперативная память')),
            ],
        ),
        migrations.CreateModel(
            name='Resolution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_resolution', models.CharField(max_length=127, verbose_name='Разрешение дисплея')),
            ],
        ),
        migrations.CreateModel(
            name='WebCam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mp', models.CharField(max_length=127, verbose_name='Разрешение вебки')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255, verbose_name='Наименование товара')),
                ('year', models.PositiveIntegerField(verbose_name='Год выпуска')),
                ('battery_capacity', models.PositiveIntegerField(verbose_name='Ёмкость аккумулятора')),
                ('weight', models.PositiveIntegerField(verbose_name='Вес девайся (гр)')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('body_material', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.bodymaterial', verbose_name='Материал корпуса')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.country', verbose_name='Страна производства')),
                ('cpu', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.cpu', verbose_name='CPU')),
                ('ddr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.ddr', verbose_name='DDR')),
                ('display_resolution', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.resolution', verbose_name='Разрешение дисплея')),
                ('display_size', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.displaysize', verbose_name='Диагональ дисплея')),
                ('garancy', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.garancy', verbose_name='Срок гарантии в месяцах')),
                ('graph', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.graph', verbose_name='Видеокарта')),
                ('mem_hdd', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.mem_hdd', verbose_name='HDD')),
                ('mem_ssd', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.mem_ssd', verbose_name='SSD')),
                ('operating_system', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.os', verbose_name='OS')),
                ('produccer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.produccer', verbose_name='Производитель')),
                ('ram', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.ram', verbose_name='RAM')),
                ('web_cam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.webcam', verbose_name='Разрешение вебки')),
            ],
        ),
    ]