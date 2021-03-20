from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='meet_index'),
    path('create', views.create, name='meet_create'),
    path('edit', views.edit, name='meet_edit'),
    path('delete', views.delete, name='meet_delete'),
    path('search', views.search, name='meet_search'),
    path('login', views.login_meet, name='meet_login'),
    path('logout', views.logout_meet, name='meet_logout')
]