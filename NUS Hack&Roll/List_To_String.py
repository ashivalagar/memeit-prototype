def LTS(List):
    String=''
    for i in List:
        String+=str(i)
    return String

def splitwords(text):
    text=text.split(' ')
    String=''
    for i in text:
        if(i[-4:]=='.com'):
            pass
        else:
            String+=i
            String+=" "


    return String
