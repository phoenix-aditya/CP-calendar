import requests
import json


def codeforcesdata(username):
    url="https://codeforces.com/api/user.info?handles="+str(username)+";"
    usrdata=requests.get(url).json()
    
    my_dict={"username": username}

    for i in usrdata['result']:
        name=str(i['firstName']+" "+i['lastName'])
        my_dict["name"]=name
        my_dict["rating"]=i['rating']
        my_dict["maxrating"]=i['maxRating']
        my_dict["rank"]=i['rank']
        my_dict["maxrank"]=i['maxRank']
        my_dict["organization"]=i['organization']
    
    return my_dict




if __name__=="__main__":
    print(codeforcesdata("phoenix_aditya"))
