import requests
import time

cc_number = 9
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

    def find_first_pair(k, liste):
        pairs = []
        for i1, m in enumerate(liste):
            for i2, n in enumerate(liste):
                if m + n == k:
                    pairs.append([i1, i2])
        distance_list = []
        for i in range(len(pairs)):
            # distance = (distance between indices, index in pairs)
            distance = (pairs[i][0] - pairs[i][1]).__abs__(), i
            distance_list.append(distance)
        distance_list = sorted(distance_list)
        return pairs[distance_list[0][1]]

    result = find_first_pair(k, liste)
    print(result)
    response2 = requests.post(url_output, json={'token': result})
    print('------------Response 2 of Server -------')
    print(response2.text)
    print('----------------------------------------')
    # Success: TMT{5umm3d17upr16h7d1dn7y4}


def benchmark(n):
    start = time.time()
    for i in range(n):
        solve()
    print((time.time() - start) / n)


benchmark(100)
