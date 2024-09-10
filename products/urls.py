from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListCreateView.as_view(), name='product_list'),
    path('<int:pk>/', views.ProductUpdateDeleteView.as_view(), name='update'),
]
