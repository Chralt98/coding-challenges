import requests

cc_number = 6
url_input = 'https://cc.the-morpheus.de/challenges/' + str(cc_number) + '/'
url_output = 'https://cc.the-morpheus.de/solutions/' + str(cc_number) + '/'


def recursive_decimal2binary(decimal, binaries=None):
    if binaries is None:
        binaries = []
    binary = int(decimal % 2)
    if binary is 1:
        decimal = decimal - 1
    binaries.append(binary)
    if decimal == 0:
        binaries.reverse()
        solution = ''.join(str(e) for e in binaries)
        return solution
    return recursive_decimal2binary(decimal // 2, binaries)


response = int(requests.get(url_input).text)
print('------------ Response of Server --------')
print(response)
print('----------------------------------------')
result = recursive_decimal2binary(response)
print(result)
response2 = requests.post(url_output, json={'token': result})
print('------------Response 2 of Server -------')
print(response2.text)
print('----------------------------------------')
# Success: TMT{O6gjviTFP0f1Uv25chkI}
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
