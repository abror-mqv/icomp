from os import name
from django.db import models
from django.forms import ModelChoiceField
from django.db.models.deletion import PROTECT
from django.db.models.expressions import ValueRange
from django.forms.fields import ImageField

# Create your models here.

# fullname: Ноутбук игровой Acer Nitro 5 AN515-44-R5FE NH.Q9HER.001
# produccer: Acer
# ram: 1gb, 2gb, 4gb, 6gb, 8gb, 12gb, 16gb, 32gb
# ddr: 2, 3, 4
# mem_ssd: 64gb, 128gb, 256gb, 512gb, 1tb, 2tb
# mem_hdd: 128gb, 256gb, 512gb, 1tb, 2tb, 4tb
# cpu: AMD Ryzen 5 4600H 3.0 ГГц    Количество ядер	6 Кэш-память 8 МБ
# graph: GeForce GTX 1650 Ti 4GB
# os: Windows 10 Домашняя 64
# screen-resolution: 1920x1080 пикс.
# screen-capacity: 15.6"
# web-cam: 1mp
# body-material: plastic
# battary-capacity: 3733 mAh
# weight: 2.3 kg
# country: China
# garancy: 12 months

class Produccer(models.Model):
    name = models.CharField(verbose_name="Имя производителя", max_length=63)
    def __str__(self):
        return self.name

class Ram(models.Model):
    ram = models.PositiveIntegerField(verbose_name="Оперативная память")
    def __str__(self):
        return str(self.ram)

class Ddr(models.Model):
    ddr = models.PositiveSmallIntegerField(verbose_name="ddr")
    def __str__(self):
        return str(self.ddr)

class Mem_ssd(models.Model):
    mem_ssd = models.PositiveIntegerField(verbose_name="Обём ссдшника")
    def __str__(self):
        return str(self.mem_ssd)

class Mem_hdd(models.Model):
    mem_hdd = models.PositiveIntegerField(verbose_name="Обём хддшника")
    def __str__(self):
        return str(self.mem_hdd)

class Cpu(models.Model):
    name = models.CharField(verbose_name="Процессор", max_length=63)
    core = models.IntegerField(verbose_name="Кол-во ядер")
    cache = models.IntegerField(verbose_name="Кэш-память")
    def __str__(self):
        return self.name

class Graph(models.Model):
    name = models.CharField(verbose_name="Видеокарта", max_length=63)
    mem = models.IntegerField(verbose_name="Видеопамять")
    def __str__(self):
        return self.name

class OS(models.Model):
    name = models.CharField(verbose_name="Наименование ОС", max_length=127)
    x = models.PositiveIntegerField(verbose_name="Разряд ОС")
    def __str__(self):
        return self.name

class Resolution(models.Model):
    screen_resolution = models.CharField(verbose_name="Разрешение дисплея", max_length=127)
    def __str__(self):
        return self.screen_resolution

class DisplaySize(models.Model):
    display_size = models.CharField(verbose_name="Диагональ дисплея", max_length=127)
    def __str__(self):
        return self.display_size

class WebCam(models.Model):
    mp = models.CharField(verbose_name="Разрешение вебки", max_length=127)
    def __str__(self):
        return self.mp

class BodyMaterial(models.Model):
    material = models.CharField(verbose_name="Материал корпуса", max_length=127)
    def __str__(self):
        return self.material

class Country(models.Model):
    country = models.CharField(verbose_name="Страна произодства", max_length=127)
    def __str__(self):
        return self.country

class Garancy(models.Model):
    months = models.PositiveIntegerField(verbose_name="Срок гарантии в месяцах")
    def __str__(self):
        return str(self.months)



class Product(models.Model):
    image = models.ImageField(verbose_name="Изображение")
    fullname = models.CharField(verbose_name="Наименование товара", max_length=255)
    year = models.PositiveIntegerField(verbose_name="Год выпуска")
    produccer = models.ForeignKey(Produccer, verbose_name="Производитель", on_delete=models.PROTECT) 
    ram = models.ForeignKey(Ram ,verbose_name="RAM", on_delete=models.PROTECT) 
    ddr = models.ForeignKey(Ddr ,verbose_name="DDR", on_delete=models.PROTECT, null=True) 
    mem_ssd = models.ForeignKey(Mem_ssd,verbose_name="SSD", on_delete=models.PROTECT, null=True, blank=True) 
    mem_hdd = models.ForeignKey(Mem_hdd, verbose_name="HDD", on_delete=models.PROTECT, null=True, blank=True) 
    cpu = models.ForeignKey(Cpu, verbose_name="CPU", on_delete=models.PROTECT) 
    graph = models.ForeignKey(Graph, verbose_name="Видеокарта", on_delete=models.PROTECT, null=True)
    operating_system = models.ForeignKey(OS, verbose_name="OS", on_delete=models.PROTECT, null=True)
    display_resolution = models.ForeignKey(Resolution, verbose_name="Разрешение дисплея", on_delete=models.PROTECT)
    display_size = models.ForeignKey(DisplaySize, verbose_name="Диагональ дисплея", on_delete=models.PROTECT)
    web_cam = models.ForeignKey(WebCam, verbose_name="Разрешение вебки", on_delete=models.PROTECT, null=True)
    body_material = models.ForeignKey(BodyMaterial, verbose_name="Материал корпуса", on_delete=models.PROTECT, null=True)

    battery_capacity = models.PositiveIntegerField(verbose_name="Ёмкость аккумулятора")  
    weight = models.PositiveIntegerField(verbose_name="Вес девайся (гр)")

    country = models.ForeignKey(Country, verbose_name="Страна производства", on_delete=models.PROTECT, null=True)
    garancy = models.ForeignKey(Garancy, verbose_name="Срок гарантии в месяцах", on_delete=models.PROTECT)
    price = models.PositiveIntegerField(verbose_name='Цена')
    
    def __str__(self):
        return self.fullname

