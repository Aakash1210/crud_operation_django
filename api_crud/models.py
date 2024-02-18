# models.py
from django.db import models

class NetworkAdmin(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    class Meta:
        db_table = "NetworkAdmin"
class Router(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    physical_address = models.CharField(max_length=255)
    virtual_address = models.CharField(max_length=255)
    network_admin = models.ForeignKey(NetworkAdmin, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    class Meta:
        db_table = "Router"
