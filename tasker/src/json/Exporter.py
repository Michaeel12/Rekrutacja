import json


class Exporter:

    def __init__(self):
        pass



    def save_tasks(self,tasks):
        self.tasks = tasks
        with open('D:/PythonProjekty/Projects/taski.json','w') as file:
            json.dump(self.tasks, file)
        # TODO zapisz taski do pliku tutaj

