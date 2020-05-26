import requests
from bs4 import BeautifulSoup
import pprint

get = requests.get('https://news.ycombinator.com/news')
# parse the string into proper HTML format
soup = BeautifulSoup(get.text, 'html.parser')
# graped the story link
links = soup.select('.storylink')  # used css selector to access data from the HTML file. .(dot) is a class
subtext = soup.select('.subtext')  # graped the id
hn = []

def sort_stories_by_votes(list):
    return sorted(list, key= lambda x : x['Points'], reverse=True)

def create_custom_hn(links, subtext):
    for idx, item in enumerate(links):
        text = item.getText()
        link = item.get('href')
        votes = subtext[idx].select('.score')
        if len(votes):
            point = int(votes[0].getText().replace(' points', " "))
            if point >= 100:
                hn.append({'Headline': text, 'link': link, 'Points': point})
        # the output was in form of 123 points. so we have replace points with a empty string and converted it to integer

    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(links, subtext))
#create_custom_hn(links, subtext)
