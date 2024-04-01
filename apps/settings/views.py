from django.http import HttpRequest
from django.shortcuts import render, redirect

from apps.settings.utils import send_contact_email
from . import models
from apps.telegram.views import get_text
from django.core.mail import send_mail

# Create your views here.
def index(request):
    setting_id = models.Settings.objects.latest('id')
    static_all = models.About.objects.all().order_by("?")[:3]
    static = models.Stati.objects.all().order_by()
    product_all = models.Product.objects.all()
    interesting = models.Interesting.objects.all()
    return render(request, "base/index.html", locals())


def about(request):
    about_id = models.AboutMain.objects.latest('id')
    static = models.Stati.objects.all()
    static_all = models.About.objects.all().order_by("?")[:3]
    return render(request, "base/about.html", locals())


def coming(request):
    return render(request, "base/coming-soon-full.html", locals())


def gellary(request):
    return render(request, "base/gallery.html", locals())


# добавоение талаграм бота
def contact_view(request):
    if request.method == "POST":
        message = request.POST.get('message')
        text = request.POST.get('text')
        email = request.POST.get('email')
        if message:
            models.Сontacts.objects.create(message=message, text=text, email=email)

        get_text(f""" Оставлен отзыв 
                Имя пользователя: {message}
                Номер телефона: {text}
                Сообщение: {email}
                """)
        return redirect('index')
    return render(request, 'base/contacts.html', locals())


def where(request):
    static_all = models.About.objects.all()
    return render(request, "base/where.html", locals())


def blog(request):
    return render(request, "blog/blog-list.html", locals())


# форма обратного связи
def contact(request: HttpRequest):
    settings = models.Settings.objects.latest("id")
    if request.method == "POST":
        last_name = request.POST.get('form[nom]')
        email = request.POST.get('form[email]')
        number = request.POST.get('form[tel]')
        message = request.POST.get('form[message]')

        send_mail(
            'Cheff Contact',
            f"""Здравствуйте.
            Спасибо за обратную связь, мы скоро свами свяжемся.
            Ваше ФИО: {last_name}
            Ваш email: {email}
            Ваш номер телефона: {number}
            Ваше сообщение: {message}...

            Если вы ошиблись при указании данных можете обратно зайти на сайт и оставить новый отзыв с исправленными
            данными! """,
            "noreply@somehost.local",
            ["nurlanuuulubeksultan@gmail.com"]
        )
        # Вызов задачи Celery для обработки формы с данными
        send_contact_email.delay(last_name, email, number, message)

        return redirect('index')
    return render(request, 'base/contacts.html', locals())



def not_faund(request):
    return render(request, "404/404.html", status=404)
