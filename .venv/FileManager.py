import csv
from Task import Task

class FileManager:
    def saveList(self,list):
        with open("storageFile",mode="w",newline="") as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            #writer.writerow("Name;Status".split(","))
            for t in list:
                writer.writerow(t.toStringCSV().split(","))

    def loadList(self):
        result = []
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

