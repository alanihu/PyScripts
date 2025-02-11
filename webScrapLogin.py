import requests
from bs4 import BeautifulSoup 

#This URL will be the URL that your login form points to with the "action" tag.
POST_LOGIN_URL = 'https://freecycle.org/login'

#This URL is the page you actually want to pull down with requests.
REQUEST_URL = 'https://freecycle.org/home/dashboard'


#username-input-name is the "name" tag associated with the username input field of the login form.
#password-input-name is the "name" tag associated with the password input field of the login form.
payload = {
    'user': 'alan1687',
	'password': '1987Freecycle_1606'  #Preferably set your password in an env variable and sub it in.
}

with requests.Session() as session:
    post = session.post(POST_LOGIN_URL, data=payload)
    r = session.get(REQUEST_URL)
soup = BeautifulSoup(r.text)

print(soup.prettify())   #or whatever else you want to do with the request data!