import requests, json
from bs4 import BeautifulSoup

#need auth to see page 
url = "https://fantasy.espn.com/football/league/standings?seasonId=2019&leagueId=1721747"
data = requests.get(url)
# data = data.json()
# print(data.content)

soup = BeautifulSoup(data.content, 'html.parser') # If this line causes an error, run 'pip install html5lib' or install html5lib
print(soup.prettify())
