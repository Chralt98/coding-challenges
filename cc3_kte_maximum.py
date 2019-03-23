import requests

cc_number = 3
url_input = 'https://cc.the-morpheus.de/challenges/' + str(cc_number) + '/'
url_output = 'https://cc.the-morpheus.de/solutions/' + str(cc_number) + '/'

response = requests.get(url_input).json()
print('------------ Response of Server --------')
print(response)
print('----------------------------------------')
liste = sorted(list(response['list']), reverse=True)
print(liste)
k = response['k']
print(k)
k_max = liste[k-1]
print(k_max)
response2 = requests.post(url_output, json={'token': k_max})
print('------------Response 2 of Server -------')
print(response2.text)
print('----------------------------------------')
# Success: TMT{S0SpkHzubAmCu7H3r5wR}

"""
import time
start = time.time()
for i in range(100):
    pass
print((time.time() - start)/100)

result = ''
response2 = requests.post(url_output, json={'token': result})
print('------------Response 2 of Server -------')
print(response2.text)
print('----------------------------------------')
# Success: TMT{WBVjoml6PjsOu3yzFvr3}
"""
