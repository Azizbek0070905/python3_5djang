from django.contrib import admin
from myfiles.models import *


# Register your models here.

class Adminservices(admin.ModelAdmin):
    list_display = ["img", "name", "malumot", "date"]


admin.site.register(Services, Adminservices)


class Admintype(admin.ModelAdmin):
    list_display = ["turi"]


admin.site.register(Type, Admintype)


class Adminportfolio(admin.ModelAdmin):
    list_display = ["img", "name", "type", "category", "client", "date", "link", "matn"]


# "image", "rasm",

admin.site.register(Portfolio, Adminportfolio)


class Adminkasbi(admin.ModelAdmin):
    list_display = ["hodim"]


admin.site.register(Kasbi, Adminkasbi)


class Adminteam(admin.ModelAdmin):
    list_display = ["name", "kasbi", "malumot", "img", "twit", "face", "inst", "tele", "date"]


admin.site.register(Team, Adminteam)


class Admincontact(admin.ModelAdmin):
    list_display = ["nomi", "email", "mavzu", "matn", "date"]


admin.site.register(Contact, Admincontact)

class AdminSubcribe(admin.ModelAdmin):
    list_display = ["email", "date"]

admin.site.register(Subcribe, AdminSubcribe)



class AdminSubcribe1(admin.ModelAdmin):
    list_display = ["gmail", "date"]

admin.site.register(Subcribe1, AdminSubcribe1)