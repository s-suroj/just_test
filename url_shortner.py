#a url shortner written in python
import requests

print(requests.get("http://tinyurl.com/api-create.php?url="+input("Enter a url to shorten: ")).text)

