import requests
from pprint import pprint

coindesk_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'


def main():
    num_of_bitcoin = get_number_of_bitcoin()
    data = request_exchange_rate()
    dollars_exchange_rate = get_exchange_rate(data)
    bitcoin_value_in_dollars = calculate_bitcoin_to_dollar(dollars_exchange_rate, num_of_bitcoin)
    display_result(num_of_bitcoin, bitcoin_value_in_dollars)

def get_number_of_bitcoin():
    while True:
        try:
            num_of_bitcoin = float(input('Enter the number bitcoins you want to convert: '))
            if num_of_bitcoin<=0:
                raise ValueError('Number of bitcoin must be >0')
            return num_of_bitcoin
        except:
            print('Enter a number greater than 0')


def request_exchange_rate():
    try:
        response = requests.get(coindesk_url)
        response.raise_for_status() #raises an exception for 400 or 500 status code
        data = response.json() #convert response to json (like python dictionary)
        return data
    except Exception as e:
        print(e)
        print('There was an error making the request')

def get_exchange_rate(data): #extra info from data returned from request
    dollars_exchange_rate = data['bpi']['USD']['rate_float']
    return dollars_exchange_rate
        

def calculate_bitcoin_to_dollar(dollars_exchange_rate, num_of_bitcoin):
    bitcoin_value_in_dollars=  dollars_exchange_rate  * num_of_bitcoin
    return bitcoin_value_in_dollars

def display_result( num_of_bitcoin,bitcoin_value_in_dollars):
    print(f'$ {bitcoin_value_in_dollars:.2f} is the equivalent of {num_of_bitcoin} bitcoins')




if __name__ == "__main__":
    main()

    #APIpowered by Coindesk