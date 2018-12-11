from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gene_card/<str:gene>/<int:weight>/', views.gene_card_ajax, name='gene_card')
]

