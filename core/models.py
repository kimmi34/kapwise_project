from django.db import models

class Geo(models.Model):
    lat = models.CharField(max_length = 100,null = True,blank = True)
    lng = models.CharField(max_length = 100,null = True,blank = True)
    id = models.PositiveIntegerField(primary_key=True)


class Address(models.Model):
    street = models.CharField(max_length = 100,null = True,blank = True)
    suite = models.CharField(max_length = 100,null = True,blank = True)
    city = models.CharField(max_length = 100,null = True,blank = True)
    zipcode = models.CharField(max_length = 100,null = True,blank = True)
    geo = models.ForeignKey(Geo,on_delete = models.CASCADE, db_index=True)
    id = models.PositiveIntegerField(primary_key=True)

    def __str__(self):
        return self.street 


class Company(models.Model):
    name = models.CharField(max_length = 100,null = True,blank = True)
    catchPhrase = models.CharField(max_length = 100,null = True,blank = True)
    bs = models.CharField(max_length = 100,null = True,blank = True)
    id = models.PositiveIntegerField(primary_key=True)

    def __str__(self):
        return self.name

class User(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length = 100,null = True,blank = True)
    username = models.CharField(max_length=100,null = True,blank = True)
    email = models.CharField( max_length =100, null = True,blank = True)
    phone = models.CharField(max_length= 100,null = True,blank = True)
    website = models.CharField(max_length = 100,null = True,blank = True)
    company = models.ForeignKey(Company,on_delete = models.CASCADE, db_index=True)
    address = models.ForeignKey(Address,on_delete = models.CASCADE, db_index=True)

    def __str__(self):
        return self.name 

