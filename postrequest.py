import requests

"""
The client POST to check if some number is a prime
@author Christopher Altmann as Chralt
"""
# url with port 1337 on local server and the path prim
url = 'http://localhost:1337/prime'
print(requests.get(url).json())
# infinite repeat
while 1:
    # user input of wished number
    number = input('Enter your possible prime number: ')
    # request to the Flask server with required JSON format
    result = requests.post(url, json={"possible_prime": number})
    print('Response of the server: ')
    print('------------------------')
    # result of the server
    print(result.json())
    print('------------------------')
