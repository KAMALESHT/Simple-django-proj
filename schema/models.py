from django.db import models

class disptable(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=150)
    gender=models.CharField(max_length=1)
    class Meta :
        db_table :  "student"
