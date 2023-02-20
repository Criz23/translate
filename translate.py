from textblob import TextBlob 
from io import open
import re

def readFile():
	file = open("_django.po", "r")
	file_l = file.readlines()
	file.close()
	return file_l

def translate(cadena):
	try:
		blob = TextBlob(cadena) 
		return(str(blob.translate(from_lang='en', to='zh-hans')))
	except:
		return cadena


msgid = False
string = ""
string_t = ""
pat = r'"(.*?)"'
i = 0
j = 0


file_l = readFile()
file_r = open("django.po", "w")
for linea in file_l:
	if (linea[0:5] == "msgid"):
		string = re.findall(pat,linea)
		string_t = translate(string[0])
		file_r.write(linea)
		i =i+1
		print (i)
	elif (linea[0:6] == "msgstr"):
		print(linea[0:6])
		file_r.write('msgstr "' + string_t + '"')
		file_r.write('\n')
		print('msgstr "' + string_t + '"')
		j = j+1
		print (j)
	else:
		file_r.write(linea)
file_r.close()

