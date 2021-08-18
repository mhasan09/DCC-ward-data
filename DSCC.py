import xlrd
from googletrans import Translator
#defining the path
path = "./data/dscc_data.xlsx"
inputWorkBook = xlrd.open_workbook(path)
inputWorkSheet = inputWorkBook.sheet_by_index(0)
json_data = []
translator = Translator()
#we're getting the data from a excel sheet, which we devide into rows and columns
for i in range(1, inputWorkSheet.nrows):
    ward_data = {
        "area_name": {
            "en": inputWorkSheet.cell_value(i, 1),
            "bn": translator.translate(inputWorkSheet.cell_value(i, 1), dest='bn')
        },
        "city_corporation": "Dhaka South City Corporation",
        "city_corp_tag": "DSCC",
        "ward": str(int(inputWorkSheet.cell_value(i, 0)))
    }
    json_data.append(ward_data)
print(json_data)

'''
That's our data output format
 {
      "area_name": {
         "en": "Uttara Model Town",
         "bn": "উত্তরা মডলে টাউন"
      },
      "city_corporation": "Dhaka North City Corporation",
      "city_corp_tag": "DNCC",
      "ward": "1"
   },
   
'''
