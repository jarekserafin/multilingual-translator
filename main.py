import requests
from bs4 import BeautifulSoup
import time


def take_input():
    print(msg_home)
    home_language = int(input())
    print(msg_foreign)
    foreign_language = int(input())
    print(msg_word)
    word = input().lower()
    home_language = languages[home_language - 1]
    foreign_language = languages[foreign_language - 1]
    return home_language, foreign_language, word


def url_maker(lan_1, lan_2):
    return "https://context.reverso.net/translation/" + lan_1.lower() + "-" + lan_2.lower() + "/" + word


def get_content(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    spans = soup.find_all('span', {'class': "display-term"})
    new_translations = list()
    for x in spans:
        new_translations.append(x.text)
    divs_examples = soup.find_all('div', {'class': ['src ltr', 'trg ltr']})
    for x in divs_examples:
        examples.append(x.text)
    new_examples = [item.strip() for item in examples]
    return new_translations, new_examples


# headers needed to get 200 acceptance from website instead of 403
headers = {'User-Agent': 'Mozilla/5.0'}
translations = list()
examples = list()
msg_welcome = "Hello, welcome to the translator. Translator supports: "
msg_home = "Type the number of your language: "
msg_foreign = "Type the number of language you want to translate to: "
msg_word = "Type the word you want to translate:"
languages = ['Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew', 'Japanese', 'Dutch', 'Polish',
             'Portuguese', 'Romanian', 'Russian', 'Turkish']

print(msg_welcome)
for ind, language in enumerate(languages, start=1):
    print(str(ind) + ".", language)

home_language, foreign_language, word = take_input()
url = url_maker(home_language, foreign_language)

print(foreign_language + " Translations:")
print()
translations, examples = get_content(url)
for word in translations:
    print(word)

print()
print(foreign_language + " Examples:")
for i, example in enumerate(examples):
    if i % 2 == 0:
        print()
    print(example)
