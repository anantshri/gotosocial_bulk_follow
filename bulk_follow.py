import requests
import json
import argparse

INSTANCE_NAME="example.org"
TOKEN_VALUE="SOMETHINGTHATLOOKSLIKEATOKEN"

def get_headers(AUTHORIZATION_TOKEN):
    headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer ' + str(AUTHORIZATION_TOKEN),
    }
    return headers

def get_id(account_name,instance_name,headers):
    params = {
        'type': 'accounts',
        'exclude_unreviewed': 'false',
        'q': str(account_name),
        'resolve': 'true',
        'limit': '20',
        'offset': '0',
        'following': 'false',
    }

    search_url="https://" + str(instance_name) + "/api/v1/search"

    response = requests.get(search_url, params=params, headers=headers)

    js=json.loads(response.text)

    follow_id=js["accounts"][0]["id"]

    return follow_id


def follow_user(account_name,instance_name,headers):
    follow_url="https://" + instance_name + "/api/v1/accounts/" + get_id(account_name,instance_name,headers) + "/follow"
    json_data = {
    'reblogs': True,
    'notify': False,
    }
    response = requests.post(follow_url, headers=headers, json=json_data)

    if response.status_code != 200:
        print(response.status_code)
        print(response.text)
    return response.text


def main():
    global TOKEN_VALUE
    global INSTANCE_NAME
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--account", help="Account to Follow", required=True)
    parser.add_argument("-i", "--instance", help="GoToSocial Instance", required=False)
    parser.add_argument("-t", "--token", help="Bearer Token", required=False)
    args = parser.parse_args()
    if args.token is not None:
        TOKEN_VALUE = args.token
    if args.instance is not None:
        INSTANCE_NAME = args.instance
    headers = get_headers(TOKEN_VALUE)
    follow_user(args.account, INSTANCE_NAME,headers)

if __name__ == "__main__":
    main()
