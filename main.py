import os
import pandas

df = pandas.read_excel('data/data.xlsx', sheet_name="Sheet1")
adnolist = df['ADNO'].tolist()
namelist = df['Name'].tolist()
reglist = df['REG'].tolist()

newreg = []
newad = []

for val in reglist:
    val = val.replace('Reg No.:','')
    val = val.replace('/','')
    val = val+'.jpg'
    newreg.append(val)

for val in adnolist:
    newad.append(str(val)+'.jpg')


for count, filename in enumerate(os.listdir(os.curdir+"/Data/c/")):
    src = 'C:/Users/ABHIJITH UDAYAKUMAR/PycharmProjects/filerenameAutomation/Data/c/'+str(filename)
    ind = newreg.index(filename)
    dst = 'C:/Users/ABHIJITH UDAYAKUMAR/PycharmProjects/filerenameAutomation/Data/c/'+newad[ind]
    print("Renaming "+str(namelist[ind]))
    os.rename(src,dst)

