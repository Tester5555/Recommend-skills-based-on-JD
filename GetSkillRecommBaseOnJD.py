from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import os.path


# This method can extract and save job description to txt file from the given url.
def test_html_save(job_url, jd_path):
    browser = webdriver.Chrome()
    browser.get(job_url)
    time.sleep(4)
    html_content = browser.page_source  # Getting the html from the webpage
    browser.close()
    soup = BeautifulSoup(html_content, 'html.parser')  # creates a beautiful soup object 'soup'.

    jds = soup.find_all('li')

    with open(jd_path, 'wt', encoding='utf-8') as jd_file:
        for jd in jds:
            jd_file.write(jd.text + '\n')


def skills_file_to_list(skills_file):
    # Read all skills and save to a list from existed allSkills file
    extension = os.path.splitext(skills_file)[1]
    if extension == '.xlsx' or extension == '.xls':
        df = pd.read_excel(skills_file, usecols='D')
    elif extension == '.csv':
        df = pd.read_csv(skills_file)
        df.columns = ["Index", "SkillID", "url", "name", "type"]
    else:
        print('Skills file only support excel or csv format.')

    skills_list = list(df.name)
    return skills_list


def search_recommended_skill(skills_file, jd_path, recommend_skills_file):
    # Read all skills and save to a list from existed allSkills file
  #  df = pd.read_excel(skill_list, usecols='D')
  #  skills_list = df.values.tolist()
    skills_list = skills_file_to_list(skills_file)

    with open(recommend_skills_file, 'wt', encoding='utf-8'):
        recommend_skills_file.write('Recommended skills for this job:' + '\n')
        for skill in skills_list:
            
            with open(jd_path, 'r') as file:
                # read all content of a file
                content = file.read()
                # check if string present in a file
                if skill in content:
                    print(skill + ' is recommended')
                    recommend_skills_file.write(skill + '\n')


# input the job description webpage here
jd_url = 'https://www.seek.com.au/job/57088961?type=standout#sol=b8eb0692125198a860d2c23abae42da821ae67cb'
# The all skills list be matched.
all_skills_list = 'C:\Project\Skillojo\jd\\allSkills.csv'
# Job description will be converted to txt
jd = "C:\Project\Skillojo\jd\jd.txt"
# The recommended skills for this job will save in this txt file.
recommended_skills = "C:\Project\Skillojo\jd\\recommended_skills.txt"

# Scrape job description and save to txt file. This step can be skipped if job description is in txt format.
test_html_save(jd_url, jd)

# Produce recommended skills list based on given job description txt file.
search_recommended_skill(all_skills_list, jd, recommended_skills)

