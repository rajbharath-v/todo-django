from django.urls import path
from . import views
urlpatterns=[
    path('addtask/',views.addtask,name='addtask'),
    path('mark_As_Done/<int:pk>/',views.mark_as_done,name='mark_as_done'),
    path('delete_task/<int:pk>/',views.delete_task,name='delete_task'),
    path('undone_task/<int:pk>/',views.undone_task,name='undone_task'),
    path('edit_task/<int:pk>/',views.edit_task,name='edit_task'),
]