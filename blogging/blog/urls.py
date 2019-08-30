from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:pk>', views.blog_detail, name="detail"),
    path('write', views.blog, name='blog'),
    path('<category>/', views.blog_categories, name="category"),
    path('about_us', views.about, name ="about"),
    path("contact", views.contact,name="contact"),
]
