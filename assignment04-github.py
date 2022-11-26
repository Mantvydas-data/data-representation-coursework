#Importing required packages
import requests
from github import Github

#Importing key from internal file
from config import config as cfg
apik = cfg["githubk"]

#Key is used for Github access
g = Github(apik)

#Specifying private Github repo
repo = g.get_repo("Mantvydas-data/aprivateone")

#Checking repo for required file and getting it's URL
secretletter = repo.get_contents("letter.txt")
letterURL = secretletter.download_url

#File content is retrieved 
response = requests.get(letterURL)
contentoftheleter = response.text

#Replacing instances of name Andrew with Mantvydas
updatedletter = contentoftheleter.replace("Andrew","Mantvydas")

#Updated letter is pushed to Github
githubpush=repo.update_file(secretletter.path,"updated by prog",
updatedletter,secretletter.sha)