#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 15:26:54 2020

@author: MengLuo
"""

import sys
import re


#read the vocabulary file, we have 5 vocabulary file. They are joy_vocabulary_list
#disgust_vocabulary_list, anger_vocabulary_list, fear_vocabulary_list,
#sadness_vocabulary_list. Then I use a dictionary to store them.
def read_file():
    
    dic = {}
    list_joy = []
    list_disgust = []
    list_anger = []
    list_fear = []
    list_sadness = []
    
    #open the vocabulary file
    fp_JOY = open("JOY.txt","r", encoding = 'UTF-8')
    fp_DISGUST = open("DISGUST.txt","r", encoding = 'UTF-8')
    fp_ANGER = open("ANGER.txt","r", encoding = 'UTF-8')
    fp_FEAR = open("FEAR.txt","r", encoding = 'UTF-8')
    fp_SADNESS = open("SADNESS.txt","r", encoding = 'UTF-8')
    
    #read them line by line
    for line in fp_JOY.readlines():
        if line != '':
            list_joy.append(line.strip())

 
    for line in fp_DISGUST.readlines():
        if line != '':
            list_disgust.append(line.strip())
        
    for line in fp_ANGER.readlines():
        if line != '':
            list_anger.append(line.strip())
         
    for line in fp_FEAR.readlines():
        if line != '':
            list_fear.append(line.strip())
            
    for line in fp_SADNESS.readlines():
        if line != '':
            list_sadness.append(line.strip())
            
    # put them into dictionary
    dic["joy"] = list_joy   
    dic["disgust"] = list_disgust 
    dic["anger"] = list_anger
    dic["fear"] = list_fear
    dic["sadness"] = list_sadness
    
    return dic

#read the input txt file. 
def read_content():
    content = ""
    while 1<2:
        file = input("Please input the txt file name: ")
        try:
            fp = open(file,"r")
            for line in fp.readlines():
                content = content + line 
            return content
        #if we can't find the input file, we print the error message 
        #and ask for input again.
        except:
            print("Error, input file not found")
            continue

# I made 2 dictionary for record the score of emotion. One is for each
# single sentence, and another one is for whole content. we decide the 
# sentence emotion first, then after go through all sentence, we get 
# the score of all sentences and find the highest score. the content 
# emotion will be the highest scores' emotion.
def main_work(dic,content):
    
    dic_emotion_sentence = {"Joy":0 , "Disgust":0 ,"Anger":0 ,"Fear":0 ,"Sadness":0,"Neutral":0 }
    
    nagetive =["not", "but", "won't"] 
    
    list_joy = dic["joy"]
    list_disgust = dic["disgust"]
    list_anger = dic["anger"]
    list_fear = dic["fear"]
    list_sadness = dic["sadness"]
    
    # use split to get each sentences.
    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', content)
    dic_emotion = {"score_joy":0 , "score_disgust":0 ,"score_anger":0 ,"score_fear":0 ,"score_sadness":0 }
    
    #get each sentences
    for sentence in sentences:
        x = 0
        lst = list(sentence)
        
        #I elimilate all punctuation in the sentence.
        while x <len(sentence):            
            if lst[x] in '!,.?":;0123456789':
                lst[x] = ' '
            x+=1
        sentence = ''.join(lst)
        
        # we have a nag tag, which is used for deciding if the meaning is 
        # reversed.
        nag = False
        
        #we split the sentence to each word.
        sentence = sentence.split(' ')
        
        #for each word in sentence, when we found a word and it's in our 
        #vocabulary list. I will add 1 which means this emotion has one
        #point. In the end, the emotion with highest score will be the emotion
        #of this SENTENCE.
        for word in sentence:
            if word in list_joy:
                dic_emotion["score_joy"] += 1
            if word in list_disgust:
                dic_emotion["score_disgust"] += 1
            if word in list_anger:
                dic_emotion["score_anger"] += 1
            if word in list_fear:
                dic_emotion["score_fear"] += 1
            if word in list_sadness:
                dic_emotion["score_sadness"] += 1
            #if we found any word like not and but, the nagetive tag will be true
            if word in nagetive:
                nag = True
        
        #we get the emotion with highest score.
        emotion = sorted(dic_emotion,key=lambda x:dic_emotion[x])[-1]
        
        #If the nagetive tag is true, the meaning will be reversed.
        if nag == True and emotion.strip() == "score_joy":
            dic_emotion_sentence["Sadness"] +=1
        if nag == True and emotion.strip() == "score_sadness":
            dic_emotion_sentence["Joy"] +=1
        if nag == True and emotion.strip() == "score_disgust":
            dic_emotion_sentence["Neutral"]+=1
        if nag == True and emotion.strip() == "score_anger":
            dic_emotion_sentence["Neutral"]+=1
        if nag == True and emotion.strip() == "score_fear":
            dic_emotion_sentence["Neutral"]+=1
    
    #after go through all sentence, get the highest scores' emotion.
    final_emotion = sorted(dic_emotion_sentence,key=lambda x:dic_emotion_sentence[x])[-1]

    return final_emotion
            
        
def main():
    dic = read_file()
    content = read_content()
    emotion = main_work(dic,content)
    print(emotion)
if __name__ == "__main__":    
    main()