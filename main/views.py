from datetime import datetime
from typing import Any

from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from scripts import exceptions, youtube

from .models import *


def home(request) -> HttpResponse:
    return render(request, 'home.html')


def length(request) -> HttpResponse:
    if request.method == "POST":
        link: Any = request.POST.get("link")
        try:
            time: str = youtube.main(url=link, desc=True)
            return redirect("/done")
        except exceptions.LinkException:
            time: bool = None
            messages.error(request, "Your link was not found.")
        finally:
            return render(request, 'after.html', context={'time': time})
    return render(request, 'length.html')


def contact(request) -> HttpResponse:
    if request.method == "POST":
        email = request.POST.get("email")
        desc = request.POST.get("desc")
        now = datetime.now()
        contact = Contact(email=email, desc=desc, now=now)
        contact.save()
        messages.success(
            request, "Your message was sent to our team. Thank you for your feedback!")
    return render(request, 'contact.html')
