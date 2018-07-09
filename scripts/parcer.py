import os
import sys
import django
import xlrd

def execute_command():
    from catalog.models import Price,Provider
    try:
#        print(sys.argv[0],sys.argv[1],sys.argv[2])
        rb = xlrd.open_workbook(sys.argv[1],formatting_info=True)
        print("The number of worksheets is {0}".format(rb.nsheets))
        print("Worksheet name(s): {0}".format(rb.sheet_names()))
#выбираем активный лист
        sheet = rb.sheet_by_index(0)
        print("{0} {1} {2}".format(sheet.name, sheet.nrows, sheet.ncols))
        print("Cell is {0}".format(sheet.cell_value(rowx=1, colx=1)))
        for rx in range(1,20):
            p = Price(provider=Provider.objects.first())
            p.nomenclature = sheet.cell_value(rowx=rx, colx=0)
            p.brend = sheet.cell_value(rowx=rx, colx=1)
            p.articul = sheet.cell_value(rowx=rx, colx=2)
            p.describe = sheet.cell_value(rowx=rx, colx=3)
            p.multi = sheet.cell_value(rowx=rx, colx=4)
            p.cost = sheet.cell_value(rowx=rx, colx=5)
            p.availability = sheet.cell_value(rowx=rx, colx=6)
            p.delivery = sheet.cell_value(rowx=rx, colx=7)
            p.catnumber = sheet.cell_value(rowx=rx, colx=8)
            p.oemnumber = sheet.cell_value(rowx=rx, colx=9)
            p.save()
#получаем список значений из всех записей
#        vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
#        print(vars(sheet.Range("A2:J2")))
    except Exception as e:
        print(e)

if __name__ == "__main__":
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zed_ad_ru.settings")
	django.setup()
	execute_command()