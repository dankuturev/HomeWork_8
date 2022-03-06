import requests


def best_hero(hero_list):
    hero_int = {}
    for hero_name in hero_list:
        url = 'https://superheroapi.com/api/2619421814940190/search/' + hero_name
        response = requests.get(url)
        hero_id = str(response.json()['results'][0]['id'])
        url = 'https://superheroapi.com/api/2619421814940190/' + hero_id + '/powerstats'
        response = requests.get(url)
        stats = response.json()['intelligence']
        hero_int[hero_name] = stats
        best_hero_list = max(hero_int.items(), key=lambda x: x[0])
    print(hero_int)
    print(f'Самый умный герой - {best_hero_list[0]}')


best_hero(['Hulk', 'Captain America', 'Thanos'])
