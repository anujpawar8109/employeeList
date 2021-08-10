from django.db.models import fields
from .models import employees
from rest_framework import serializers
# from rest_framework import employees

class employeesSerializer(serializers.ModelSerializer):

    class Meta:
        model = employees
        fields= "__all__"











        # db_table = 'employees'
        # managed = True
        # verbose_name = 'employees'
        # verbose_name_plural = 'firstname, lastname, emp_id'
        