from django.shortcuts import render,redirect
from .models import *
from quiz.models import *
# Create your views here.
from django.core.paginator import Paginator
from django.db.models import Q

#  index sayfası
def index(request):
    searc = Kategori.objects.filter(Q(isim__icontains='tutorial') | Q(isim__icontains='referance') & Q(tutorialActive=True)) 
    kategoriler = Kategori.objects.all()
    navbarKategori = Kbaslik.objects.all()
    
    paginator = Paginator(kategoriler, 1)
    page = request.GET.get('page', 1)
    page_obj = paginator.get_page(page)
    
    return render(request, 'index.html', {
        'page_obj': page_obj,
        'kategoriler': kategoriler,
        'navbarKategori':navbarKategori,
        'searc':searc,
    })
#html referance için farklı bir sayfa denemesi
def html(req,ref_ad):
    searc = Kategori.objects.filter(Q(isim__icontains='tutorial') | Q(isim__icontains='referance') & Q(tutorialActive=True)) 
    kategoriler = Kategori.objects.filter(Q(slug__icontains=ref_ad)|Q(parent__slug__icontains=ref_ad) , Q(referanceActive=True))
    paginator = Paginator(kategoriler, 1)
    navbarKategori = Kbaslik.objects.all()
    page = req.GET.get('page', 1)
    page_obj = paginator.get_page(page)
    
    return render(req, 'layout.html', {
        'page_obj': page_obj,
        'kategoriler': kategoriler,
        'navbarKategori':navbarKategori,
        'searc':searc,
    })
    
    
#kategori isimlerine göre navbarda tıklanılan kurs a gimesi için filtrelenmiş view
def deneme(req,kat_ad):
    kategoriler = Kategori.objects.filter(Q(isim__icontains=kat_ad)& Q(tutorialActive=True))
    searc = Kategori.objects.filter(Q(isim__icontains='tutorial') | Q(isim__icontains='referance') & Q(tutorialActive=True)) 
    navbarKategori = Kbaslik.objects.all()
    
    paginator = Paginator(kategoriler, 1)
    page = req.GET.get('page', 1)
    page_obj = paginator.get_page(page)
    
    return render(req, 'layout.html', {
        'page_obj': page_obj,
        'kategoriler': kategoriler,
        'searc':searc,
        'navbarKategori':navbarKategori,
    })


# gerek kalmadı 
# def search(req,):  
#     if "q" in req.GET and req.GET["q"] != "":
#         q=req.GET["q"]
#         kategoriler =Kategori.objects.filter(isim__contains = q).order_by('isim')
#         paginator = Paginator(kategoriler, 1)
#         page = req.GET.get('page', 1)
#         page_obj = paginator.get_page(page)
    
#     else:
#         return redirect ('/')
#     return render(req,'layout.html',{
#         'kategoriler':kategoriler,
#         'page_obj': page_obj,
#     })