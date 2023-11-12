from django.shortcuts import render
from django.http import HttpResponse
from http import HTTPStatus


def index(request):
    context = {
        'Title': 'BigHouzzz',
        'Header1': 'Главная страница!',
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