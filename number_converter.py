'''
The data could in Bengali numeric form this function will convert this into English numeric form
'''
bengali = {
            '০': 0,
            '১': 1,
            '২': 2,
            '৩': 3,
            '৪': 4,
            '৫': 5,
            '৬': 6,
            '৭': 7,
            '৮': 8,
            '৯': 9
        }

def toEnglish(string):
    x = ''
    for i in string:
        if i in bengali:
            i = bengali[i]
            x = str(i) + x
    return x



print(toEnglish('০১'))




