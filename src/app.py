from bs4 import BeautifulSoup
import requests

print("***Starting scraper***")

root = "http://ufcstats.com/"
url = "http://ufcstats.com/statistics/fighters"

result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")

# Find the table
table_body = doc.find('tbody')
# Find every table row
rows = table_body.find_all('tr')
# Loop over each table row
for row in rows:
    # Find every table column within a table row
    cols = row.find_all('td')
    # remove white space from text in each table column
    cols = [x.text.strip() for x in cols]
    # print results
    print(cols)