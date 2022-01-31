from django.db import models
from django.urls import reverse

# Create your models here.
class couple(models.Model):
    name1 = models.CharField(max_length=100)
    name2 = models.CharField(max_length=100)

    def gaame(self):
        l1 = list(self.name1)
        l2 = list(self.name2)
        common = []
        
        for i in l1:
            if  i in l2:
                common.append(i)
        l1.extend(l2)
        for i in range(len(l1)-1, -1, -1):
            if l1[i] in common:
                l1.remove(l1[i])
        n = len(l1)%5
        if n == 0:
            st = 'ENEMIES'
            return st
        elif n == 1:
            st = 'FRIENDS'
            return st
        elif n == 2:
            st = 'LOVERS'
            return st
        elif n == 3:
            st = 'AFFECTIONATE'
            return st
        elif n == 4:
            st = 'MARRIAGE'
            return st
    
    def get_absolute_url(self):
        return reverse('result', args=[str(self.id)])