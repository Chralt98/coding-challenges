import requests
import time

cc_number = 8
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
                for i3, o in enumerate(liste):
                    for i4, p in enumerate(liste):
                        if m + n + o + p == k:
                            return [i1, i2, i3, i4]

    print("Result: " + str(find_first_pair(k, liste)))
    result = find_first_pair(k, liste)
    response2 = requests.post(url_output, json={'token': result})
    print(response2.text)
    # Success: TMT{HAwxLryQhiLh3eGh0pbx}
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
