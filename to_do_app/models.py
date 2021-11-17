from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)    
    created_date = models.DateTimeField(auto_now_add=True) # oluşturulduğu tarih
    
    class Meta:
        ordering = ('-created_date',) # tersten sırala
    
    def __str__(self):
        return self.title
    
    