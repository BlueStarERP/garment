from django.db import models

# Create your models here.
class department(models.Model):
    department_name = models.CharField(max_length=100)
    def __str__(self):
        return self.department_name


class region(models.Model):
    region_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.region_name

class township(models.Model):
    region = models.ForeignKey(region, on_delete=models.CASCADE)
    township = models.CharField(max_length=100)
    
    def __str__(self):
        return self.township



class employee_profile(models.Model):
    employee_id = models.CharField(max_length=225, unique=True)
    employee_name = models.CharField(max_length=225, blank=True, null=True)
    ssb_id = models.CharField(max_length=225, blank=True, null=True)
    nrc_no = models.CharField(max_length=225, unique=True)
    fathername = models.CharField(max_length=225)
    mothername = models.CharField(max_length=225)
    gender = models.CharField(max_length=100)
    dob = models.DateField()
    entrydate = models.DateField()
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    phone = models.CharField(max_length=225, blank=True, null=True)
    address = models.TextField() 
    township = models.ForeignKey(township, on_delete=models.CASCADE, blank=True, null=True)
    employee_status = models.IntegerField(default=1)
    photo = models.ImageField(upload_to='', blank=True, null=True)
    familytable = models.ImageField(upload_to='', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.employee_name
