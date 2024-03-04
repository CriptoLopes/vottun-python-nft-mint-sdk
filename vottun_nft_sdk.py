#vottun_nft_sdk.py
import requests

class NFTSDK:
    def __init__(self):
        self.deploy_url = "https://api.vottun.tech/erc/v1/erc721/deploy"
        self.ipfs_upload_url = "https://ipfsapi-v2.vottun.tech/ipfs/v2/file/upload"
        self.ipfs_metadata_url = "https://ipfsapi-v2.vottun.tech/ipfs/v2/file/metadata"
        self.mint_url = "https://api.vottun.tech/erc/v1/erc721/mint"
        self.token_uri_url = "https://api.vottun.tech/erc/v1/erc721/tokenUri"
    
    def deploy_contract(self, name, symbol, network, gasLimit, alias):
        payload = {
            "name": name,
            "symbol": symbol,
            "network": network,
            "gasLimit": gasLimit,
            "alias": alias
        }
        response = requests.post(self.deploy_url, json=payload)
        return response.json()

    def upload_files(self, files):
        # files should be a list of ('file', open('file_path', 'rb')) tuples
        response = requests.post(self.ipfs_upload_url, files=files)
        return response.json()

    def load_metadata(self, name, image, description, attributes, data):
        payload = {
            "name": name,
            "image": image,
            "description": description,
            "attributes": attributes,
            "data": data
        }
        response = requests.post(self.ipfs_metadata_url, json=payload)
        return response.json()

    def mint_nft(self, recipientAddress, tokenId, ipfsUri, ipfsHash, network, contractAddress, royaltyPercentage, gas):
        payload = {
            "recipientAddress": recipientAddress,
            "tokenId": tokenId,
            "ipfsUri": ipfsUri,
            "ipfsHash": ipfsHash,
            "network": network,
            "contractAddress": contractAddress,
            "royaltyPercentage": royaltyPercentage,
            "gas": gas
        }
        response = requests.post(self.mint_url, json=payload)
        return response.json()

    def read_token_uri(self, contractAddress, network, id):
        payload = {
            "contractAddress": contractAddress,
            "network": network,
            "id": id
        }
        response = requests.post(self.token_uri_url, json=payload)
        return response.json()
