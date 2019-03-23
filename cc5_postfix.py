import requests

cc_number = 5
url_input = 'https://cc.the-morpheus.de/challenges/' + str(cc_number) + '/'
url_output = 'https://cc.the-morpheus.de/solutions/' + str(cc_number) + '/'


def is_number(element):
    try:
        int(element)
    except ValueError:
        return False
    return True


def calculate(first_number, second_number, operator):
    first_number = float(first_number)
    second_number = float(second_number)
    result = 0
    if operator is '+':
        result = first_number + second_number
    elif operator is '-':
        result = first_number - second_number
    elif operator is '*':
        result = first_number * second_number
    elif operator is '/':
        result = first_number / second_number
    return result


def recursive_postfix(liste):
    liste = list(liste)
    if len(liste) == 1:
        return liste[0]
    for i in range(len(liste)):
        if not is_number(liste[i]):
            result = calculate(liste.pop(i-2), liste.pop(i-2), liste.pop(i-2))
            liste.insert(i-2, result)
            return recursive_postfix(liste)


response = requests.get(url_input).text
print('------------ Response of Server --------')
print(response)
#  1 2 3 / * 4 5 * +
#  1 * (2/3) + (4*5) = 2/3 * 20 = 40/3
print('----------------------------------------')
array = response.split(' ')
print(array)
result2 = int(recursive_postfix(array))
print(result2)
response2 = requests.post(url_output, json={'token': result2})
print('------------Response 2 of Server -------')
print(response2.text)
print('----------------------------------------')
# Success: TMT{cLVgwaS4j3JJorwe1GCw}
"""
import time
start = time.time()
for i in range(100):
    pass
print((time.time() - start)/100)

result = ''
response2 = requests.post(url_output, json={'token': int(result)})
print('------------Response 2 of Server -------')
print(response2.text)
print('----------------------------------------')
# Success: TMT{WBVjoml6PjsOu3yzFvr3}
"""
