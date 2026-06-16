from django.db import models

# Create your models here.

class Employee(models.Model):
    DEPARTMENT = [
        ('hr', 'human resource'),
        ('acc', 'accounting'),
        ('mgt', 'management'),
        ('it', 'information & technology'),
    ]
    name = models.CharField(max_length=255, null=True)
    picture = models.ImageField(upload_to='media/employee', null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=15, null=True)
    city = models.CharField(max_length=255, null=True)
    department = models.CharField(max_length=50, choices=DEPARTMENT, null=True)
    salary = models.PositiveIntegerField(default=1, null=True)

    def __str__(self):
        return f"{self.name}---{self.email}---{self.department}"

class Product(models.Model):
    CATEGORY = [
        ('clothing', 'clothing'),
        ('electronics', 'electronics'),
        ('sports', 'sports'),
    ]
    product_name = models.CharField(max_length=255, null=True)
    category = models.CharField(max_length=100, choices=CATEGORY, null=True)
    price = models.FloatField(null=True)
    quantity = models.PositiveIntegerField(default=1, null=True)
    total = models.FloatField(null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return f"{self.product_name}---{self.price}"

class Student(models.Model):
    YEAR = [
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd'),
        ('4th', '4th')
    ]
    SEMESTER = [
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd')
    ]
    student_name = models.CharField(max_length=255, null=True)
    roll_number = models.CharField(max_length=8, null=True)
    email = models.EmailField(null=True)
    course = models.CharField(max_length=255, null=True)
    year = models.CharField(max_length=5, choices=YEAR, null=True)
    semester = models.CharField(max_length=5, choices=SEMESTER, null=True)

    def __str__(self):
        return f"{self.student_name}---{self.course}"
