import requests
from requests.auth import HTTPBasicAuth

def test_basicAuth():
    res = requests.get("https://api.github.com/user", auth=HTTPBasicAuth('mrubarapatre198@gmail.com', 'Elsa@408408'))
    print(res.text)


