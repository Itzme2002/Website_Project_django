from django.urls import path
from .import views
urlpatterns=[
    path('home/',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('about/',views.about,name='about'),
    path('help/',views.help,name='help'),
    path('contact/',views.contact,name='contact'),
    path('form/',views.form,name='form'),
    path('registration/',views.registration,name='registration'),
    path('login_user/',views.login_user,name='login_user'),
    path('dash_board/',views.dash_board,name='dash_board'),
    path('logout/',views.logout,name='logout')
]