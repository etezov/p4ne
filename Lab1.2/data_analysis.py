# Lab 1.2

from openpyxl import load_workbook
from matplotlib import pyplot

wb = load_workbook('data_analysis_lab.xlsx')  # Загрузка таблицы Excel из файла в переменную wb
sheet = wb['Data']  # Загрузка листа с именем "Data" в переменную sheet


def getvalue(x): return x.value  # Определение функции, возвращающей содержимое колонки таблицы


year = list(map(getvalue, sheet['A'][1:])) # Список по столбцу "Годы"
temp_rel = list(map(getvalue, sheet['C'][1:]))  # Список по столбцу "Относит. температура"
solar_activity = list(map(getvalue, sheet['D'][1:]))  # Список по столбцу "Активность"

pyplot.plot(year, temp_rel, label="temp_rel")  # Построение графика зависимости относит. температуры от года
pyplot.plot(year, solar_activity, label="solar_activity")  # Построение графика зависимости солнечной активности от года

pyplot.show()  # Вывод графика на экран
