from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

# Create your views here.


class SearchView(View):

    def get(self, request):
        key = request.GET.get('key')
        print(key)
        return JsonResponse({'status': 'OK'})
