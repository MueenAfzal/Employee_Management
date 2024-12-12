
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [    
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('all', views.all, name='all'),
    path('add', views.add, name='add'),
    path('remove', views.remove, name='remove'),
    path('remove/<int:emp_id>', views.remove, name='remove'),
    path('filter', views.filter, name='filter'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
