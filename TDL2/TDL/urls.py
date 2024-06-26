from django.urls import path, include

from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('change_status/<int:pk>/', views.change_status, name='change_status'),
]
