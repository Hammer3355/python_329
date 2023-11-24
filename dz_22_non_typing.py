import json



class JsonFileHandler:
    def __init__(self, filepath):
        self.data = None
        self.filepath = filepath

    def read_file(self, as_dict=False):
        with open(self.filepath, 'r', encoding='utf-8') as file:
            self.data = json.load(file)
            return self.data

    def write_file(self, data):
        with open(self.filepath, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def append_file(self, data):
        raise TypeError('Данный тип файла не поддерживает операцию дописывания')

    def get_cities_set(self, cities_list):
        cities_set = set()
        for city in cities_list:
            cities_set.add(city['name'])
        self.write_file(list(cities_set))
        return cities_set


class Cities:
    def __init__(self, cities_list):
        self.cities_set = set(cities_list)

    def get_cities_list(self):
        return set(self.cities_set)

    def remove_city(self, city):
        self.cities_set.discard(city)


class CityGame:
    def __init__(self, cities):
        self.cities = cities
        self.human_city = ''
        self.computer_city = ''

    def check_game_rules(self, last_city, new_city):
        if last_city[-1].lower() == new_city[0].lower():
            return True
        else:
            return False

    def human_step(self):
        self.human_city = input('Введите город: ')
        if self.human_city == 'стоп':
            print('Вы проиграли')
            return False
        if self.human_city not in self.cities.get_cities_list():
            print(f'Города {self.human_city} нет в списке. Вы проиграли')
            return False
        if self.computer_city:
            if not self.check_game_rules(self.computer_city, self.human_city):
                print(f'Вы проиграли. Ваш ответ не начинается на букву {self.computer_city[-1]}')
                return False
        self.cities.remove_city(self.human_city)
        self.human_city = self.human_city
        return True

    def computer_step(self):
        for city in self.cities.get_cities_list():
            if self.check_game_rules(self.human_city, city):
                print(f'Компьютер называет город: {city}')
                self.computer_city = city
                self.cities.remove_city(city)
                return True
        else:
            print('Вы победили! Компьютер не смог назвать город')
            return False


class GameManager:
    def __init__(self):
        self.json_file = JsonFileHandler('cities_cleaned.json')
        self.cities = Cities(self.json_file.read_file())
        self.game = CityGame(self.cities)

    def __call__(self):
        self.run_game()

    def run_game(self):
        while True:
            if not self.game.human_step():
                break
            if not self.game.computer_step():
                break


if __name__ == "__main__":
    game_manager = GameManager()
    game_manager()
