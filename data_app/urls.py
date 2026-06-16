from django.urls import path
from data_app.views import *

urlpatterns = [
    path('employee-list/', employee_list, name="employee_list"),
    path('employee-profile/<str:emp_id>/', employee_view, name="employee_view"),
    path('add-employee/', add_employee, name="add_employee"),
    path('edit-employee/<str:emp_id>', edit_employee, name="edit_employee"),
    path('delete-employe/<str:emp_id>/', delete_employe, name="delete_employe"),

    path('product-list/', product_list, name="product_list"),
    path('add-product/', add_product, name="add_product"),
    path('edit-product/<str:pro_id>/', edit_product, name="edit_product"),
    path('delete-product/<str:pro_id>/', delete_product, name="delete_product"),

    path('student-list/', student_list, name="student_list"),
    path('add-student/', add_student, name="add_student"),
    path('edit-student/<str:stu_id>', edit_student, name="edit_student"),
    path('delete_student/<str:stu_id>', delete_student, name="delete_student"),
]
