import random
import requests


def generate_random_character():

    url = 'https://hp-api.onrender.com/api/characters'
    response = requests.get(url)
    characters = response.json()

    character_dict = {character['id']: {'name': character['name'], 'species': character['species'], 'house': character['house'], 'patronus': character['patronus']} for character in characters}

    random_id = random.choice(list(character_dict.keys()))

    character_data = character_dict[random_id]
    character_name = character_data['name']
    character_species = character_data['species']
    character_house = character_data['house']
    character_patronus = character_data['patronus']

    random_character = {
        'id': random_id,
        'name': character_name,
        'species': character_species,
        'house': character_house,
        'patronus': character_patronus
    }

    return random_character


def run():

    my_character = generate_random_character()
    print('You were given {}'.format(my_character['name']))

    stat_choice = input('Which stat do you want to use? (name, species, patronus, house) ')
    opponent_character = generate_random_character()
    print('The opponent chose: {}'.format(opponent_character['name']))

    my_stat = my_character[stat_choice]
    opponent_stat = opponent_character[stat_choice]

    print('You chose this stat: {}'.format(my_stat))
    print('The opponents stat was: {}'.format(opponent_stat))

    if my_stat > opponent_stat:
        print('You Win!')
    elif my_stat < opponent_stat:
        print('You Lose!')
    else:
        print('Draw!')


run()
