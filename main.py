import requests

def Who_very_smart(hero_list: list):

    hero_id_list = []
    hero_int_list = []
    for i in hero_list:
        url = f"https://superheroapi.com/api/2619421814940190/search/{i}"
        resp1 = requests.get(url)
        hero_id_list.append(resp1.json()['results'][0]["id"])

    for i in hero_id_list:
        url = f"https://superheroapi.com/api/2619421814940190/{i}/powerstats/"
        resp1 = requests.get(url)
        hero_int_list.append(int(resp1.json()["intelligence"]))

    print(f"Very smarter is this {hero_list[hero_int_list.index(max(hero_int_list))]}")

hero_list = ["Hulk", "Captain America", "Thanos"]
Who_very_smart(hero_list)



