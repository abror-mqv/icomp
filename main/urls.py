from django.urls import path
from .views import index, DView, catalog, aboutus
urlpatterns = [
    path('', index, name='homepage'),
    path('<int:pk>', DView.as_view(), name='dlaptop'),
    path('catalog', catalog, name='catalog'),
    path('about-us', aboutus, name='about-us')
    
]
