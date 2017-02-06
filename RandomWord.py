import requests

class RandomWord:

    base_url = "http://randomword.setgetgo.com"
    path = "/get.php"

    def get_random_word(self, length = 0):

        request_url = self.base_url+self.path
        if length > 0:
            request_url += "?len="+format(length)
        response = requests.get(request_url)

        if(response.status_code == 200):
            return response.text
        else:
            return False
