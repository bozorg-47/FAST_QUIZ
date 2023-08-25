from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('members/', views.members, name='members'),
    path('members/index', views.index, name='index'),
    path('members/index/football', views.football, name='football'),
    path('members/index/general', views.general, name='general'),
    path('members/index/contact', views.contact, name='contact'),
    path('members/index/about', views.about, name='about'),
    path('members/details/<int:id>', views.details, name='details'),

]