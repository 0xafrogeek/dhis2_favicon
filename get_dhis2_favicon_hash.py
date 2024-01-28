import requests
import sys
import mmh3
import codecs


def get_dhis2_favicon_hash(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        favicon = codecs.encode(response.content, "base64")
        hash = mmh3.hash(favicon)
        return hash
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}", file=sys.stderr)
    except Exception as err:
        print(f"Other error occurred: {err}", file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(f"Usage: python3 {sys.argv[0]} <dhis2-instance-url>")
    else:
        favicon_url = sys.argv[1]
        hash = get_favicon_hash(favicon_url)
        if hash is not None:
            print(f"DHIS2 favicon hash: {hash}")
