from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify  

User=get_user_model()

# Create your models here.

class Shop(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField(null=True, blank=True)
    address=models.TextField(null=True, blank=True)
    phone=models.CharField(max_length=20,unique=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, allow_unicode=True,null=True,blank=True) 
    active=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs): 
        if not self.slug:  
            self.slug = slugify(self.title,allow_unicode=True)  
        super(Shop,self).save(*args, **kwargs)  

    def __str__(self):  
        return self.title  

    class Meta:  
        verbose_name_plural = "Shop"
        verbose_name_plural = "Shops"