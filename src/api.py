import requests


def get_graphql_api_url(subdomain="graphql"):
    return f"https://{subdomain}.epicgames.com/graphql"


def send_post_request_to_api(json_data, subdomain="graphql", verbose=True):
    r = requests.post(get_graphql_api_url(subdomain=subdomain), json=json_data)
    return to_data(r, verbose=verbose)


def to_data(response, verbose=True):
    if response.ok:
        data = response.json()
    else:
        data = None
        if verbose:
            print(f"Status code = {response.status_code}")
    return data
