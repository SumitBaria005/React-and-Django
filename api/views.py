from django.http import JsonResponse

# Create your views here.


def home(request):
    return JsonResponse({
        'info': 'Welcome to Django Api Page',
        'name': 'Sumit'
    })
