import json
import data_fetcher


def generate_html_string(data):
    """Generates a formatted html sting based on the animal data."""
    html_string = ""
    for animal in data:
        html_string += serialize_animal_info(animal)

    return html_string


def serialize_animal_info(animal):
    html_string = ""


    html_string += '<li class= "cards__item">\n'

    name = animal['name']
    # add name title
    html_string += f'<div class="card__title">{name}</div>\n'
    html_string += '<div class="card__text">\n<ul>\n'

    if 'diet' in animal['characteristics'].keys():
        diet = animal['characteristics']['diet']
        # add diet info
        html_string += f"<li>{strong_html_string("Diet:")} {diet}</li>\n"

    locations = animal['locations']
    # separates all locations with a ','
    locations = ", ".join(locations)

    # add location info
    html_string += f"<li>{strong_html_string("Location:")} {locations}</li>\n"

    if 'type' in animal['characteristics'].keys():
        animal_type = animal['characteristics']['type']
        # add type info
        html_string += f"<li>{strong_html_string("Type:")} {animal_type}</li>\n"


    html_string += f"</ul>\n</div>\n</li>\n\n"

    return html_string


def strong_html_string(text):
    """Returns a string with the html strong element"""
    return f"<strong>{text}</strong>"


def creates_new_html_file(html_string):
    """creates new html file with replaced html string"""
    with open('animals_template.html', 'r') as file:
        content = file.read()

    content = content.replace("__REPLACE_ANIMALS_INFO__", html_string)

    with open('../../../Downloads/My-Zootopia-main/animals.html', 'w') as file:
        file.write(content)


def main():
    """The main function"""
    data = data_fetcher.fetch_data()
    html_string = generate_html_string(data)

    creates_new_html_file(html_string)


if __name__ == '__main__':
    main()