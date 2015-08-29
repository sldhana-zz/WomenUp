from django.db import models

# Create your models here.

# Supporter

class Supporter(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Address1 = models.CharField(max_length=50)
    Address2 = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    ZIP = models.CharField(max_length=50)
    Phone = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)


# Agency
class Agency(models.Model):
    Name = models.CharField(max_length=50)
    ContactName = models.CharField(max_length=50)
    TINNumber = models.CharField(max_length=50)
    Address1 = models.CharField(max_length=50)
    Address2 = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    ZIP = models.CharField(max_length=50)
    Phone = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)



class Service(models.Model):
    ServiceName=models.CharField(max_length=50)


class SupporterService(models.Model):
    Supporter= models.ForeignKey(Supporter)
    Service=models.ForeignKey(Service)

class AgencySupporterApproval(models.Model):
    Agency=models.ForeignKey(Agency)
    Supporter=models.ForeignKey(Supporter)
