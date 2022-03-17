# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class DocumentType(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=4)

    class Meta:
        managed = True
        db_table = 'document_type'
        
    def __str__(self):
        return self.name
        
class Offers(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.ForeignKey('Status', models.DO_NOTHING)
    creator_user = models.ForeignKey(User,on_delete = models.CASCADE, related_name='creator')
    updater_user = models.ForeignKey(User,models.DO_NOTHING, related_name='updater')
    creation_date = models.DateTimeField()
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        managed = True
        db_table = 'offer'
    
    def __str__(self):
        return self.title

class Postulation(models.Model):
    offer = models.ForeignKey(Offers, on_delete= models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField()
    
    class Meta:
        managed = True
        db_table = 'postulation'
        unique_together = (('offer','user'),)
    
class Status(models.Model):
    value = models.CharField(max_length=15)

    class Meta:
        managed = True
        db_table = 'status'
        
    def __str__(self):
        return self.value

class UserApp(models.Model):
    document_number = models.BigIntegerField(unique=True)
    second_name = models.CharField(max_length=30, blank=True, null=True)
    second_lastname = models.CharField(max_length=30, blank=True, null=True)
    profession = models.CharField(max_length=100)
    profile = models.TextField()
    document_type = models.ForeignKey(DocumentType, models.DO_NOTHING)
    user = models.OneToOneField(User, on_delete = models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'user_app'

    
    