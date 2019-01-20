import io
import os

def detect_text(path):
    text_list=''
    """Detects text in the file."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)


    texts = response.text_annotations
    #print('Texts:')
    if(len(texts)!=0):
        text_list=texts[0].description.replace('\n', ' ')
        return(text_list)

    else:
        return('')
#detect_text(" 2rdet5.jpg")
