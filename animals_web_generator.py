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

    if animal['characteristics'].get('diet'):
        diet = animal['characteristics']['diet']
        # add diet info
        html_string += f"<li>{strong_html_string("Diet:")} {diet}</li>\n"

    location = animal['locations'][0]

    # add location info
    html_string += f"<li>{strong_html_string("Location:")} {location}</li>\n"

    if animal['characteristics'].get('type'):
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

    with open('animals.html', 'w') as file:
        file.write(content)


def main():
    """The main function"""
    input_animal = input("Enter a animal name: ")

    data = data_fetcher.fetch_data(input_animal)

    html_string = generate_html_string(data)

    creates_new_html_file(html_string)
    print("The html string has been generated successfully.")


if __name__ == '__main__':
    main()