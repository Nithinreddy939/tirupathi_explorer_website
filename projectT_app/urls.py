from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', views.index, name='index'),
    path('items/', views.items, name='items'),
    path('about_website/', views.about, name='about'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('cart/', views.cart, name='cart'),

    # temples data
    path('famous_temples/',views.famous_temples,name='famous_temples'),
    path('Sri_Venkateswara_Temple/',views.temple_1,name='Sri_Venkateswara_Temple'),
    path('sri_padmavathi_temple/',views.temple_2,name='sri_padmavathi_temple'),
    path('govindharajula_temple/',views.temple_3,name='govindhrajula_temple'),
    path('Kapileswara_temple/',views.temple_4,name='kapileswara_temple'),
    path('sri_kalyana_venkateswara_temple/',views.temple_5,name='sri_kalyana_venkateswara_temple'),
]
urlpatterns += staticfiles_urlpatterns()
