from django.http import JsonResponse, HttpResponseNotFound


def index(request):
    if request.method == 'GET':
        data = {
            'name': 'Foo',
            'bar': 'Bar',
            'method': 'GET'
        }
    elif request.method == 'POST':
        data = {
            'name': 'Foo',
            'bar': 'Bar',
            'method': 'POST'
        }

    else:
        return HttpResponseNotFound('Oops')

    return JsonResponse(data)
