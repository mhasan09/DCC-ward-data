'''
Sometimes the data is in bengali which needs to be translated. It's from the google Translator API library in PyPI
'''

from googletrans import Translator
import time
start_time = time.time()
translator = Translator()
translation = translator.translate("Gulistan", dest='bn')
translation1 = translator.translate("Mirpur", dest='bn')
translation2 = translator.translate("Gopibagh", dest='bn')
translation3 = translator.translate("Maniknagar Purbo (East)", dest='bn')
translation4 = translator.translate("Kamlapur Dakkhin (South)", dest='bn')
translation5 = translator.translate("Dakshin Mir Hazirbagh", dest='bn')
print("Gulistan _>", translation.text)
print("Mirpur ->", translation1.text)
print("Gopibagh ->", translation2.text)
print("Maniknagar Purbo (East) ->", translation3.text)
print("Kamlapur Dakkhin (South) ->", translation4.text)
print("Dakshin Mir Hazirbagh ->", translation5.text)
print("--- %s seconds ---" % (time.time() - start_time))