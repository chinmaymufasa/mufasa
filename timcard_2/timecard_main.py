__author__ = 'satyam'


from editpyxl import Workbook
from datetime import datetime,timedelta
import shutil

MAIN_DATE = "02-21-2020"        #February 21 2020 as const date
wb = Workbook()


def write_to_excel(f_name, set_time, is_night_shift):
    wb.open("D:\\PycharmProjects\\timcard_2\\blank template sheet.xlsx")

    today_date = datetime.today().date()
    today_date = today_date.strftime("%x")

    if is_before_seven_am() and is_night_shift:
        special_clock_in(f_name,set_time)

#    assign_time(f_name,set_time,today_date)

    wb.save("D:\\PycharmProjects\\timcard_2\\blank template sheet.xlsx")
    wb.close()

    return
def is_before_seven_am():

    current_hour = datetime.now().strftime("%I")

    if int(current_hour) < 7:
        return True

    return False

def special_clock_in(f_name,set_time):
    previous_day = datetime.now()-timedelta(1)
    print(previous_day)


    return

def assign_time(f_name,set_time,set_date):
    for s in range(len(wb.sheetnames)):
        if wb.sheetnames[s] != f_name:
            continue
        elif wb.sheetnames[s] == f_name:
            print("found sheet")
            wb.active = s
            sheet = wb.active

            find_date_format = datetime.strptime(str(set_date), "%m-%d-%Y")
            for cols in sheet.iter_cols():
                for cell in cols:
                    if cell.value != find_date_format:
                        continue
                    elif cell.value == find_date_format:
                        print("Found the date: ")
                        cell_row = cell.coordinate[1:]
                        cell_row = int(cell_row)
                        for col in sheet.iter_cols(min_row=cell_row ,min_col = 0, max_row = cell_row, max_col = 14):
                            for cells in col:
                                if cells.value is not None:
                                    continue
                                else:
                                    print("set ", cells.coordinate, " to ", set_time)
                                    cells.value = set_time
                                    return
    print("nope")




    return


def check_and_set_date(is_night_shift):
    temp = datetime.strptime(MAIN_DATE, '%m-%d-%Y')
    day_difference = datetime.today().date() - temp.date()

    print(datetime.today().date())
    print(temp.date())
    print(day_difference.days)
    print(day_difference.days %  14)
    wb.open("D:\\PycharmProjects\\timcard_2\\blank template sheet.xlsx")
    ws = wb.active
    column_top = 5
    column_bottom = 11
    row_fixed_1 = 4
    row_fixed_2 = 16

    for x in range(0,2,1):
        for y in range(row_fixed_1,row_fixed_2,2):
            for row in ws.iter_rows(column_top,column_bottom,y,y):
                #5,11,4,4 week 1, in: column 1
                #5,11,6,6 week 1, out: column 2
                #21, 27,4,4 week 2, in: column 1
                #21, 27,6,6 week 2, out: column 2
                for cell in row:
                    cell.value = "04:20"
        column_top = 21
        column_bottom = 27

    wb.save("D:\\PycharmProjects\\timcard_2\\blank template sheet.xlsx")
    wb.close()
    return

if __name__ == "__main__":
    write_to_excel("Chinmay", "13:30", False)
