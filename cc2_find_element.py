import requests
import time

cc_number = 2
url_input = 'https://cc.the-morpheus.de/challenges/' + str(cc_number) + '/'
url_output = 'https://cc.the-morpheus.de/solutions/' + str(cc_number) + '/'


def find_element_unsorted():
    start = time.time()
    for i in range(100):
        response = requests.get(url_input).json()
        """
        print('------------ Response of Server --------')
        print(response)
        print('----------------------------------------')
        """
        element = response['k']
        liste = list(response['list'])
        result = liste.index(element)
        response2 = requests.post(url_output, json={'token': result})
        """
        print('------------Response 2 of Server -------')
        print(response2.text)
        print('----------------------------------------')
        """
        # Success: TMT{AlwiUi8lp8du3iFTs8kc}
    print((time.time() - start)/100)


def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]


def recursive_compare(liste, element2):
    if len(liste) == 1:
        return liste[0][0]
    first_half, second_half = split_list(liste)
    if element2 < second_half[0][1]:
        return recursive_compare(first_half, element2)
    elif element2 > second_half[0][1]:
        return recursive_compare(second_half, element2)
    else:
        # (6, 128919831893)
        return second_half[0][0]


def find_element_sorted():
    url_input2 = 'https://cc.the-morpheus.de/challenges/2/sorted/'
    url_output2 = 'https://cc.the-morpheus.de/solutions/2/'
    response = requests.get(url_input2).json()
    print('------------ Response of Server --------')
    print(response)
    print('----------------------------------------')

    element = response['k']
    liste = list(response['list'])
    tuple_list = []
    for i in range(len(liste)):
        tuple_list.append((i, liste[i]))
    result2 = recursive_compare(tuple_list, element)
    print(result2)
    response2 = requests.post(url_output2, json={'token': result2})
    print(response2.text)
    # Success: TMT{WBVjoml6PjsOu3yzFvr3}


# start = time.time()
# for i in range(500):
find_element_sorted()
# print((time.time() - start)/500)
# find_element_unsorted()
