from django.urls import path
from .views import about, student_add, student_delete, student_detail, student_list, student_update

urlpatterns = [
    # path('', home, name='home'),
    path('',student_add , name='add'),
    path('list/',student_list , name='list'),
    path('update/<int:id>',student_update , name='update'),
    path('delete/<int:id>',student_delete , name='delete'),
    path('student/<int:id>', student_detail, name="detail"),
    path('about/', about, name="about"),
]