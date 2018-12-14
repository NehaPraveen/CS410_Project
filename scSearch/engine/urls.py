from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gene_card/<str:gene>/<int:weight>/', views.gene_card_ajax, name='gene_card'),
    path('search/<str:json_query_str>/', views.search_results_ajax, name='search')
]

