import xlrd
path = "./data/dscc_data.xlsx"
inputWorkBook = xlrd.open_workbook(path)
inputWorkSheet = inputWorkBook.sheet_by_index(0)
json_data = []

for i in range(1,inputWorkSheet.nrows):
    ward_data = {
        "area_name": {
            "en": inputWorkSheet.cell_value(i,1),
            "bn": ""
        },
        "city_corporation": "Dhaka South City Corporation",
        "city_corp_tag": "DSCC",
        "ward": int(inputWorkSheet.cell_value(i,0))
    }
    json_data.append(ward_data)
print(json_data)

'''
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