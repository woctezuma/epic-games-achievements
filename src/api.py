import requests

DEFAULT_SUBDOMAIN: str = "graphql"


def get_graphql_api_url(subdomain=DEFAULT_SUBDOMAIN):
    return f"https://{subdomain}.epicgames.com/ue/graphql"


def send_post_request_to_api(json_data, subdomain=DEFAULT_SUBDOMAIN, verbose=True):
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
