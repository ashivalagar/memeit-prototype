from photoTextWriter import make_meme
def meme_writer(msg,position,img):
    if(position==0):
        make_meme(bottomString=msg,topString='',filename=img)
    else:
        make_meme(bottomString='',topString=msg,filename=img)
