from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    kategori = models.ForeignKey(Category, on_delete=models.CASCADE)  # Kategori ile ilişkilendirme
    proje_adi = models.CharField(max_length=200)
    aciklama = models.TextField()
    resim = models.CharField(max_length=100)
    anasayfa = models.BooleanField(default=False)

    def __str__(self):
        return self.proje_adi


    