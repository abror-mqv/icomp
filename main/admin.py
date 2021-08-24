from django.contrib import admin
from .models import Product, Produccer, Ram, Ddr, Mem_hdd, Mem_ssd, Cpu, Graph, OS, Resolution, DisplaySize, WebCam, BodyMaterial, Country, Garancy

# Register your models here.

admin.site.register(Product)
admin.site.register(Produccer)
admin.site.register(Ram)
admin.site.register(Ddr)
admin.site.register(Mem_ssd)
admin.site.register(Mem_hdd)
admin.site.register(Cpu)
admin.site.register(Graph)
admin.site.register(OS)
admin.site.register(Resolution)
admin.site.register(DisplaySize)
admin.site.register(WebCam)
admin.site.register(BodyMaterial)
admin.site.register(Country)
admin.site.register(Garancy)
