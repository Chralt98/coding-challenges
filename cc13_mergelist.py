import requests
import time

cc_number = 13
url_input = 'https://cc.the-morpheus.de/challenges/' + str(cc_number) + '/'
url_output = 'https://cc.the-morpheus.de/solutions/' + str(cc_number) + '/'


def solve():
    response = requests.get(url_input).json()
    print('------------ Response of Server --------')
    print(response)
    print('----------------------------------------')
    # TODO: programm your solution here
    # [1,5,8,16,34]
    lista = list(response['lista'])
    # [2,7,16,27,37]
    listb = list(response['listb'])
    # [1,2,5,7,8,16,27,34,37]
    result = sorted(lista + listb)
    response2 = requests.post(url_output, json={'token': result})
    print('------------Response 2 of Server -------')
    print(response2.text)
    print('----------------------------------------')
    # Success, TMT{N4aEMLcN3PaTbEZih9Qz}


def benchmark(n):
    start = time.time()
    for i in range(n):
        solve()
    print((time.time() - start) / n)


benchmark(1)
