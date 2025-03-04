from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register, name='register'),
    path('person/<int:pk>', views.individual_record, name='person'),
    path('delete/<int:pk>', views.delete_record, name='delete'),
    path('add-person', views.add_person, name='add_person'),
    path('update/<int:pk>', views.update, name='update'),
]