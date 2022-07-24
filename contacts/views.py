from django.shortcuts import render, redirect
from order.tg import contact_us



def contacts(request):
    return render(request, 'contacts/contacts.html')


def get_form(request):
    data = request.POST
    contact_us(data)
    return render(request, 'contacts/done.html')



