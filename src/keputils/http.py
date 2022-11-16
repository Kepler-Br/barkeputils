from urllib.parse import urlparse


class HttpStatus:
    TEMPORARY_REDIRECT = 307
    NOT_FOUND = 404
    OK = 200

    def __init__(self):
        raise RuntimeError('HttpStatus is not supposed to be called')


def extract_domain(url: str) -> str:
    return urlparse(url).netloc


def extract_root_url(url: str) -> str:
    parsed = urlparse(url)

    return f'{parsed.scheme}://{parsed.netloc}'


def extract_path_with_query(url: str) -> str:
    parsed = urlparse(url)

    if len(parsed.query) != 0:
        return f'{parsed.path}?{parsed.query}'
    return parsed.path
