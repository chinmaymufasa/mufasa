from editpyxl import Workbook
from editpyxl import Worksheet
from datetime import datetime
import shutil

MAIN_DATE = "02-21-2020"        #February 21 2020 as const date

def write_to_excel(f_name, set_time, is_night_shift):
    check_and_set_date(is_night_shift)

    return

def check_and_set_date(is_night_shift):
    temp = datetime.strptime(MAIN_DATE, '%m-%d-%Y')
    day_difference = datetime.today().date() - temp.date()

    print(datetime.today().date())
    print(temp.date())
    print(day_difference.days)


    return
















