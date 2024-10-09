from django.db import models

# Create your models here.

class School(models.Model):
    # we extend it to models and Model class
    school_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100,choices=
                            (('Government','Government'),
                             ('private','private'),
                            ('International','International')))
    added_date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + "-" + self.location


#student model
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=100,choices=
                            (('Self Learner','sl'),
                             ('Leader','ld'),
                            ('Sincere','sc')))
    school = models.ForeignKey(School,on_delete=models.CASCADE)