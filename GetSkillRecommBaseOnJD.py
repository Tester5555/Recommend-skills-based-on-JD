from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import os.path
import pypandoc


# This method can extract and save job description to txt file from the given url.
def jd_convert(jd_input, jd_output):
    pypandoc.convert_file(jd_input, 'plain', outputfile=jd_output)


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
    skills_list = skills_file_to_list(skills_file)

    with open(recommend_skills_file, 'wt', encoding='utf-8') as rec_file:
        rec_file.write('Recommended skills for this job:' + '\n')
        for skill in skills_list:
            
            with open(jd_path, 'r') as file:
                # read all content of a file
                content = file.read()
                # check if string present in a file
                if skill in content:
                    print(skill + ' is recommended')
                    rec_file.write(skill + '\n')


# Job description docx file or webpage.
#jd = 'https://www.seek.com.au/job/57119141?type=standout#sol=971afa04a55e6fb0f1f744f6957ffc8d8e313295.html'
jd = 'C:\Project\Skillojo\jd\Test Analyst.docx'

# The all skills list be matched.
all_skills_list = 'C:\Project\Skillojo\jd\\allSkills.csv'
# Job description will be converted to txt
jd_txt = "C:\Project\Skillojo\jd\jd.txt"
# The recommended skills for this job will save in this txt file.
recommended_skills = "C:\Project\Skillojo\jd\\recommended_skills.txt"

# Scrape job description and save to txt file. This step can be skipped if job description is in txt format.
jd_convert(jd, jd_txt)

# Produce recommended skills list based on given job description txt file.
search_recommended_skill(all_skills_list, jd_txt, recommended_skills)

