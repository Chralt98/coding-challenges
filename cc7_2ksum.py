import requests
import time

cc_number = 7
url_input = 'https://cc.the-morpheus.de/challenges/' + str(cc_number) + '/'
url_output = 'https://cc.the-morpheus.de/solutions/' + str(cc_number) + '/'

start = time.time()
for i in range(100):
    response = requests.get(url_input).json()
    k = response['k']
    liste = response['list']


    def find_first_pair(k, liste):
        for i1, m in enumerate(liste):
            for i2, n in enumerate(liste):
                if m + n == k:
                    return [i1, i2]


    for l in range(len(liste)):
        for j in range(len(liste)):
            if liste[l] + liste[j] == k:
                result = [l, j]
                break

    for l in liste:
        for j in liste:
            if l + j == k:
                result2 = [liste.index(l), liste.index(j)]
                break

    print("morpheus: " + str(result) + " ,me: " + str(find_first_pair(k, liste)) + ", morpheus 2st: " + str(result2))
    # result = find_first_pair(k, liste)
    response2 = requests.post(url_output, json={'token': find_first_pair(k, liste)})
    print(response2.text)
    # Success: TMT{izRWIGQW5BsTv5R0JogU}
print((time.time() - start)/100)
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
