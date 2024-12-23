from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Event(models.Model):
    img = models.ImageField(upload_to='pic')  # Field for event image
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=50)
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

class Registration(models.Model):
    cus_name = models.CharField(max_length=150, editable=False) 
    cus_contact = models.CharField(max_length=12)
    name = models.ForeignKey(Event, on_delete=models.CASCADE)
    dateEvent = models.DateTimeField(blank=True, null=True, editable=False)
    event_image = models.ImageField(upload_to='pic', editable=False, null=True, blank=True)  
    registered_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        request = kwargs.pop('request', None)  
        if not self.pk:  
            if request and request.user.is_authenticated:
                self.cus_name = request.user.username  

            if self.name:
                self.dateEvent = self.name.date
                self.event_image = self.name.img  

        super().save(*args, **kwargs)
