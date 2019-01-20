import xlwt
import Tag_Getter,Emo_Getter,Text_Getter
import Meme_Getter as meme
from ListToString import LTS,splitwords


book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")

def add_elements(row,tag,emo,text):
    #row=sheet1.max_row+1
    sheet1.write(row,0,row-1)
    sheet1.write(row,1,tag)
    sheet1.write(row,2,emo)
    sheet1.write(row,3,text)

sheet1.write(0,0,'Sl.No')
sheet1.write(0,1,'Tags')
sheet1.write(0,2,'Emotion')
sheet1.write(0,3,'Text')

list_of_paths=meme.give_path("/Users/vivekadrakatti/Documents/NUS Hack&Roll/memes")
j=1
for i in list_of_paths:

    tag=LTS(Tag_Getter.detect_labels(i))
    emo=LTS(Emo_Getter.detect_faces(i))
    text=LTS(splitwords(Text_Getter.detect_text(i)))

    add_elements(j,tag,emo,text)
    print(j)
    j+=1
    book.save("finalfinal.xls")

sheet1.write(0,5,j)
