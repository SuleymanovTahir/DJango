from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name='home'),
    path('profile/<int:id>/', views.detail_card, name='detail_card'),
    path('mail/',views.first_form,name='first_form'),
    # path('icecream/', views.icecream_list, name='icecream_list'),
]