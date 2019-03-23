import requests

result = requests.get('https://cc.the-morpheus.de/challenges/1/').text
print('------------ Response of Server --------')
print(result)
print('----------------------------------------')
response = requests.post('https://cc.the-morpheus.de/solutions/1/', json={'token': result})
print('------------2Response of Server --------')
print(response.text)
print('----------------------------------------')
# Success: TMT{WBVjoml6PjsOu3yzFvr3}
