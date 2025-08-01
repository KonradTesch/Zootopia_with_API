import requests

API_KEY = "tkS2l43VBWlA3FJjbcpoaw==zvgRWe26Wbps8RIP"

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
      'name': ...,
      'taxonomy': {
        ...
      },
      'locations': [
        ...
      ],
      'characteristics': {
        ...
      }
    },
    """
    api_url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"

    header = {
      "X-Api-Key": API_KEY
    }

    response = requests.get(api_url, headers=header)

    if response.status_code == requests.codes.ok:
        if len(response.json()) == 0:
            print(f"The animal {animal_name} was not found.")

        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return []