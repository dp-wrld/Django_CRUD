from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('add_user',views.add_user,name="add_user"),
    path('edit_user/<int:uid>',views.edit_user,name="edit_user"),
    path('delete_user/<int:uid>',views.delete_user,name="delete_user")
]