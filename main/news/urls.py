from django.urls import path
from .views import *

# Ссылки внути /news/
# path 'way' , (func -функция из .views)
# ip/news/way
urlpatterns = [
    path('', index),
    path('test/', test),
]
