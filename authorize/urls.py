from django.urls import path
from authorize.views import index, sign_up, sign_in

urlpatterns = [
    path('', index, name='index'),
    path('sign_up/', sign_up, name='sign_up'),
    path('sign_in/', sign_in, name='sign_in')

]