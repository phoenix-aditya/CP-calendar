import requests
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

def codeforcesdata(username):
    url="https://codeforces.com/api/user.info?handles="+str(username)+";"
    usrdata=requests.get(url).json()
    
    my_dict={"username": username}

    for i in usrdata['result']:
        #name=str(i['firstName']+" "+i['lastName'])
        #my_dict["name"]=name
        my_dict["rating"]=i['rating']
        my_dict["maxrating"]=i['maxRating']
        my_dict["rank"]=i['rank']
        my_dict["maxrank"]=i['maxRank']
        my_dict["organization"]=i['organization']
    
    return my_dict

def codechefdata(username):
    chrome_options=Options()
    chrome_options.add_argument("--headless")
    driver=webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    url="https://www.codechef.com/users/"+str(username)
    driver.get(url)

    my_dict={"username":username}
    
    #getting rating
    rating = driver.find_element_by_xpath("/html/body/main/div/div/div/aside/div[1]/div/div[1]/div[1]").text
    my_dict.update({"rating":rating})
    
    #get highest rating
    highestrating=driver.find_element_by_xpath("/html/body/main/div/div/div/aside/div[1]/div/div[1]/small").text
    highestrating=highestrating[16:20]
    my_dict.update({"highest_rating":highestrating})

    #get global rank
    globalrank=driver.find_element_by_xpath("/html/body/main/div/div/div/aside/div[1]/div/div[2]/ul/li[1]/a/strong").text
    my_dict.update({"global_rank":globalrank})

    #get country rank
    countryrank=driver.find_element_by_xpath("/html/body/main/div/div/div/aside/div[1]/div/div[2]/ul/li[2]/a/strong").text
    my_dict.update({"counntryrank":countryrank})

    #long challenge rating
    longrating=driver.find_element_by_xpath("//*[@id='hp-sidebar-blurbRating']/div/table/tbody/tr[1]/td[2]").text
    my_dict.update({"longrating":longrating})

    #cookoff rating
    cookrating=driver.find_element_by_xpath("//*[@id='hp-sidebar-blurbRating']/div/table/tbody/tr[2]/td[2]").text
    my_dict.update({"cookrating": cookrating})

    #lunchtimerating
    lunchrating=driver.find_element_by_xpath("//*[@id='hp-sidebar-blurbRating']/div/table/tbody/tr[3]/td[2]").text
    my_dict.update({"lunchrating":lunchrating})

    driver.close()
    return my_dict

def atcoderdata(username):
    chrome_options=Options()
    chrome_options.add_argument("--headless")
    driver=webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    #driver=webdriver.Chrome(ChromeDriverManager().install())
    url="https://atcoder.jp/users/"+str(username)
    driver.get(url)

    my_dict={"status":"success"}

    my_dict.update({"username": username})

    rank=driver.find_element_by_xpath("//*[@id='main-container']/div[1]/div[3]/table/tbody/tr[1]/td").text
    my_dict.update({"rank":rank})

    rating=driver.find_element_by_xpath("//*[@id='main-container']/div[1]/div[3]/table/tbody/tr[2]/td/span").text
    my_dict.update({"rating":rating})

    highestrating=driver.find_element_by_xpath("//*[@id='main-container']/div[1]/div[3]/table/tbody/tr[3]/td/span[1]").text
    my_dict.update({"highestrating":highestrating})

    driver.close()

    return my_dict










if __name__=="__main__":
    #print(codeforcesdata("parvg555"))
    #print(codechefdata("parvg555"))
    print(atcoderdata("tourist"))

