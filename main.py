import os
import requests
import json
import sys

token = sys.argv[1]
endpoint = sys.argv[2]
codeql_languages = ["cpp", "csharp", "go", "java", "javascript", "python", "ruby"]

# Connect to the languages API and return languages
def get_languages():
    headers = {'Authorization': 'Bearer ' + token, 'Accept': 'application/vnd.github.v3+json'}
    response = requests.get(endpoint, headers=headers)
    return response.json()

def build_languages_list(languages):
    languages = [language.lower() for language in languages.keys()]
    for i in range(len(languages)):
        if languages[i] == "c#":
            languages[i] = ("csharp")
        if languages[i] == "c++":
            languages[i] = ("cpp")

    intersection = list(set(languages) & set(codeql_languages))
    return intersection

def main():
    languages = get_languages()
    return build_languages_list(languages)

if __name__ == '__main__':
    main()


