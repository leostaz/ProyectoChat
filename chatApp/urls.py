from django.urls import path

from . import views


urlpatterns = [

    path('', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_request, name="login"),
    path('logout/', views.RequestLogoutView.as_view(), name='logout'),
    path('editar-perfil/', views.ProfileUpdateView.as_view(), name="editar_perfil"),
    path('agregar-avatar/', views.agregar_avatar, name="agregar_avatar"),

]
