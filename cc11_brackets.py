import requests
import time

cc_number = 11
url_input = 'https://cc.the-morpheus.de/challenges/' + str(cc_number) + '/'
url_output = 'https://cc.the-morpheus.de/solutions/' + str(cc_number) + '/'


def solve():
    response = requests.get(url_input).text
    print('------------ Response of Server --------')
    print(response)
    print('----------------------------------------')
    # TODO: programm your solution here

    def is_bracket(term):
        term = list(term)
        brackets = []
        for i in range(len(term)):
            if term[i] == ')' and not brackets:
                return False
            if term[i] == '(':
                brackets.append('(')
            elif term[i] == ')':
                brackets.append(')')
        print(brackets)
        if len(brackets) == 1:
            return False
        while brackets:
            if brackets[0] == '(' and brackets[-1] == ')':
                brackets.remove(brackets[-1])
                brackets.remove(brackets[0])
            else:
                return False
        return True

    def is_bracket2(term):
        opened = 0
        for i in term:
            if i == '(':
                opened += 1
            elif i == ')':
                opened -= 1
            if opened < 0:
                return False
        if opened != 0:
            return False
        return True

    result = is_bracket2(response)
    print(result)
    result = is_bracket(response)
    print(result)
    response2 = requests.post(url_output, json={'token': result})
    print('------------Response 2 of Server -------')
    print(response2.text)
    print('----------------------------------------')
    # Success: TMT{t2VdCXazxCHu11K37BeS}


def benchmark(n):
    start = time.time()
    for i in range(n):
        solve()
    print((time.time() - start) / n)


benchmark(100)
