from django.shortcuts import render
import requests
import json

# Create your views here.

#APIKEY=YnKVpJET8HP4qn5ohBi2Yg==ThzjeNI3Q8yfaoBW


def home(request):

    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url + query, headers ={'X-Api-Key': 'YnKVpJET8HP4qn5ohBi2Yg==ThzjeNI3Q8yfaoBW'})
        try:
            food =json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            food ="oopa tropa - eroarea!"
            print(e)
        return render(request, 'home.html', {'food': food})
    else:
        return render(request, 'home.html', {'query': 'Enter a valid query'})
