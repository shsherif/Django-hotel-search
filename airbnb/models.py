from django.db import models
from django.utils import timezone

City =(
    ('Cairo','Cairo'),
    ('Giza','Giza'),
    ('Sharm El Sheikh','Sharm El Sheikh'),
    ('Alexandria','Alexandria'),
    ('Hurghada','Hurghada'),
)

Status =(
    ('Available','Available'),
    ('Busy','Busy'),

class Appartment(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    title = models.TextField(max_length=50, unique=True)
    location = models.CharField(choices=City, default='Cairo')
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    status = mCharField(choices=City, default='Available')
    rooms= models.IntegerField()
    reserve_date = models.DateTimeField(default=timezone.now)
    release_date = models.DateTimeField()
    image=models.ImageField(upload_to='Appartment/')
    
    def __str__(self):
        return self.title
    
class Owner(models.Model):
    Owner_first_name = models.CharField(max_length=30)
    Owner_last_name = models.CharField(max_length=30)
    Owner_email = models.EmailField(default='')
    Owner_phone = models.IntegerField()
    Owner_rate = models.IntegerField()
    def __str__(self):
        return self.Owner_first_name
    
class Tenant(models.Model):
    Tenant_first_name = models.CharField(max_length=30)
    Tenant_last_name = models.CharField(max_length=30)
    Tenant_email = models.EmailField(default='')
    Tenant_phone = models.IntegerField()
    Tenant_rate = models.IntegerField()
    def __str__(self):
        return self.Tenant_first_name

