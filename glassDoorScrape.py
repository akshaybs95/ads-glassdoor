import AdityaLib as ADL
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
import time


def Scrapedata():
    driver = ADL.open_web('https://www.glassdoor.co.in/Job/united-states-usa-jobs-SRCH_IL.0,13_IN1_KO14,17.htm')
    soup = bs(driver.page_source, features="html.parser")

    listings = soup.find_all("li", attrs={"class":"JobsList_jobListItem__wjTHv"})
    driver.find_element(By.XPATH,'//*[@id="left-column"]/div[2]/div/button').click()
    time.sleep(5)
    try:
        driver.find_element(By.XPATH,"/html/body/div[11]/div[2]/div[2]/div[1]/button").click()
    except:
        pass
    data = []
    for i in range(1,61):
        driver.find_element(By.XPATH,'//*[@id="left-column"]/div[2]/ul/li['+str(i)+']').click()
        time.sleep(2)

        header = driver.find_element(By.XPATH,'//*[@id="app-navigation"]/div[3]/div[2]/div[2]/div/div[1]/header').text
        
        details = header.split("\n")
        if len(header.split("\n")) == 4:
            company = details[0]
            JobTitle = details[1]
            location = details[2]
        if len(header.split("\n")) == 5:
            company = details[0]
            JobTitle = details[2]
            location = details[3]

        try:
            driver.find_element(By.XPATH,'//*[@id="app-navigation"]/div[3]/div[2]/div[2]/div/div[1]/section/div[2]/div[2]/button').click()
        except Exception as e:
            # print(str(e))
            pass
        time.sleep(2)
        desc =  driver.find_element(By.XPATH,'//*[@id="app-navigation"]/div[3]/div[2]/div[2]/div/div[1]/section/div[2]/div[1]').text

        data.append([company, JobTitle, location,desc])    
    
    ADL.Save_to_File("OutFile.csv",["Company","Job Title","Location","job Description"],data, True,False)
    pass

def Main():
    Scrapedata()

if __name__ ==  '__main__':
    Main()