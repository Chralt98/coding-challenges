from flask import Flask, jsonify, request
import json

"""
A Flask microservice to handle POST JSON request 
with key 'possible_prime' to response 
if this value is a prime number 
returns JSON with key is_prime and value True or False
@author Christopher Altmann as Chralt
"""

# flask app is initialized
app = Flask(__name__)


# check if the integer is prime
def is_prime(n):
    # the first prime numbers are 2,3,5,7,11...
    if n < 2:
        return False
    # check if this number divides only by itself and 1
    for i in range(3, n):
        # if there is another number that divides the pasted number -> no prime number
        if n % i == 0:
            return False
    # if every number is tested except one and the number then it is prime
    return True


@app.route('/prime', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # use json to handle it like json and not like a normal string
        posted_json = json.loads(request.data.decode('utf-8'))
        try:
            # use the key 'possible_prime' to get the value number
            number = int(posted_json['possible_prime'])
        except ValueError:
            # if the value is no number response an error
            return jsonify(not_a_number=posted_json['possible_prime'], description='Could not check prime, '
                                                                                   'because the value is not a number.')
        except:
            # if there is no key 'possible_prime' response an error
            return jsonify(title='error', description='Could not handle JSON. Do you have the key possible_prime?')
        # response: {"number": 6, "is_prime": False}
        return jsonify(number=number, is_prime=is_prime(number))
    else:
        # GET request to explain how to use this microservice
        return jsonify(title='PrimeChecker',
                       description='Do a post request http://localhost:1337/prim with JSON {"possible_prime": number}')


if __name__ == '__main__':
    # uses threaded if multiple clients request the website this python file will run multi threaded
    app.run(port=1337, debug=True, threaded=True)
