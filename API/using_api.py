import requests

def get_apod():
    api_key = "enter your api key"  # Replace with your NASA API key
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

    # Request data from NASA API
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        # Extract data from the response
        title = data['title']
        explanation = data['explanation']
        image_url = data['url']

        print(f"Title: {title}")
        print(f"Explanation: {explanation}")
        print(f"Image LinkL {image_url}")
    else:
        print("Error fetching data from NASA API.")

get_apod()

