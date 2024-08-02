import json


class Wydatki():
    wydatki_list = []

    def __init__(self):
        try:
            with open("wydatki.json", mode='r') as file:
                self.wydatki_list = json.load(file)
        except Exception as e:
            print(e)

    def get_all(self):
        return self.wydatki_list

    def add(self, data):
        self.wydatki_list.append(data)
