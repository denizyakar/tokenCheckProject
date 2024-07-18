import requests
import json

# Sample wallet addresses for testing:
# 0x436a1d6a6DdCb2781b8a28373756829E5fb0f251
# 0x518489F9ed41Fc35BCD23407C484F31897067ff0
# 0x88AA83547A5A647EfA4c41991BEfC87705Bd71D2
# 0x7F6aAe679dC0bD7d6ecF62224A5a3423877d6Be7
# For more wallet addresses, visit: https://etherscan.io/

def fetch_eth_balance(address: str, api_key: str, api_secret: str) -> float:
    # Infura API endpoint
    endpoint = f"https://mainnet.infura.io/v3/{api_key}"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "jsonrpc": "2.0",
        "method": "eth_getBalance",
        "params": [address, "latest"],
        "id": 1
    }

    response = requests.post(endpoint, json=data, headers=headers, auth=(api_key, api_secret))

    if response.status_code == 200:
        result = response.json()
        wei_balance = int(result['result'], 16)
        eth_balance = wei_balance / 10**18
        return eth_balance
    else:
        response.raise_for_status()

def verify_eth_balance(address: str, min_balance: float, api_key: str, api_secret: str) -> bool:
    balance = fetch_eth_balance(address, api_key, api_secret)
    return balance > min_balance

# Get wallet address from user input
wallet_address = input("Please enter the wallet address: ")
min_balance = 1.0  # Set the threshold balance
api_key = '62323220b8774f4aba258e0cb701a069'
api_secret = 'IwJJ45q3FwdAgX1O25lDthqgQQnO3QaBEPxNq8OU5Cj0CU1KfC8qHQ'

result = verify_eth_balance(wallet_address, min_balance, api_key, api_secret)

# Display the ETH amount:
eth_balance = fetch_eth_balance(wallet_address, api_key, api_secret)
print("Threshold: ", min_balance)
print("\nETH in Wallet: ", eth_balance)
print("\nIs ETH in Wallet more than the threshold?")

print(result)  # True or False
