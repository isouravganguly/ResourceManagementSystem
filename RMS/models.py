from django.db import models
from django.db.models.fields import CharField, NullBooleanField, PositiveIntegerField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class products(models.Model):
    Name= models.CharField(max_length=20)
    Category= models.CharField(max_length=20)
    addedOn= models.DateField()
    Quantity= models.PositiveIntegerField()
    Company= models.CharField(max_length=20)

    def __str__(self):
        return self.Name

class department(models.Model):
    Name= CharField(max_length=30)
    empcount= models.PositiveIntegerField()
    lastIssue= models.DateField(null=True)
    lastproduct= models.ForeignKey(products, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.Name

class employees(models.Model):
    Name= models.CharField(max_length=40)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null= True)
    Department= models.ForeignKey(department, on_delete=models.SET_NULL, null=True)
    EmpID= models.PositiveBigIntegerField()
    pic=models.ImageField(blank=True, upload_to='profile_image')

    def __str__(self):
        return (self.Name).replace(" ", "")
        

#@receiver(post_save, sender=employees)
def create_user_profile(sender,instance, *args, **kwargs):
        if kwargs['created']:
            s= (instance.Name+str(instance.EmpID)).replace(" ", "")
            usern=User.objects.create(username=s, password="dummypass")
            usern.set_password('dummypass')
            
            instance.user=usern
            usern.save()

class transactions(models.Model):
    officeID= models.ForeignKey(employees, on_delete=models.CASCADE)
    issueDate= models.DateTimeField()
    proID= models.ForeignKey(products, on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField()

post_save.connect(create_user_profile, sender=employees)