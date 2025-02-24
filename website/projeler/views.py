from django.shortcuts import render
from .models import Category, Project

#   kategori_liste=["proje1","proje2","proje3"]
#   proje_bilgi=[
#     {
#         "id":1,
#         "proje_adi": "proje1adi",
#         "acıklama": "proje1 aciklama",
#         "resim": "pp.jpg",
#         "anasayfa":True
#     },
#     {
#         "id":2,
#         "proje_adi": "proje2adi",
#         "acıklama": "proje2 aciklama",
#         "resim": "pp.jpg",
#         "anasayfa":True
#     },
#     {
#         "id":3,
#         "proje_adi": "proje3adi",
#         "acıklama": "proje3 aciklama",
#         "resim": "pp.jpg",
#         "anasayfa":False
#     }
#     ]


def home(request):
    data = {
        "kategoriler": Category.objects.all(),
        "projeler": Project.objects.all()
    }
    return render(request, "index1.html", data)

def projedetay(request, id):
    try:
        proje = Project.objects.get(id=id)  # ID'ye göre proje çekiliyor
        data = {"proje": proje}
        return render(request, "detaylar.html", data)
    except Project.DoesNotExist:
        return render(request, "404.html")  # Eğer proje bulunamazsa 404 sayfası döndürülüyor