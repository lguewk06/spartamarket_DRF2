from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='list'),
    path('create/', views.ProductCreateView.as_view(), name='create'),
    path('<int:pk>/', views.ProductUpdateView.as_view(), name='update'),
    path('<int:pk>/', views.ProductDeleteView.as_view(), name='delete'),
]
