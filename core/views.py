from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from http import HTTPStatus
from .models import Review


def index(request):
    reviews = Review.objects.filter(is_active=True).order_by('-created')
    context = {
        'Title': 'BigHouzzz',
        'Header1': 'Главная страница!',
        'Reviews': reviews,
    }
    return render(request, 'core/index.html', context)


class AboutProjectView(TemplateView):
    template_name = 'core/about.html'


class ContactsView(TemplateView):
    template_name = 'core/contacts.html'


def page_not_found(request, exception):
    return render(
        request,
        'core/404.html',
        {'path': request.path},
        status=HTTPStatus.NOT_FOUND
    )


def server_error(request, *args, **argv):
    return render(request, 'core/500.html')


def csrf_failure(request, reason=''):
    return render(request, 'core/403csrf.html')