#csv write read utility by python
import csv
#to open and read request url and many other operation
import urllib.request
#for scraping
from bs4 import BeautifulSoup


#Example Inputs::
#https://en.wikipedia.org/wiki/List_of_public_listed_software_companies_of_India
#wiki table sortable
#dataoutput.csv

#get the inputs
print("input the url from which data has to be extracted")
input_url=input()
print("input the class name of the table on which scraping has to be done")
class_name=input()
print("input the output file name with csv extension")
outputfile=input()

#open the file in write mode
f=open(outputfile,'w',newline='')
writer=csv.writer(f)

#opent the url to scrape
soup=BeautifulSoup(urllib.request.urlopen(input_url).read(),'lxml')

#we want to table contents so
#find the table body of a particular website to extract
tbody=soup('table',{"class":class_name})[0].find_all('tr')
for row in tbody:
	cols=row.findChildren(recursive=False)
	cols=[ele.text.strip() for ele in cols]
	writer.writerow(cols)