__author__ = 'satyam'

import PIL
from editpyxl import Workbook
#import openpyxl as xl
from datetime import datetime
import datetime as dt
import shutil
# import TimeCardSystem as tcs

wb = Workbook()
MAIN_DATE = "02-20-2020"
# wb.open("blank template sheet.xlsx")

#sheet = wb.active

def check_date():
    print(dt.date.today())

    return

def write_to_excel (f_name,find_date, time, is_night_shift):


    if check_name(f_name):
       set_sheet(f_name)
       print("found sheet")
    else:
        print("not found: " + f_name)
        create_sheet(f_name)
        set_sheet(f_name)

    ws = wb[f_name]
    if is_night_shift:
        print("it is night shift")
    #    int(find_date[])
        print(int(find_date[3:5]))

        cell_coordinate = find_day(find_date,ws)

    if cell_coordinate == 0:
        print("Date doesn't exist")
        return
    next_empty_cell = check_for_empty_cell(cell_coordinate)
    if next_empty_cell == 0:
        print("All shifts are full")
        return
    assign_new_time(next_empty_cell,time)

    # next_cell_coordinate = cell_coordinate
    # next_cell_coordinate = chr(ord(next_cell_coordinate[0]) + 2) + cell_coordinate[1]
    # next_empty_cell = check_for_empty_cell(next_cell_coordinate)


    return

def check_name(f_name):
    for s in range(len(wb.sheetnames)):
        if wb.sheetnames[s] == f_name:
            return True

    return False

def create_sheet(f_name):
    # opening the source excel file
    #workbook = load_workbook(filename="Time card with Calculator copy.xlsx", read_only=False)

    # blank_sheet = load_workbook(filename="blank template sheet.xlsx",read_only=False)

    filename_src = "blank template sheet.xlsx"
    new_sheet = f_name + MAIN_DATE + ".xlsx"
    # new_sheet = "Test Run.xlsx"

    shutil.copy2("D:\\PycharmProjects\\Excel_timecard\\" + filename_src,"D:\\PycharmProjects\\Excel_timecard\\" + new_sheet,follow_symlinks=True)
    wb.open(new_sheet)
    ws = wb.active
    ws.cell('D5').value = "04:20"

    wb.save(new_sheet)
    wb.close()

    return


def set_sheet (f_name):
    for s in range(len(wb.sheetnames)):
        if wb.sheetnames[s] == f_name:
            break
#    sheet = workbook[f_name]
    wb.active= s
    global sheet
    sheet = wb.active
    return

def find_day(find_date,ws):
    find_date_format = dt.datetime.strptime(find_date, "%m-%d-%Y")
    for cols in ws.iter_cols():
       for cell in cols:
           if cell.value == find_date_format:
               print("Found the date: ")
               return cell.coordinate
    print("Date not found")
    return 0

def check_for_empty_cell(next_cell_coordinate):
    # final_cell_value = ""
    # while next_cell_coordinate[0] <= 'O':
    #     cell = sheet[next_cell_coordinate]
    #     final_cell_value = cell.coordinate
    #     # print(cell)
    #     # print(cell.value)
    #     print(sheet)
    #     print(cell.value)
    #     if cell.value == 0:
    #         break
    #     else:
    #         next_cell_coordinate = chr(ord(next_cell_coordinate[0]) + 1) + next_cell_coordinate[1]
    # if final_cell_value[0] == 'O':
    #     return 0
    # else:
    #     print(final_cell_value)
    #     return final_cell_value
    ws = wb.active
    cell_row = next_cell_coordinate[1:]
    cell_row = int(cell_row)
    for col in ws.iter_cols(min_row=cell_row ,min_col = 0, max_row = cell_row, max_col = 14):
        for cell in col:
            if cell.value is None:
                print(cell.coordinate)
                return cell.coordinate
    return 0

def assign_new_time(next_empty_cell, time):

    print(sheet)
    print(time)
    sheet[next_empty_cell] = time
    # sheet.cell.value = time

    return

def reset_time_card():
    for s in range(len(wb.sheetnames)):
        set_sheet(wb.sheetnames[s])
        # for row in sheet['D5:D11']:
        #     for cell in row:
        #         cell.value = None
        ws = wb.active
        #control cell columns
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
                        cell.value = None
            column_top = 21
            column_bottom = 27
    return

#'F5:F11','H5:H11','J5:J11','L5:L11','N5:N11','D21:D27','F21:F27','H21:H27','J21:J27','L21:L27','N21:N27'


def load_file(load_this_file):
    temp = datetime.strptime(MAIN_DATE, '%m-%d-%Y')
    day_difference = datetime.today().date() - temp.date()

    print(datetime.today().date())
    print(temp.date())
    print(day_difference.days)

    # if day_counter <= 13:
    #     global file_name
    #     file_name = load_this_file
    #     return
    # else:
    #     global MAIN_DATE
    #     MAIN_DATE = str(dt.date.today())
    return

if __name__ == "__main__":


    create_sheet("Time Card M6 Dixon ")
#    global MAIN_DATE
#    MAIN_DATE =
    create_sheet("test2 ")
    # ws = wb.active
    # ws.cell('T4').value = 9


    # reset_time_card()
    # is_night_shift = True
    # # load_filename = "M6_Timecard_" + MAIN_DATE
    # # load_file(load_filename)
    # write_to_excel("Chinmay","08-19-2019","14:00",is_night_shift)
    # write_to_excel("Singh","08-19-2019","9:00",is_night_shift)
    # write_to_excel("Patricia","08-19-2019","9:34",is_night_shift)
    # write_to_excel("Veronica","08-19-2019","10:01",is_night_shift)
    # write_to_excel("Singh","08-19-2019","12:30",is_night_shift)
    # write_to_excel("Patricia","08-19-2019","14:20",is_night_shift)
    # write_to_excel("Veronica","08-19-2019","15:11",is_night_shift)
    # write_to_excel("Chinmay","08-19-2019","20:00",is_night_shift)


    # wb.save("Time card with Calculator.xlsx")
    # wb.close()