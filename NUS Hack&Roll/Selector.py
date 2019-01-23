import pandas as pd
from random import randint

memes = pd.read_csv('/Users/vivekadrakatti/Documents/NUS Hack&Roll/dataset.csv')
tag_list = memes['Tags'].tolist()
emotion_list = memes['Emotion'].tolist()
caption_list = memes['Text'].tolist()
# function to get meme text appropriately
def simple_function(picture_emotions,picture_tags):
    indexes_emotion=[]
    indexes_captions=[]
    for i in range(len(emotion_list)):
        if(abs(int(emotion_list[i])==int(picture_emotions))):
            indexes_emotion.append(i)
        elif picture_emotions!=0 and emotion_list[i]!=0:
            emotion_list[i]=str(emotion_list[i])
            picture_emotions=str(picture_emotions)
            for j in range(0,5):
                if (int(emotion_list[i][j])>=2 and int(picture_emotions[j])>=2):
                    indexes_emotion.append(i)
                    break
    for i in indexes_emotion:
        if(len(caption_list[i])>3):
            indexes_captions.append(i)
    final_index = []
    for i in indexes_captions:
        for j in picture_tags:
            if (j in str(tag_list[i])):
                final_index.append(i)
    majority=[0 for i in range(len(final_index))]
    k=-1
    for i in final_index:
        k+=1
        for j in picture_tags:
            if(j in tag_list[i]):
                majority[k]+=1
    index_M = []
    maximum = max(majority)
    for i in range(len(final_index)):
        if(majority[i]==maximum):
            index_M.append((final_index[i],majority[i]))
    rand_no = randint(0,len(index_M)-1)
    grand_finale = index_M[rand_no][0]
    return (caption_list[grand_finale])
