from django.shortcuts import render
from django.contrib import messages
import requests
import datetime

def home(request):
    if 'city' in request.POST:
         city = request.POST['city']
    else:
         city = 'goa'
         
    OPENWEATHERMAP_API_KEY = "d4d0287496367498b29be85d8c75b449"
    PARAMS = {'q': city, 'appid': OPENWEATHERMAP_API_KEY, 'units': 'metric'}
    
    # Handle Image Search using Wikipedia API (Free, no API key required)
    # First search for the city to get the most relevant page
    search_url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={city}&utf8=&format=json"
    image_url = ""
    try:
        search_data = requests.get(search_url, headers={'User-Agent': 'WeatherApp4U/1.0'}).json()
        title = search_data['query']['search'][0]['title']
    except (KeyError, IndexError, Exception):
        title = city

    try:
        # Fetch the image for the title
        wiki_url = f"https://en.wikipedia.org/w/api.php?action=query&prop=pageimages&titles={title}&format=json&pithumbsize=1000"
        wiki_data = requests.get(wiki_url, headers={'User-Agent': 'WeatherApp4U/1.0'}).json()
        pages = wiki_data.get('query', {}).get('pages', {})
        for page_id, page_info in pages.items():
            if 'thumbnail' in page_info:
                image_url = page_info['thumbnail']['source']
                break
    except Exception:
        pass  # Silently handle image search failure

    # Handle Weather Search
    url = "https://api.openweathermap.org/data/2.5/weather"
    description = ""
    icon = ""
    temp = ""
    day = datetime.date.today()
    exception_occurred = False

    humidity = ""
    wind_speed = ""
    pressure = ""
    feels_like = ""

    try:
        data = requests.get(url, params=PARAMS).json()
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        pressure = data['main']['pressure']
        feels_like = data['main']['feels_like']
    except (KeyError, IndexError):
        exception_occurred = True
        messages.error(request, 'Entered data is not available to API')

    return render(request, 'weatherapp/index.html', {
        'description': description, 
        'icon': icon, 
        'temp': temp, 
        'day': day, 
        'city': city, 
        'exception_occurred': exception_occurred, 
        'image_url': image_url,
        'humidity': humidity,
        'wind_speed': wind_speed,
        'pressure': pressure,
        'feels_like': feels_like

    })