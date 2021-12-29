import requests
import os
import argparse
from dotenv import load_dotenv
from urllib.parse import urlparse


def shorten_link(bitly_token, user_input):
    requests.get(user_input).raise_for_status()
    header = {'Authorization': 'Bearer {}'.format(bitly_token)}
    json = {'long_url': user_input}
    target_url = 'https://api-ssl.bitly.com/v4/shorten'
    short_link = requests.post(
      target_url,
      headers=header,
      json=json
    )
    short_link.raise_for_status()
    if 'error' in short_link.json():
        raise requests.exceptions.HTTPError(short_link.json(['error']))

    return short_link.json()['id']


def count_clicks(bitly_token, user_input):
    url = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'\
        .format(user_input)
    data = requests.get(
      url,
      headers={'Authorization': 'Bearer {}'.format(bitly_token)}
    )
    data.raise_for_status()

    return data.json()['total_clicks']


def is_bitlink(bitly_token, url):
    header = {'Authorization': 'Bearer {}'.format(bitly_token)}
    response = requests.get(
        'https://api-ssl.bitly.com/v4/bitlinks/{}'.format(url),
        headers=header
    )
    return response.ok


def process_link(bitly_token, url):
    parsed = urlparse(url)
    if parsed.netloc == 'bit.ly' and parsed.scheme is not None:
        url = '{}{}{}{}{}'.format(
            parsed.netloc,
            parsed.path,
            parsed.params,
            parsed.query,
            parsed.fragment
        )
    try:
        if is_bitlink(bitly_token, url):
            return f'Times bitly was clicked: {count_clicks(bitly_token, url)}'
        return(shorten_link(bitly_token, url))
    except (
        requests.exceptions.HTTPError,
        requests.exceptions.ConnectionError,
        requests.exceptions.MissingSchema
    ):
        return "Not a valid link"


def main():
    load_dotenv()
    bitly_token = os.getenv('BITLY_TOKEN')
    parser = argparse.ArgumentParser(
        description='Get a shortlink from a url or clicks from a shortlink'
    )
    parser.add_argument('url', help='url to be shortened or counted')
    args = parser.parse_args()
    print(process_link(bitly_token, args.url))

if __name__ == "__main__":
    main()
