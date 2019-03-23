import requests

cc_number = 4
url_input = 'https://cc.the-morpheus.de/challenges/' + str(cc_number) + '/'
url_output = 'https://cc.the-morpheus.de/solutions/' + str(cc_number) + '/'


# [1,2,3,4,5,6] one time rotation -> [6,1,2,3,4,5]
def rotate(liste2, n):
    for i in range(n):
        last_element = liste2.pop()
        liste2.insert(0, last_element)
    return liste2


response = requests.get(url_input).json()
print('------------ Response of Server --------')
print(response)
print('----------------------------------------')
liste = list(response['list'])
k = response['k']
k = k % len(liste)
result = rotate(liste, k)
response2 = requests.post(url_output, json={'token': result})
print('------------Response 2 of Server -------')
print(response2.text)
print('----------------------------------------')
# Success: TMT{ckcagjB0E9fPjW2p6gxz}
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
