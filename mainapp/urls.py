from . import views
from django.urls import path

app_name = 'mainapp'
urlpatterns = [
    path('gift-list', views.index, name='index'),
    path('recipients', views.distinct_recipients, name='recipients'),
    path('gift-details/<int:id>', views.details, name='details'),
    path('add-new-gift', views.create_item, name='create_item'),
    path('update-gift/<int:id>', views.update_item, name='update_item'),
    path('delete-gift/<int:id>', views.delete_item, name='delete_item'),
    path('page-does-not-exist', views.page_does_not_exist, name='no_page'),
]
