from django import forms 
from django.conf import settings
import requests 
import ssl  
import json

class ApiLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)

    def search(self):
        result = {}
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        endpoint = 'https://190.64.82.90:9898/AGEOS/services/user/login/?usuario={userid}'
        url = endpoint.format(userid=username)
        headers = {'content-type': 'application/json'}
        data = {"usuario": username, "password": password}
        response = requests.post(url, headers=headers, verify=False, data=json.dumps(data))
        print('Resupuestaaaaaaa: ',response)
        if response.status_code == 200:
            #print('Entre por el 200 con response = ',response)
            #result = response.json() //esto es si viene en formato json
            #result['success'] = True
            elraw = response.raw.decode_content
            #print("resultadooo = ",resultado)
            elcontent = response.content 
            #print("otroooooo = ",otro)
            elhtml = response.text
            result = {'success':True, 'elraw':elraw, 'elcontent':elcontent, 'elhtml': elhtml}
            #print('result', result)
            
            #print(response.text)
        else:
            result['success'] = False
            if response.status_code == 200:
                print('Entre por el 404')
                result['message'] = 'Error 404'
            else:
                print('Entre por el vaya uno a saber')
                result['message'] = 'Error no identificado'
        
        return result


