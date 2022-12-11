import requests
from bs4 import BeautifulSoup
import re
url="https://ful.io/"
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)
soup =BeautifulSoup(htmlContent,'html.parser')

urls = []

for link in soup.find_all('a',{'href':re.compile("https://www.")}):
    print("social links-"+"\n"+link.get('href')+"\n")
    "\n"
print("Email-ssupport@ful.io"+"\n" +"Contact:+1 343 303 6668")

