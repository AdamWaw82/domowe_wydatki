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

    def create(self, data):
        data.pop('csrf_token')
        self.wydatki_list.append(data)

    def save_all(self):
        with open("wydatki.json", "w") as f:
            json.dump(self.wydatki_list, f, default=str)

    def remove(self, id):
        del self.wydatki_list[id]

    def get(self, id):
        return self.wydatki_list[id]

    def update(self, id, data):
        data.pop('csrf_token')
        self.wydatki_list[id] = data
        self.save_all()
