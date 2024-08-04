import requests

initial_currency = input("Enter a initial currency (e.g., USD): ")
target_currency = input("Enter a target currency (e.g., EUR): ")

while True:
    try:
        amount = float(input("Enter the amount: "))
    except ValueError:
        print("The amount must be a numberic value!")
        continue

    if amount <= 0:
        print("The amount must be greater than 0")
        continue
    else:
        break

url = f"https://api.apilayer.com/fixer/convert?to={target_currency}&from={initial_currency}&amount={amount}"

payload = {}
headers= {
  "apikey": "iYBJCGj2vBiWcPJlx5ES5LllR2bdA4iI"
}

try:
    response = requests.get(url, headers=headers, data=payload)
    response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    quit()

status_code = response.status_code

if status_code == 200:
    result = response.json()
    converted_amount = result.get('result')

    if converted_amount is None:
        # print("Error in conversion. Please check the currency codes and try again.")
        error_info = result.get('error', {}).get('info', 'Unknown error.')
        print(f"Error in conversion: {error_info}")
    else:
        print(f'{amount} {initial_currency.upper()} = {converted_amount} {target_currency.upper()}')

else:
    print("Sorry, there was a problem. Please try again later.")
