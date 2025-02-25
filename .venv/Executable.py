from distutils.command.check import check
from TaskManager import TaskManager
from FileManager import FileManager
from GUI import GUI
from Menu import *
import sys
import os
from DiaryItems import *

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Command.TaskerCommands import *
from Command.DairyCommands import *
from Command.MenuCommands import *


'''
prog = GUI()
prog.runLoop()
'''
fileManager = FileManager()
day = fileManager.loadDaily()
print(day.morning.purpose)
showstuff = showToday(day)
morning = fillMorning(day.morning)
evening = fillEvening(day.evening)
night = fillNight(day.night,day.morning)
saveDay = saveToday(day,fileManager)
Diary = Menu([showstuff,morning,evening,night,saveDay],"Diary")
openDry = openDiary(Diary)
taskmngr = TaskManager(fileManager.loadList())
add = addTask(taskmngr)
remove = removeTask(taskmngr)
check = checkTask(taskmngr)
show = show(taskmngr)
removeCh = removeChecked(taskmngr)
reset = reset(taskmngr)
save = saveTasker(taskmngr,fileManager)
load = loadTasker(taskmngr)
commandList = [add,remove,check,show,removeCh,reset]
tasker = MenuSave(commandList,"To Do List",save,load)
openTskr = openToDoList(tasker)
prog = Menu([openTskr,openDry],"Main APP")
prog.executionLoop()