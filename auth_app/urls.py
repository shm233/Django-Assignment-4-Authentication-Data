from django.urls import path
from auth_app.views import *

urlpatterns = [
    path('', sign_up, name="sign_up"),
    path('sign-in/', sign_in, name="sign_in"),
    path('sign-out/', sign_out, name="sign_out"),
    path('home-page/', home_page, name="home_page"),
]
