import jsonpath
import requests


def test_OAuth():

    #get Token through below request(to get token we have to provide- grant type, Username, Password)
    request_data = {'grant_type':'test','Username':'admin','Password':'admin'}
    res = requests.get("https://thetestingworldapi.com/Token", request_data)
    token = jsonpath.jsonpath(res.json(),'access_Token')
    token = token[0]
    print(res.text)

    #use token as header in this request
    header_data ={'Authorization':'Bearer '+token}
    res = requests.get("https://thetestingworldapi.com/api/StDetails/1104", headers=header_data)
    print(res.text)