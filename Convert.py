from xml.etree import ElementTree
import csv
xml=ElementTree.parse("sample.xml")
csvfile=open("export.csv","w",encoding='UTF-8')
csvfile_writer=csv.writer(csvfile)
csvfile_writer.writerow(["Date","Maturity","DBTS_Code","Price","FileName"])
for item in xml.findall("item"):
    if(item):
        Date=item.find("Date")
        Maturity=item.find("Maturity")
        DBTS_Code=item.find("DBTS_Code")
        Price=item.find("Price")
        FileName=item.find("FileName")
        csv_line=[Date.text,Maturity.text,DBTS_Code.text,Price.text,FileName.text]
        csvfile_writer.writerow(csv_line)
csvfile.close()