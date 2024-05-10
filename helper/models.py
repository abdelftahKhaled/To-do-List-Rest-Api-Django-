from django.db import models



class Trickingmodel(models.Model):
        created_at=models.DateTimeField(auto_now_add=True)
        last_upate=models.DateTimeField(auto_now=True)
        
        class Meta:
            ordering=['created_at',]
            abstract=True