from django.shortcuts import render
from myfiles.models import Portfolio, Services, Team, Contact, Subcribe, Subcribe1


# Create your views here.

def index(malumot):
    if "name" in malumot.POST:
        ism = malumot.POST.get("name")
        email = malumot.POST.get("email")
        subject = malumot.POST.get("subject")
        matn = malumot.POST.get("message")
        Contact(nomi=ism, email=email, mavzu=subject, matn=matn).save()
    elif "email" in malumot.POST:
        nom = malumot.POST.get("email")
        Subcribe(email=nom).save()
    elif "gmail" in malumot.POST:
        nomi = malumot.POST.get("gmail")
        Subcribe1(gmail=nomi).save()
    ports = Portfolio.objects.all()
    servi = Services.objects.all()
    team = Team.objects.all()
    return render(malumot, "index.html", {"ports": ports, "servi": servi, "team": team})


def inner_page(malumot):
    return render(malumot, "inner-page.html")


def portfolio(malumot, id):
    port = Portfolio.objects.get(id=id)
    return render(malumot, "portfolio-details.html", {"port": port})
