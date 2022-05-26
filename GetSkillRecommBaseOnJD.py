from pathlib import Path
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

# This method can extract and save job description to txt file from the given url.
def test_html_save(job_url, jd_path):
    browser = webdriver.Chrome()
    browser.get(job_url)
    time.sleep(4) #Waits for 4 secs until the page loads
    html_content = browser.page_source  # Getting the html from the webpage
    browser.close()
    soup = BeautifulSoup(html_content, 'html.parser') # creates a beautiful soup object 'soup'.

    jds = soup.find_all('li')

    with open(jd_path, 'wt', encoding='utf-8') as jd_file:
        for jd in jds:
            jd_file.write(jd.text + '\n')

def search_recommended_skill(skill_list, jd_path, skill_path):
    # Read all skills and save to a list from existed allSkills file
    df = pd.read_excel(skill_list, usecols='D')
    skills_list = df.values.tolist()

    with open(skill_path, 'wt', encoding='utf-8') as skill_file:
        skill_file.write('Recommended skills for this job:' + '\n')
        for skill in skills_list:
            with open(jd_path, 'r') as file:
                # read all content of a file
                content = file.read()
                # check if string present in a file
                if skill[0] in content:
                    print(skill[0] + ' is recommended')
                    skill_file.write(skill[0] + '\n')

# input the job description webpage here
jd_url = 'https://www.seek.com.au/job/56898038?type=standard#sol=4038512b16b3c7c94fe23ca8c06996a546765a60'
all_skills_list = 'C:\Project\Skillojo\jd\\allSkills.xlsx'
jds_save_path = "C:\Project\Skillojo\jd\jd.txt"
recommended_skills_path = "C:\Project\Skillojo\jd\\recommended_skills.txt"

# Scrape job description and save to txt file. This step can be skipped if job description is in txt format.
test_html_save(jd_url, jds_save_path)

# Produce recommended skills list based on given job description txt file.
search_recommended_skill(all_skills_list, jds_save_path, recommended_skills_path)

