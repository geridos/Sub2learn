from django.urls import path

from . import views
from . import views_frontdoor
from . import views_aboutme
from . import views_blog
from . import views_app

urlpatterns = [
    path('', views_frontdoor.index, name='index'),
    path('aboutme/<str:aboutme_page>', views_aboutme.index, name='aboutme_index'),
    path('blog/<str:blog_page>', views_blog.index, name='blog_index'),
    path('app/profiles', views_app.index, name='app_index'),
    path('app/new_profile', views_app.add_new_profile, name='app_add_new_profile'),
    path('app/<str:profile_name>/stat', views_app.profile_stat, name='profile_stat'),
    path('app/<str:profile_name>/words/burntoil', views_app.burntOil, name='burntOil'),
    path('app/<str:profile_name>/words/midnightoil', views_app.midnightOil, name='midnightOil'),
    path('app/<str:profile_name>/new_input/', views_app.new_input, name='new_input'),
]
