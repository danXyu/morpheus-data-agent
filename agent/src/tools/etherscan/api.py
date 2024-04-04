import requests

class EtherscanAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.etherscan.io/api'

    def make_api_request(self, module, action, **kwargs):
        url = f"{self.base_url}?module={module}&action={action}&apikey={self.api_key}"
        for key, value in kwargs.items():
            url += f"&{key}={value}"
        response = requests.get(url)
        data = response.json()
        return data

    def get_ether_balance(self, address):
        module = 'account'
        action = 'balance'
        tag = 'latest'
        response_data = self.make_api_request(module, action, address=address, tag=tag)
        balance_wei = int(response_data['result'])
        balance_ether = balance_wei / 10**18
        return balance_ether

    def check_contract_execution_status(self, transaction_hash):
        module = 'transaction'
        action = 'getstatus'
        response_data = self.make_api_request(module, action, txhash=transaction_hash)
        status = response_data['result']['isError']
        return status == '0'

    def check_transaction_receipt_status(self, transaction_hash):
        module = 'transaction'
        action = 'gettxreceiptstatus'
        response_data = self.make_api_request(module, action, txhash=transaction_hash)
        status = response_data['result']['status']
        return status == '1'

    def get_erc20_token_supply(self, contract_address):
        module = 'stats'
        action = 'tokensupply'
        response_data = self.make_api_request(module, action, contractaddress=contract_address)
        total_supply = int(response_data['result'])
        return total_supply

    def get_confirmation_time_estimate(self):
        module = 'gastracker'
        action = 'gasestimate'
        response_data = self.make_api_request(module, action)
        confirmation_times = {
            'safe_low': response_data['result']['SafeLow'],
            'standard': response_data['result']['Standard'],
            'fast': response_data['result']['Fast'],
            'fastest': response_data['result']['Fastest']
        }
        return confirmation_times