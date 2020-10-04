#!/usr/bin/python3 

import requests
import os
import datetime
import json

header={'User-agent':'my bot 0.1'}

r = requests.get('https://api.reddit.com/r/sexstories',headers=header)

data=r.json()
newData=data['data']['children']



#function for creating files
def createFiles(path,newtiile,title,body):
	
	f = open(path+"/"+newtitle, "w")
	f.write("\t\t\t\t\t\t\t\t\t\t"+title+"\n\n")
	f.write(body)
	f.close()

for story in newData:
	title=story['data']['title']
	newtitle=title.replace(" ","_")[:25] #Make Title without any space
	link=story['data']['permalink']
	gotolink=requests.get('https://api.reddit.com/'+link,headers=header)

	individualData=gotolink.json()
	#Saving file to json
	with open('output.json', 'a') as json_file:
		json.dump(individualData, json_file)

	body=individualData[0]['data']['children'][0]['data']['selftext']

	#Get tag Flair
	tag=individualData[0]['data']['children'][0]['data']['link_flair_text']
	if tag is None:
		tag="None"
	else:	
		tag=individualData[0]['data']['children'][0]['data']['link_flair_text'].split()[0]
	Date=datetime.datetime.now()
	dirName=str(Date.year)+"_"+str(Date.month)+"_"+str(Date.day)

	workingDir=os.getcwd() #/home/kaliDesktop/project
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