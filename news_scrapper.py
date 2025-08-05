import requests
from bs4 import BeautifulSoup

URL = "https://www.aljazeera.com/news/" #fetch
response = requests.get(URL)

if response.status_code == 200: #parse
    soup = BeautifulSoup(response.text, "html.parser")

    headlines = soup.find_all("h3")

    with open("headlines.txt", "w", encoding="utf-8") as file: #save
        for i, headline in enumerate(headlines, 1):
            title = headline.get_text(strip=True)
            file.write(f"{i}. {title}\n")
    
    print("Headlines successfully saved to headlines.txt")
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
