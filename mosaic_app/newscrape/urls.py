from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='news_index'),
    # path('edit/<int:num>', views.edit, name='edit'),
    # path('delete/<int:num>', views.delete, name='delete'),
    # path('history', views.history, name='history')
]