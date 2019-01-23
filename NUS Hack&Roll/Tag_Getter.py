#Generating tags for each picture using Google Vision API's label detection function.


import io
import os
def detect_labels(path):
    """Detects labels in the file."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    #print('Labels:')
    #print(labels)
    tag_list=[]
    for label in labels:
       tag_list.append(label.description)
    return(tag_list)


#detect_labels("/Users/vivekadrakatti/Documents/2rdet5.jpg")
