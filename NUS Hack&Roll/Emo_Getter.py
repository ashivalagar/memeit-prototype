import io
import os

def detect_faces(path):
    """Detects faces in an image."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    #print('Faces:')
    #print(faces)
    #
    # for face in faces:
    #     print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
    #     print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
    #     print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))

    if len(faces)!=0:
        emo_list=[]
        emo_list.append(faces[-1].joy_likelihood)
        emo_list.append(faces[-1].sorrow_likelihood)
        emo_list.append(faces[-1].anger_likelihood)
        emo_list.append(faces[-1].surprise_likelihood)
        emo_list.append(faces[-1].headwear_likelihood)
        return(emo_list)

    else:
        return([0,0,0,0,0])

#detect_faces("/Users/vivekadrakatti/Documents/2rdet5.jpg")
