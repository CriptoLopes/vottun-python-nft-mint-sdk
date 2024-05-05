# ================================================
# Author: Antonio23
# Description: Program to check NFT ownership
# ================================================

import requests

def check_nft_ownership(contract_address, token_id, owner_address, app_id, api_key):
    """
    Check if the provided address is the owner of the specified NFT using the Vottun API.

    Args:
    contract_address (str): The smart contract address of the NFT.
    token_id (str): The token ID of the NFT.
    owner_address (str): The Ethereum address to verify against the NFT.
    app_id (str): Application ID provided by Vottun.
    api_key (str): API key provided by Vottun.

    Returns:
    bool: True if the provided address is the owner, False otherwise. Returns None if API call fails.
    """
    url = "https://api.vottun.tech/erc/v1/erc721/ownerOf"
    headers = {
        'appId': app_id,
        'apiKey': api_key,
        'Content-Type': 'application/json'
    }
    payload = {
        'contractAddress': contract_address,
        'network': '80001',  # Adjust this according to the blockchain network ID
        'id': token_id
    }
    
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # Compare owner address from response to the provided owner_address, case insensitive
        return data['owner'].lower() == owner_address.lower()
    else:
        # Return None if the API call was unsuccessful
        return None

# Example parameters
contract_address = '0x9CfFCE57A4c48BeF32a2137584672A36971af5B7'
token_id = '1'
owner_address = '0x7F06A3D6A1E3Adc9Fe9FA50Be3fB88bFD66efc3B'
app_id = 'your_app_id'
api_key = 'your_api_key'

# Call the function and print the result
is_owner = check_nft_ownership(contract_address, token_id, owner_address, app_id, api_key)
print(f"Is the address {owner_address} the owner of the NFT? {is_owner}")
