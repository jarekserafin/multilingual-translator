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
    if foreign_language != 0:
        foreign_language = languages[foreign_language - 1]
    return home_language, foreign_language, word


def url_maker(lan_1, lan_2):
    return "https://context.reverso.net/translation/" + lan_1.lower() + "-" + lan_2.lower() + "/" + word


def get_translations(url):
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


def get_translations_for_all(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    spans = soup.find('span', {'class': "display-term"})
    new_translations = list()
    examples = list()
    for x in spans:
        new_translations.append(x.text)
    translation = new_translations[0]
    divs_examples = soup.find_all('div', {'class': ['src ltr', 'trg ltr']}, limit=2)
    for i, x in enumerate(divs_examples):
        examples.append(x.text)
    new_examples = [item.strip() for item in examples]
    return translation, new_examples


# def beginning_to_file(file):
#     file.write(msg_welcome + "\n")
#     for ind, language in enumerate(languages, start=1):
#         file.write(str(ind) + "." + language + "\n")
#     file.write(msg_home + "\n")
#     file.write(msg_foreign + "\n")
#     file.write(msg_word + "\n")


# headers needed to get 200 acceptance from website instead of 403
headers = {'User-Agent': 'Mozilla/5.0'}
translations = list()
examples = list()
msg_welcome = "Hello, welcome to the translator. Translator supports: "
msg_home = "Type the number of your language: "
msg_foreign = "Type the number of a language you want to translate to or '0' to translate to all languages: "
msg_word = "Type the word you want to translate:"
languages = ['Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew', 'Japanese', 'Dutch', 'Polish',
             'Portuguese', 'Romanian', 'Russian', 'Turkish']


print(msg_welcome)
for ind, language in enumerate(languages, start=1):
    print(str(ind) + ".", language)

home_language, foreign_language, word = take_input()
file_path = word + ".txt"
with open(file_path, 'w') as file:

    # beginning_to_file(file)
    if foreign_language != 0:
        url = url_maker(home_language, foreign_language)
        translations, examples = get_translations(url)
        print(foreign_language + " Translations:")
        file.write(foreign_language + " Translations:\n")
        print()
        file.write("\n")
        for word in translations:
            print(word)
            file.write(word + "\n")
        print()
        file.write("\n")
        print(foreign_language + " Examples:")
        file.write(foreign_language + " Examples:\n")
        for i, example in enumerate(examples):
            if i % 2 == 0:
                print()
                file.write("\n")
            print(example)
            file.write(example + "\n")
    else:
        for ind, foreign_language in enumerate(languages, start=1):
            if foreign_language == home_language:
                continue
            url = url_maker(home_language, foreign_language)
            translation, examples = get_translations_for_all(url)

            print(foreign_language + " Translations:")
            file.write(foreign_language + " Translations:\n")
            print(translation)
            file.write(translation + "\n")
            print()
            file.write("\n")
            print(foreign_language + " Examples:")
            file.write(foreign_language + " Examples:\n")
            for example in examples:
                print(example)
                file.write(example + "\n")
            print()
            file.write("\n")
