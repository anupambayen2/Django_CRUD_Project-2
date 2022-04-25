from django.urls import path 
from .views import Add_Student, Edit_Student, Home, Delete_Student

urlpatterns =[

    path('',Home.as_view(), name='home'),
    path('add_student/',Add_Student.as_view(),name='add_student'),
    path('delete_student/',Delete_Student.as_view(), name='delete_student'),
    path('edit_student/<int:id>/',Edit_Student.as_view(), name='edit_student'),
    
]