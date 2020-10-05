#!/usr/bin/python3 

import requests
import os
import datetime
import json

header={'User-agent':'my bot 0.1'}

r = requests.get('https://api.reddit.com/r/sexstories',headers=header)
print("Reaching home !!!")

data=r.json()
newData=data['data']['children']



#function for creating files
def createFiles(path,newtitle,title,body):
	
	f = open(path+"/"+newtitle+".txt", "w",encoding="utf-8")
	f.write("\t\t\t\t\t\t\t\t\t\t"+title+"\n\n")
	f.write(body)
	f.close()
	print("Eggs fertilized Successfully !!! \n\n")

for story in newData:
	print("Checking out the Body !!!")

	title=story['data']['title']
	newtitle=title.replace(" ","_")[:25]
	charsToReplace={'\'':'','-':"","\"":"","[":"","]":"","/":"_"}
	for key, value in charsToReplace.items():
		newtitle=newtitle.replace(key,value) #Make Title without ' or - 

	link=story['data']['permalink']
	gotolink=requests.get('https://api.reddit.com/'+link,headers=header)
	print("Opening Clothes !!!")

	individualData=gotolink.json()
	
	#Saving file to json
	# with open('output.json', 'a') as json_file:
	# 	json.dump(individualData, json_file)

	body=individualData[0]['data']['children'][0]['data']['selftext']


	#Get tag Flair
	print("Performing foreplay !!!!")

	tag=individualData[0]['data']['children'][0]['data']['link_flair_text']
	if tag is None:
		tag="None"
	else:	
		tag=individualData[0]['data']['children'][0]['data']['link_flair_text'].split()[0]
	
	print("Watching time !!!")
	Date=datetime.datetime.now()
	dirName=str(Date.year)+"_"+str(Date.month)+"_"+str(Date.day)

	workingDir=os.getcwd() #/home/kali/Desktop/project
	fullpath=workingDir+"/"+dirName+"/"+tag

	if(os.path.isdir(dirName)):
		if(os.path.isdir(fullpath)):
			createFiles(fullpath,newtitle,title,body)
		else:
			tag=dirName+"/"+tag
			os.mkdir(tag)
			createFiles(fullpath,newtitle,title,body)

				
	else:
		os.makedirs(dirName+"/"+tag)
		createFiles(fullpath,newtitle,title,body)