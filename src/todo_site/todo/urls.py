from django.urls import path
from .views import ItemListView
from . import views

urlpatterns = [
    path('', ItemListView.as_view(), name='todo-home'),
    path('save_item', views.save_item),
    path('delete_item/<int:item_id>', views.delete_item),
]