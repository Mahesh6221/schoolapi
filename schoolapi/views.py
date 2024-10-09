from django.http import HttpResponse, JsonResponse



def home(request):
    data = [
    'mahesh',
    'umesh',
    'harish'
    ]
    return JsonResponse(data,safe=False)