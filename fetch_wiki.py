import requests

def get_image(city):
    headers = {'User-Agent': 'WeatherApp4U/1.0'}
    
    # First search for the city and landmark to get the most relevant page
    search_url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={city} landmark&utf8=&format=json"
    r = requests.get(search_url, headers=headers)
    search_data = r.json()
    
    try:
        title = search_data['query']['search'][0]['title']
    except (KeyError, IndexError):
        title = city

    # Fetch the image for the title
    wiki_url = f"https://en.wikipedia.org/w/api.php?action=query&prop=pageimages&titles={title}&format=json&pithumbsize=1000"
    wiki_data = requests.get(wiki_url, headers=headers).json()
    
    pages = wiki_data.get('query', {}).get('pages', {})
    for page_id, page_info in pages.items():
        if 'thumbnail' in page_info:
            return page_info['thumbnail']['source']
    
    # fallback to just the city name if landmark search yields no image
    if title != city:
        wiki_url = f"https://en.wikipedia.org/w/api.php?action=query&prop=pageimages&titles={city}&format=json&pithumbsize=1000"
        wiki_data = requests.get(wiki_url, headers=headers).json()
        pages = wiki_data.get('query', {}).get('pages', {})
        for page_id, page_info in pages.items():
            if 'thumbnail' in page_info:
                return page_info['thumbnail']['source']
                
    return None

for city in ["Tokyo", "London", "Goa", "Pune", "Paris", "Las Vegas", "Kyoto"]:
    print(f"{city}: {get_image(city)}")
