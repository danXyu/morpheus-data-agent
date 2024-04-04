import requests
import json
from typing import List, Dict, Union
from .config import Config

class SantimentAPI:
    def __init__(self):
        self.api_key = Config.SANTIMENT_API_KEY
        self.base_url = Config.SANTIMENT_BASE_URL

    def _make_api_request(self, query: str, variables: Dict[str, Union[str, int, List[str]]] = None) -> Dict:
        headers = {'Content-Type': 'application/json', 'Authorization': f'Apikey {self.api_key}'}
        payload = {'query': query, 'variables': variables}
        response = requests.post(self.base_url, headers=headers, json=payload)
        data = response.json()
        return data

    def get_coins_with_highest_price_increase(self, limit: int = 10) -> List[Dict[str, str]]:
        """
        Retrieves the coins with the highest price increase.
        """
        query = '''
            query($fn:json){
                allProjectsByFunction(function: $fn) {
                    projects {
                        slug name ticker
                        price_usd_change_1d:aggregatedTimeseriesData(
                            metric:"price_usd_change_1d"
                            from:"utc_now-1d"
                            to:"utc_now"
                            aggregation:LAST
                        )
                    }
                }
            }
        '''
        variables = {
            "fn": json.dumps({
                "name": "selector",
                "args": {
                    "filters": [
                        {
                            "args": {
                                "metric": "marketcap_usd",
                                "operator": "greater_than",
                                "dynamicFrom": "1d",
                                "dynamicTo": "now",
                                "aggregation": "last",
                                "threshold": 10000000
                            },
                            "name": "metric"
                        }
                    ],
                    "orderBy": {
                        "aggregation": "last",
                        "dynamicFrom": "1d",
                        "direction": "desc",
                        "dynamicTo": "now",
                        "metric": "price_usd_change_1d"
                    },
                    "pagination": {
                        "page": 1,
                        "pageSize": 10
                    }
                }
            })
        }

        response_data = self._make_api_request(query, variables)
        projects = response_data['data']['allProjectsByFunction']['projects']
        price_increase_data = []

        # Keep ordering and extract price increase, name, ticker
        for project in projects:
            price_increase = project['price_usd_change_1d']
            name = project['name']
            ticker = project['ticker']
            price_increase_data.append((price_increase, name, ticker))
        
        return price_increase_data
    
    def get_highest_dev_activity(self, limit: int = 10) -> List[Dict[str, Union[str, int]]]:
        """
        Get the coins with the highest developer activity for the last 7 days
        """
        query = '''
            query($fn:json){
                allProjectsByFunction(function: $fn) {
                    projects {
                    slug name ticker logoUrl
                    dev_activity:aggregatedTimeseriesData(
                        metric:"dev_activity_1d"
                        from:"utc_now-7d"
                        to:"utc_now"
                        aggregation:AVG
                        )
                    }
                }
            }
        '''

        variables = {
            "fn": json.dumps({
                "name": "selector",
                "args": {
                    "filters": [],
                    "orderBy": {
                        "aggregation": "avg",
                        "dynamicFrom": "7d",
                        "direction": "desc",
                        "dynamicTo": "now",
                        "metric": "dev_activity_1d"
                    },
                    "pagination": {
                        "page": 1,
                        "pageSize": 25
                    }
                }
            })
        }

        response_data = self._make_api_request(query, variables)
        projects = response_data['data']['allProjectsByFunction']['projects']
        dev_activity_data = []

        # Keep ordering and extract dev activity, name, ticker
        for project in projects:
            dev_activity = project['dev_activity']
            name = project['name']
            ticker = project['ticker']
            dev_activity_data.append((dev_activity, name, ticker))

        return dev_activity_data

    # TODO: Fix these functions
    # 
    # def get_highest_network_growth(self, limit: int = 10) -> List[Dict[str, Union[str, int]]]:
    #     """
    #     Get the coins with the highest network growth for the last 30 days
    #     """
    #     query = '''
    #         query($fn:json){
    #             allProjectsByFunction(function: $fn) {
    #                 projects {
    #                     slug name ticker
    #                     network_growth:aggregatedTimeseriesData(
    #                         metric:"network_growth_30d"
    #                         from:"utc_now-30d"
    #                         to:"utc_now"
    #                         aggregation:SUM
    #                     )
    #                 }
    #             }
    #         }
    #     '''
    #     variables = {
    #         "fn": json.dumps({
    #             "name": "selector",
    #             "args": {
    #                 "filters": [],
    #                 "orderBy": {
    #                     "aggregation": "sum",
    #                     "dynamicFrom": "30d",
    #                     "direction": "desc",
    #                     "dynamicTo": "now",
    #                     "metric": "network_growth_30d"
    #                 },
    #                 "pagination": {
    #                     "page": 1,
    #                     "pageSize": limit
    #                 }
    #             }
    #         })
    #     }
    #     response_data = self._make_api_request(query, variables)
    #     projects = response_data['data']['allProjectsByFunction']['projects']
    #     network_growth_data = [{"name": project['name'], "ticker": project['ticker'], "network_growth": project['network_growth']} for project in projects]

    #     return network_growth_data

    # def get_highest_token_circulation(self, limit: int = 10) -> List[Dict[str, Union[str, int]]]:
    #     """
    #     Get the coins with the highest token circulation for the last 30 days
    #     """
    #     query = '''
    #         query($fn:json){
    #             allProjectsByFunction(function: $fn) {
    #                 projects {
    #                     slug name ticker
    #                     token_circulation:aggregatedTimeseriesData(
    #                         metric:"token_circulation_30d"
    #                         from:"utc_now-30d"
    #                         to:"utc_now"
    #                         aggregation:SUM
    #                     )
    #                 }
    #             }
    #         }
    #     '''
    #     variables = {
    #         "fn": json.dumps({
    #             "name": "selector",
    #             "args": {
    #                 "filters": [],
    #                 "orderBy": {
    #                     "aggregation": "sum",
    #                     "dynamicFrom": "30d",
    #                     "direction": "desc",
    #                     "dynamicTo": "now",
    #                     "metric": "token_circulation_30d"
    #                 },
    #                 "pagination": {
    #                     "page": 1,
    #                     "pageSize": limit
    #                 }
    #             }
    #         })
    #     }
    #     response_data = self._make_api_request(query, variables)
    #     projects = response_data['data']['allProjectsByFunction']['projects']
    #     token_circulation_data = [{"name": project['name'], "ticker": project['ticker'], "token_circulation": project['token_circulation']} for project in projects]

    #     return token_circulation_data

    # def get_highest_transaction_volume(self, limit: int = 10) -> List[Dict[str, Union[str, int]]]:
    #     """
    #     Get the coins with the highest transaction volume for the last 30 days
    #     """
    #     query = '''
    #         query($fn:json){
    #             allProjectsByFunction(function: $fn) {
    #                 projects {
    #                     slug name ticker
    #                     transaction_volume:aggregatedTimeseriesData(
    #                         metric:"transaction_volume_30d"
    #                         from:"utc_now-30d"
    #                         to:"utc_now"
    #                         aggregation:SUM
    #                     )
    #                 }
    #             }
    #         }
    #     '''
    #     variables = {
    #         "fn": json.dumps({
    #             "name": "selector",
    #             "args": {
    #                 "filters": [],
    #                 "orderBy": {
    #                     "aggregation": "sum",
    #                     "dynamicFrom": "30d",
    #                     "direction": "desc",
    #                     "dynamicTo": "now",
    #                     "metric": "transaction_volume_30d"
    #                 },
    #                 "pagination": {
    #                     "page": 1,
    #                     "pageSize": limit
    #                 }
    #             }
    #         })
    #     }
    #     response_data = self._make_api_request(query, variables)
    #     projects = response_data['data']['allProjectsByFunction']['projects']
    #     transaction_volume_data = [{"name": project['name'], "ticker": project['ticker'], "transaction_volume": project['transaction_volume']} for project in projects]

    #     return transaction_volume_data
