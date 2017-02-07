import requests
import json

class Dictionary:

    base_url = "https://od-api.oxforddictionaries.com/api/v1"
    api_key = "08fd7afa98b06c609aae9e5fbb70741a"
    app_id = "b6797cf9"
    language = "en"

    def get_word_info(self, word):

        action = "/entries/"+self.language+"/"+word.lower()+"/definitions"
        url = self.base_url+action

        r = requests.get(url, headers={'app_id': self.app_id, 'app_key': self.api_key})

        if(r.status_code == 200):
            return r.json()
        else:
            return False

    def get_word_definition(self, json, word):

        definitions = list()

        try:
            results = json["results"][0]
            entries = results["lexicalEntries"]

            for entry in entries:
                entry = entry["entries"][0]["senses"]
                for definition in entry:
                    definition = definition['definitions'][0]
                    definition = definition.replace(word,"<WORD>")
                    definitions.append(definition)
        except:
            print("Could not load hints (definitions)")

        return definitions