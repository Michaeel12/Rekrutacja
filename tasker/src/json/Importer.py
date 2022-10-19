import json


class Importer:

    def __init__(self):
        pass

    def read_tasks(self):
        with open('taski.json','r') as file:
            return json.load(file)



        # TODO odczytaj plik i zdekoduj treść tutaj


    def get_tasks(self):

        return self.read_tasks()

