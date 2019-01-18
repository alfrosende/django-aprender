from django.shortcuts import render
import requests
from .forms import ApiLoginForm

def home(request):
    response = requests.get('http://freegeoip.net/json/')
    geodata = response.json()
    print(geodata)

    return render(request, 'apirest/home.html',{'geodata': geodata})

    '''
    return render(request, 'apirest/home.html',{
        'ip': geodata['ip'],
        'country': geodata['country_name']
    })
    '''

def loginopus(request):
    search_result = {}
    if 'username' in request.GET:
        form = ApiLoginForm(request.GET)
        if form.is_valid():
            search_result = form.search()
    else:
        form = ApiLoginForm()
    
    return render(request, 'apirest/login.html', {'form': form, 'search_result': search_result})


