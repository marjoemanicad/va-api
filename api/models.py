from email.policy import default
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserLogs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='logs')
    
    date_created = models.DateField(auto_now_add=True,blank=True,null=True)
    time_in = models.TimeField(auto_now_add=True)
    time_out = models.TimeField(auto_now=True)
    work_hours = models.IntegerField(default=0, blank=True,null=True)
    last_action = models.CharField(max_length=100)
    earned_credit = models.DecimalField(max_digits=8, decimal_places=5,default=0, blank=True,null=True)

    def __str__(self):
        return self.user.username+" "+str(self.date_created)

class Assistants(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client')
    verified = models.BooleanField(default=False)
    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assistants')

    def __str__(self):
        return ""+self.employer.username+" "+self.employee.username

class Credits(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='credits')
    used_leave = models.IntegerField(default=0, blank=True,null=True)
    current_leave = models.IntegerField(default=0, blank=True,null=True)
    previous_leave = models.IntegerField(default=0, blank=True,null=True)

class Leave(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leave')
    used_hour = models.IntegerField(default=0, blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)