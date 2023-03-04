import requests
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'converter/index.html')

def result(request):
    from_currency = request.POST['from'].upper()
    to_currency = request.POST['to'].upper()
    amount = request.POST['amount']

    # Check if the input is valid
    if not from_currency.isalpha() or not to_currency.isalpha() or not amount.isdigit():
        return render(request, 'converter/invalid_input.html')

    # Make the API call
    url = f'https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}'
    response = requests.get(url)

    # Check if the API call was successful
    if response.status_code != 200:
        return render(request, 'converter/invalid_input.html')

    data = response.json()
    result = f'{data["rates"][to_currency]}'

    '''# Extract the conversion rate from the API response
    conversion_rate = response.json()['rates'][to_currency]

    # Calculate the result
    result = float(amount) * conversion_rate'''

    return render(request, 'converter/result.html', {'from_currency': from_currency, 'to_currency': to_currency, 'amount': amount, 'result': result})

def invalid_input(request):
    return render(request, 'converter/invalid_input.html')
