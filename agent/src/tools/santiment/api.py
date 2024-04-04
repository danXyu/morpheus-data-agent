import requests
import json
from typing import List, Dict, Union

class SantimentApi:
    def __init__(self, api_key: str = "c52jivtzcaec2hwt_ywusfqvvl4jed63s"):
        self.api_key = api_key
        self.base_url = 'https://api.santiment.net/graphiql'

    def make_api_request(self, query: str, variables: Dict[str, Union[str, int, List[str]]] = None) -> Dict:
        headers = {'Content-Type': 'application/json', 'Authorization': f'Apikey {self.api_key}'}
        payload = {'query': query, 'variables': variables}
        response = requests.post(self.base_url, headers=headers, json=payload)
        data = response.json()
        return data

    def get_coins_with_highest_price_increase(self, limit: int = 10) -> List[Dict[str, str]]:
        query = '''
            query($slug: String!, $from: DateTime!, $to: DateTime!, $interval: String!, $aggregation: String!) {
                getMetric(metric: "price_usd_change_1d") {
                    timeseriesData(
                        slug: $slug
                        from: $from
                        to: $to
                        interval: $interval
                        aggregation: $aggregation
                    ) {
                        value
                    }
                }
            }
        '''
        variables = {
            'slug': '',
            'from': 'utc_now-1d',
            'to': 'utc_now',
            'interval': '1d',
            'aggregation': 'LAST'
        }
        response_data = self.make_api_request(query, variables)
        price_increase_data = response_data['data']['getMetric']['timeseriesData']
        return price_increase_data

    def get_trending_coins(self, limit: int = 10) -> List[Dict[str, str]]:
        query = '''
            query {
                getTrendingWords(size: 10, from: "2d", to: "now") {
                    topWords {
                        word
                    }
                }
            }
        '''
        response_data = self.make_api_request(query)
        trending_words = response_data['data']['getTrendingWords']['topWords']
        return trending_words

    def get_highest_dev_activity(self, limit: int = 10) -> List[Dict[str, Union[str, int]]]:
        # Get the coins with the highest developer activity for the last 7 days
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

        response_data = self.make_api_request(query, variables)
        print(response_data)
        projects = response_data['data']['allProjectsByFunction']['projects']
        dev_activity_data = []

        # Keep ordering and extract dev activity, name, ticker
        for project in projects:
            dev_activity = project['dev_activity']
            name = project['name']
            ticker = project['ticker']
            dev_activity_data.append((dev_activity, name, ticker))

        return dev_activity_data

    def get_highest_network_growth(self, limit: int = 10) -> List[Dict[str, Union[str, int]]]:
        query = '''
            query($slug: String!, $from: DateTime!, $to: DateTime!, $interval: String!, $aggregation: String!) {
                getMetric(metric: "network_growth") {
                    timeseriesData(
                        slug: $slug
                        from: $from
                        to: $to
                        interval: $interval
                        aggregation: $aggregation
                    ) {
                        value
                    }
                }
            }
        '''
        variables = {
            'slug': '',
            'from': 'utc_now-30d',
            'to': 'utc_now',
            'interval': '1d',
            'aggregation': 'MAX'
        }
        response_data = self.make_api_request(query, variables)
        network_growth_data = response_data['data']['getMetric']['timeseriesData']
        return network_growth_data

    def get_highest_token_circulation(self, limit: int = 10) -> List[Dict[str, Union[str, int]]]:
        query = '''
            query($slug: String!, $from: DateTime!, $to: DateTime!, $interval: String!, $aggregation: String!) {
                getMetric(metric: "circulation") {
                    timeseriesData(
                        slug: $slug
                        from: $from
                        to: $to
                        interval: $interval
                        aggregation: $aggregation
                    ) {
                        value
                    }
                }
            }
        '''
        variables = {
            'slug': '',
            'from': 'utc_now-30d',
            'to': 'utc_now',
            'interval': '1d',
            'aggregation': 'MAX'
        }
        response_data = self.make_api_request(query, variables)
        token_circulation_data = response_data['data']['getMetric']['timeseriesData']
        return token_circulation_data

    def get_highest_transaction_volume(self, limit: int = 10) -> List[Dict[str, Union[str, int]]]:
        query = '''
            query($slug: String!, $from: DateTime!, $to: DateTime!, $interval: String!, $aggregation: String!) {
                getMetric(metric: "transaction_volume") {
                    timeseriesData(
                        slug: $slug
                        from: $from
                        to: $to
                        interval: $interval
                        aggregation: $aggregation
                    ) {
                        value
                    }
                }
            }
        '''
        variables = {
            'slug': '',
            'from': 'utc_now-30d',
            'to': 'utc_now',
            'interval': '1d',
            'aggregation': 'MAX'
        }
        response_data = self.make_api_request(query, variables)
        print(response_data)
        transaction_volume_data = response_data['data']['getMetric']['timeseriesData']
        return transaction_volume_data

