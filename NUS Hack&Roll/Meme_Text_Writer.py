#Making final function call to write generated captions to create memes.

from Photo_Text_Writer import make_meme

def meme_writer(msg,position,img):
    if(position==0):
        make_meme(bottomString=msg,topString='',filename=img)
    else:
        make_meme(bottomString='',topString=msg,filename=img)
