from django.shortcuts import render
from django.http import HttpResponse
from .models import Car
def ahalai (request):
    return HttpResponse('Petyh')
def mamalai(request):
    return HttpResponse('votonokak')
def kaka(request):
    return HttpResponse('qwerty')
def bobi(request,pyk,ylibaemca):
    return HttpResponse(pyk+ylibaemca)
def kok(request):
    a = 'b'
    j = {'okak':'pyknem','baka':'opandala'}
    return render(request,'index.html',{'keygen':a,'laka':j})
# `vokal = Car.objects.create(name = 'BMW', price = 1500000)`
# oioioioi = Car.objects.all()
# for i in oioioioi:
#     print(i.id,i.name,i.price)
# babochka = Car.objects.create(name = 'Nissan', price = 3000000)
# babochka = Car.objects.create(name = 'Mercedes', price = 7000000)
# babvka = Car.objects.create(name = 'Ferrari', price = 5200000)
# bab = Car.objects.create(name = 'Toyota', price = 3645000)
# bytulka = Car.objects.create(name = 'Skoda', price = 425000)
# popornoka = Car.objects.all()
# for i in popornoka:
#     print(i.id,i.name,i.price)
# moloko = Car.objects.get(id = 1)
# print(moloko.name, moloko.price)
# nokac = Car.objects.get(id = 7)
# nokac.Вelete()
# najol = Car.objects.order_by('-price')
# for i in najol:
#     print(i.name, i.price)
def ulaks(request):
    lola = Car.objects.all()
    return render(request, 'index.html', {'car': lola})
# kakaQ2 = Car.objects.get(id = 1)
# kakaQ2.name = 'Tesla'
# kakaQ2.save()



# hohan = Car.objects.create(name = 'Audi', price = 4000000)
#  = Car.objects.create(name = 'Lamborghini', price = 1400000)
# kokonut = Car.objects.create(name = 'Ford', price = 6000000)
# Hokala = Car.objects.create(name= 'Lada', price = 1000000)
# hohoho = Car.objects.all()
# for i jajopin hohoho:
#     print(i.id,i.name,i.price)



# nokamlola = Car.objects.get(id = 11)
# nokamlola.delete()
# oaeko = Car.objects.get(id = 10)
# oaeko.delete()



# nokokolal = Car.objects.order_by('-price')



# kokokalka = Car.objects.get()



# kokolalalako = Car.objects.get(id = 8)
# kokolalalako.price = 3500000
# kokolalalako.save()


# oioioioi = Car.objects.all()
# for i in oioioioi:
#     print(i.id,i.name,i.price)