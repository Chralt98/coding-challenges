import requests
import time

cc_number = 10
url_input = 'https://cc.the-morpheus.de/challenges/' + str(cc_number) + '/'
url_output = 'https://cc.the-morpheus.de/solutions/' + str(cc_number) + '/'


def solve():
    response = requests.get(url_input).text
    print('------------ Response of Server --------')
    print(response)
    print('----------------------------------------')
    # TODO: programm your solution here
    result = float(response)
    response2 = requests.post(url_output, json={'token': result})
    print('------------Response 2 of Server -------')
    print(response2.text)
    print('----------------------------------------')
    # Success: TMT{WBVjoml6PjsOu3yzFvr3}


def benchmark(n):
    start = time.time()
    for i in range(n):
        solve()
    print((time.time() - start) / n)


benchmark(1)
