import requests

from bs4 import BeautifulSoup

# headers needed to get 200 acceptance from website instead of 403
headers = {'User-Agent': 'Mozilla/5.0'}

msg_welcome = "Hello, welcome to the translator. Translator supports: "
languages = ['Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew', 'Japanese', 'Dutch', 'Polish',
             'Portuguese', 'Romanian', 'Russian', 'Turkish']
for ind, language in enumerate(languages, start=1):
    print(str(ind) + ".", language)

msg_home = "Type the number of your language: "
msg_foreign = "Type the number of language you want to translate to: "
msg_word = "Type the word you want to translate:"

print(msg_home)
home_language = int(input())
print(msg_foreign)
foreign_language = int(input())
print(msg_word)
word = input().lower()

home_language = languages[home_language - 1]
foreign_language = languages[foreign_language - 1]

# valid url to get data from
url = "https://context.reverso.net/translation/" + home_language.lower() + "-" + foreign_language.lower() + "/" + word

# using request module to connect with url
r = requests.get(url, headers=headers)
print(foreign_language + " Translations:")

# using BeautifulSoup module to get content from website
soup = BeautifulSoup(r.content, 'html.parser')
translations = list()
sentences = list()

# storing all span with the given class in variable spans
spans = soup.find_all('span', {'class': "display-term"})

# appending translations into list
for x in spans:
    translations.append(x.text)

for word in translations:
    print(word)

# appending content sentences into list
divs_examples = soup.find_all('div', {'class': ['src ltr', 'trg ltr']})
for x in divs_examples:
    sentences.append(x.text)

new_sentences = [item.strip() for item in sentences]
print()

print(foreign_language + " Examples:")
for example in new_sentences:
    print(example)
