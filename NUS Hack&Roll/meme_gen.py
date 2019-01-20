import pandas as pd
from random import randint

def comparer_life(picture_emotions):
    memes = pd.read_csv('/Users/vivekadrakatti/Documents/NUS Hack&Roll/dataset.csv')

    tagList = memes['Tags'].tolist()
    emotionList = memes['Emotion'].tolist()
    captionList = memes['Text'].tolist()
    indexesEmotion=[]
    indexesCaptions=[]
    indexesTags=[]
    for i in range(len(emotionList)):
        if(abs(int(emotionList[i])-int(picture_emotions))==0):
            indexesEmotion.append(i)

        elif picture_emotions!=0 and emotionList[i]!=0:
            emotionList[i]=str(emotionList[i])
            picture_emotions=str(picture_emotions)
            for j in range(0,5):
                if (int(emotionList[i][j])>=2 and int(picture_emotions[j])>=2):
                    indexesEmotion.append(i)
                    break

    for i in indexesEmotion:
        if(len(captionList[i])>3):
            indexesCaptions.append(i)

    return indexesCaptions

def StringCompare(indexes,picture_tags):
    memes = pd.read_csv('/Users/vivekadrakatti/Documents/NUS Hack&Roll/dataset.csv')

    tagList = memes['Tags'].tolist()

    finalIndex = []

    for i in indexes:
        for j in picture_tags:
            if (j in str(tagList[i])):
                finalIndex.append(i)

    # print(len(finalIndex))
    # print(tagList[15])
    return finalIndex




def majority_match(finalIndex, picture_tags):
    memes = pd.read_csv('/Users/vivekadrakatti/Documents/NUS Hack&Roll/dataset.csv')
    max_index = []
    tagList = memes['Tags'].tolist()
    captionList = memes['Text'].tolist()
    majority=[0 for i in range(len(finalIndex))]
    k=-1
    for i in finalIndex:
        k+=1
        for j in picture_tags:
            if(j in tagList[i]):
                majority[k]+=1
    indexM = []
    maximum = max(majority)

    for i in range(len(finalIndex)):
        if(majority[i]==maximum):
            indexM.append((finalIndex[i],majority[i]))


    randNo = randint(0,len(indexM)-1)
    GrandFinale = indexM[randNo][0]
    return (captionList[GrandFinale])




def simpleFunction(picture_emotions,picture_tags):
    return majority_match(StringCompare(comparer_life(picture_emotions),picture_tags),picture_tags)
