import requests
import time

cc_number = 12
url_input = 'https://cc.the-morpheus.de/challenges/' + str(cc_number) + '/'
url_output = 'https://cc.the-morpheus.de/solutions/' + str(cc_number) + '/'


def solve():
    response = requests.get(url_input).json()
    print('------------ Response of Server --------')
    print(response)
    print('----------------------------------------')
    # TODO: programm your solution here
    k = response['k']
    liste = response['list']

    def min_length(k, liste):
        minimal = len(liste)
        for i in range(len(liste)):
            index_length, value = 0, 0
            for j in range(i, len(liste)):
                if value >= k:
                    if index_length < minimal:
                        minimal = index_length
                    break
                index_length += 1
                value += liste[j]
        return minimal

    result = min_length(k, liste)
    print(result)
    response2 = requests.post(url_output, json={'token': result})
    print('------------Response 2 of Server -------')
    print(response2.text)
    print('----------------------------------------')
    # Success: TMT{IeNdTke0JJONqwbel1HJ}


def benchmark(n):
    start = time.time()
    for i in range(n):
        solve()
    print((time.time() - start) / n)


benchmark(10)
