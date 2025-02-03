from django.urls import path
from . import views


app_name = 'shop'
urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.category_list, name='category_list'),
    path('search/', views.search_products, name='search_products'),
    path('about/', views.about, name='about'),
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('products/<int:pk>/', views.product_detail_view,
         name='product-detail-view'),
]
