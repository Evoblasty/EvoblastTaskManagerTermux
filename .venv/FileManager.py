import csv
import os
from distutils.command.check import check

from Task import Task
import json
from DiaryItems import *
from datetime import datetime, date
from setuptools.glob import glob0

class FileManager:
    def __init__(self):
        self.dayLoadedFlag = False

    def saveList(self,list):
        with open("storageFile",mode="w",newline="") as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            #writer.writerow("Name;Status".split(","))
            for t in list:
                writer.writerow(t.toStringCSV().split(","))

    def loadList(self):
        result = []
        if not os.path.exists("storageFile"):
            with open("storageFile", mode='w', newline='') as file:
                pass
            print("storageFile has been created as an empty file.")
        else:
            try:
                with open("storageFile", mode="r") as file:
                    reader = csv.reader(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    for row in reader:
                        task = Task(row[0],row[1])
                        result.append(task)
                    return result
            except FileNotFoundError:
                print(f"Error: El archivo '{ruta_csv}' no fue encontrado.")
                return []
            except PermissionError:
                print(f"Error: No tienes permisos para leer el archivo '{ruta_csv}'.")
                return []
            except Exception as e:
                print(f"Se produjo un error inesperado: {e}")
        return []

    def custom_serializer(self,obj):
        if hasattr(obj, "__dict__"):
            return obj.__dict__
        return str(obj)

    def saveDaily(self,day):
        day_list = []
        if os.path.exists("test1.json"):
            with open("test1.json", "r") as json_file:
                try:
                    day_list = json.load(json_file)  # Cargar la lista correctamente
                    if not isinstance(day_list, list):  # Asegurar que sea una lista
                        day_list = []
                except json.JSONDecodeError:
                    day_list = []  # Si el archivo está vacío o corrupto, empezar de nuevo
        if self.dayLoadedFlag:
            day_list[-1] = day
        else:
            day_list.append(day)
        with open("test1.json", "w") as json_file:
            json.dump(day_list, json_file, default=self.custom_serializer, indent=4)
        print("JSON file with nested object saved successfully!")

    def loadDaily(self):
        with open("test1.json", "r") as json_file:
            json_data = json_file.read()
        try:
            days = json.loads(json_data)
            day_dict = days[-1]
            dateObj = day_dict["date"]
            date_obj = datetime.strptime(dateObj, "%Y-%m-%d").date()
            if date.today() == date_obj:
                morning = Morning(day_dict["morning"]["w"],day_dict["morning"]["purpose"],day_dict["morning"]["virtue"])
                evening = Evening(day_dict["evening"]["w"],day_dict["evening"]["action"],day_dict["evening"]["reaction"],day_dict["evening"]["version"])
                night = Night(day_dict["night"]["w"],day_dict["night"]["goods"],day_dict["night"]["better"],day_dict["night"]["learning"],day_dict["night"]["virtue"],day_dict["night"]["death"])
                self.dayLoadedFlag = True
                return Day(dateObj,morning,evening,night)
            else:
                return Day()
        except json.JSONDecodeError as e:
            return Day()


