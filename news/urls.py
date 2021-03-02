from django.urls import path
from news.views import index, image_upload_view


urlpatterns = [
    path('', index, name='index'),
    path('recipes/', index, name='recipes'),
    path('add/', image_upload_view, name='add'),

]