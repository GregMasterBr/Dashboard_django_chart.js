from django.db import models

# Create your models here.

class Links(models.Model):
    link_redirecionado = models.URLField()
    link_encurtado = models.CharField(max_length=50,unique=True)
    created = models.DateTimeField(auto_now_add =True)
    updated = models.DateTimeField(auto_now =True)

    def __str__(self) -> str:
        return self.link_encurtado    