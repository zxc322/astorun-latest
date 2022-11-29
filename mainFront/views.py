from django.shortcuts import render
from .models import Documentation


def main(request):
	return render(request, 'mainFront/main.html')


def scroll(request):
	return render(request, 'mainFront/page404.html')


def FAQ(request):
	return render(request, 'mainFront/FAQ.html', {'FAQ': Documentation.objects.get(slug='faq')})


def RULES(request):
	return render(request, 'mainFront/RULES.html', {'RULES': Documentation.objects.get(slug='rules')})


def OFFER(request):
	return render(request, 'mainFront/OFFER.html', {'OFFER': Documentation.objects.get(slug='offer')})


def DELIVERY(request):
	return render(request, 'mainFront/DELIVERY.html', {'DELIVERY': Documentation.objects.get(slug='delivery')})


def ABOUT_US(request):
	return render(request, 'mainFront/ABOUT_US.html', {'ABOUT_US': Documentation.objects.get(slug='about_us')})
