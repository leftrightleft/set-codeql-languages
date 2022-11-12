import os
import requests
import json
import sys

token = sys.argv[0]
endpoint = sys.argv[1]
#  codeql_languages = json.loads(sys.argv[2])

print(endpoint, token, sys.argv[2])
# Connect to the languages API and return languages
def get_languages():
    headers = {'Authorization': 'Bearer ' + token, 'Accept': 'application/vnd.github.v3+json'}
    url = os.environ.get(endpoint)
    response = requests.get(url, headers=headers)
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


