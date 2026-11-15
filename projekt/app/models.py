from django.db import models

class Program(models.Model):
    orszag = models.CharField(max_length=30)
    varos = models.CharField(max_length=30)
    latnivalo = models.CharField(max_length=50)
    kep = models.CharField(max_length=50)
    ar = models.CharField(max_length=20)
    idopont = models.CharField(max_length=30)
    leiras = models.TextField()
    def __str__(self):
        return self.orszag+":"+self.varos+":"+self.latnivalo

class Velemeny(models.Model):
    nev = models.CharField(max_length=30)
    szoveg = models.CharField(max_length=200)
    def __str__(self):
        return self.nev+":"+self.szoveg
