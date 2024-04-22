#main.py
import csv
import config_data  
from vottun_nft_sdk import NFTSDK  

#data
p_recipient_address="<RECIPIENT>"   
p_network="<NETWORK>"

#functions
def load_nfts_from_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        nfts_to_mint = [row for row in csv_reader]
    return nfts_to_mint

def main():
    sdk = NFTSDK() 
    nfts = load_nfts_from_csv("nfts_to_mint.csv")  

    # Deploy contract  
    contract_details = sdk.deploy_contract(
        name="BMW top cars v3",
        symbol="BMW",
        network=80001,
        gasLimit=6000000,
        alias="BMW top cars v3"
    )
    p_contract_address = contract_details['contractAddress']
    print(f"Contract deployed at: {p_contract_address}")

    for nft in nfts:
        # Step 2: Upload the image file to IPFS
        with open(nft['filepath'], 'rb') as f:
            files = {'file': (nft['name'], f, 'image/jpeg')}   
            upload_result = sdk.upload_files(files=[files])
        
        # Step 3: Load Metadata to IPFS
        attributes = [
            {"trait_type": "Color", "value": nft['color']},
            {"trait_type": "Year", "value": nft['year']},
            {"trait_type": "Model", "value": nft['model']}
        ]
        data = {"artist": nft['artist'], "Quantity": nft['quantity']}
        metadata_result = sdk.load_metadata(
            name=nft['name'],
            image=upload_result['hash'],   
            description=nft['description'],
            attributes=attributes,
            data=data
        )
        
        # Step 4: Mint 
        mint_result = sdk.mint_nft(
            recipientAddress=p_recipient_address, 
            tokenId=nft['name'],   
            ipfsUri=metadata_result['IpfsHash'],
            ipfsHash=metadata_result['IpfsHash'].split('/')[-1],  
            network=p_network,   
            contractAddress=p_contract_address,  
            royaltyPercentage=10,  
            gas=3000000   
        )
        
        # Step 5: Read the Token URI, it's optional but some times the mint don't work without call this
        token_uri_result = sdk.read_token_uri(
            contractAddress=p_contract_address,   
            network=p_network,
            id=nft['name']   
        )

if __name__ == "__main__":
    main()
