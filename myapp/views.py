"""
This module contains the views for the Myapp app.
"""

import datetime
from django.shortcuts import render


def home(request):
    """
    Renders the home page.

    If a POST request is received, checks whether a 'check' parameter was sent
    and sets the 'is_active' variable accordingly.
    """
    is_active = True
    if request.method == 'POST':
        check = request.POST.get("check")
        print(check)
        if check is None:
            is_active = False
        else:
            is_active = True

    date = datetime.datetime.now()
    name = "LearnCodeWithDurgesh"
    list_of_programs = [
        'WAP to check even or odd',
        'WAP to check prime number',
        'WAP to print all prime numbers from 1 to 100',
        'WAP to print pascals triangle'
    ]
    student = {
        'student_name': "Rahul",
        'student_college': "ZYZ",
        'student_city': 'LUCKNOW'
    }

    data = {
        'date': date,
        'is_active': is_active,
        'name': name,
        'list_of_programs': list_of_programs,
        'student_data': student
    }
    return render(request, "home.html", data)


def about(request):
    """
    Renders the about page.
    """
    return render(request, "about.html", {})


def services(request):
    """
    Renders the services page.
    """
    return render(request, "services.html", {})
