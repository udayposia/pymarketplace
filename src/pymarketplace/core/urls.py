from django.urls import path
from .views import *

urlpatterns = [
    path('',home ,name='home'),
    path('profile/<str:username>',view_profile ,name='view_profile'),

    path('job/<int:id>',view_job ,name='view_job'),
    path('create_job',create_job ,name='create_job'),
    path('myjobs/', my_jobs, name='my_jobs'),

    path('create_order/<int:id>',create_order ,name='create_order'),

    path('jobs_request/', jobs_request, name='jobs_request'),



    path('login/',user_login ,name='user_login'),
    path('logout/',user_logout ,name='user_logout'),
    path('signup/',add_user ,name='add_user'),




]
