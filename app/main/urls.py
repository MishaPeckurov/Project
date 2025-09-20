from django.contrib import admin
from django.urls import path, include
from main import views
urlpatterns = [
    path('lakoshlak',views.ahalai),
    path('babka/',views.kaka),
    path('babki/',views.mamalai),
    path('ofigeli/<int:pyk>/<int:ylibaemca>',views.bobi),
    path('volkiofigeliofigeli/',views.kok),
    path('', views.ulaks)
]