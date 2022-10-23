from . import views
from django.urls import path
urlpatterns = [
    path('',views.Task_listview.as_view()),
    path('delete/<int:taskid>/', views.delete,name='delete'),
    path('update/<int:taskid>/', views.update,name='update'),
    path('detail/<int:pk>/',views.Detaail_view.as_view(),name= 'detail'),
    path('edit/<int:pk>/',views.Task_update.as_view()),
]