from django.shortcuts import render, redirect
from data_app.models import *

# Create your views here.
# CRUD Operation

def employee_list(request):
    employee = Employee.objects.all()
    context = {
        'emp' : employee
    }
    return render(request, 'employee/employee-list.html', context)

def employee_view(request, emp_id):
    employee = Employee.objects.get(id = emp_id)
    context = {
        'emp': employee
    }
    return render(request, 'employee/employee-profile.html', context)

def add_employee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        picture = request.FILES.get('picture')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        department = request.POST.get('department')
        salary = request.POST.get('salary')

        Employee.objects.create(
            name = name,
            picture = picture,
            email = email,
            phone = phone,
            city = city,
            department = department,
            salary = salary
        )
        return redirect('employee_list')
    return render(request, 'employee/add-employee.html')

def edit_employee(request, emp_id):
    employee = Employee.objects.get(id = emp_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        picture = request.FILES.get('picture')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        department = request.POST.get('department')
        salary = request.POST.get('salary')

        employee.name = name
        if picture:
            employee.picture = picture
        employee.email = email
        employee.phone = phone
        employee.city = city
        employee.department = department
        employee.salary = salary
        employee.save()
    context = {
        'emp' : employee
    }
    return render(request, 'employee/edit-employee.html', context)

def delete_employe(request, emp_id):
    Employee.objects.get(id = emp_id).delete()
    return redirect('employee_list')

def product_list(request):
    product = Product.objects.all()
    context = {
        'pro' : product
    }
    return render(request, 'product/product-list.html', context)

def add_product(request):
    if request.method == 'POST':
        product_name = request.POST.get('name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        description = request.POST.get('description')

        Product.objects.create(
            product_name = product_name,
            category = category,
            price = price,
            quantity = quantity,
            total = float(price) * int(quantity),
            description = description
        )
        return redirect('product_list')
    return render(request, 'product/add-product.html')

def edit_product(request, pro_id):
    product = Product.objects.get(id = pro_id)
    if request.method == 'POST':
        product_name = request.POST.get('name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        description = request.POST.get('description')

        product.product_name = product_name
        product.category = category
        product.price = price
        product.quantity = quantity
        product.total = float(price) * int(quantity)
        product.description = description
        product.save()

    context = {
        'product' : product
    }
    return render(request, 'product/edit-product.html', context)

def delete_product(request, pro_id):
    Product.objects.get(id = pro_id).delete()
    return redirect('product_list')

def student_list(request):
    student = Student.objects.all()
    context = {
        'student' : student
    }
    return render(request, 'student/student-list.html', context)

def add_student(request):
    if request.method == 'POST':
        student_name = request.POST.get('name')
        roll_number = request.POST.get('roll_number')
        email = request.POST.get('email')
        course = request.POST.get('course')
        year = request.POST.get('year')
        semester = request.POST.get('semester')

        Student.objects.create(
            student_name = student_name,
            roll_number = roll_number,
            email = email,
            course = course,
            year = year,
            semester = semester
        )
        return redirect('student_list')
    return render(request, 'student/add-student.html')

def edit_student(request, stu_id):
    student = Student.objects.get(id = stu_id)
    if request.method == 'POST':
        student_name = request.POST.get('name')
        roll_number = request.POST.get('roll_number')
        email = request.POST.get('email')
        course = request.POST.get('course')
        year = request.POST.get('year')
        semester = request.POST.get('semester')

        student.student_name = student_name
        student.roll_number = roll_number
        student.email = email
        student.course = course
        student.year = year
        student.semester = semester
        return redirect('student_list')
    context = {
        'student' : student
    }
    return render(request, 'student/edit-student.html', context)

def delete_student(request, stu_id):
    Student.objects.get(id = stu_id).delete()
    return redirect('student_list')
