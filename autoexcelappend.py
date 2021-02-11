import pandas
from pandas import ExcelWriter

dt = pandas.read_excel(r'C:\Users\ABHIJITH UDAYAKUMAR\PycharmProjects\filerenameAutomation\Data\orig.xlsx', sheet_name="CORRECTED")

minlist = dt['only child'].tolist()
print(minlist)

orimin = []

for i in minlist:
    if i == 'NO':
        orimin.append(0)
    elif i == 'YES':
        orimin.append(1)
print(orimin)

dt['Ratio'] = orimin#dt['Theta']

dt.head(5)
dt.to_excel("yeye.xlsx") #Write DateFrame back as Excel file

#def ExcelUpdateADmissionNumber():
    # adnolist = dt['Admission No'].tolist()

    # admn = []

    # for i in adnolist:
    #    admn.append(str(i)+'.jpg')

    # print(admn)

    # dt['Ratio'] = admn#dt['Theta']
    # Display top 5 rows to check if everything looks good
    # dt.head(5)

    # To save it back as Excel
    # dt.to_excel("yeye.xlsx") #Write DateFrame back as Excel file