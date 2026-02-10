from concurrent.futures import ThreadPoolExecutor, as_completed

import httpx

URLs = [
    "http://www.foxnews.com/",
    "http://www.cnn.com/",
    "http://europe.wsj.com/",
    "http://www.bbc.co.uk/",
    "http://nonexistent-subdomain.python.org/",
]


def load_url(url, timeout):
    resp = httpx.get(url, timeout=timeout, follow_redirects=True)
    resp.raise_for_status()
    return resp.content


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(load_url, url, 5.0): url for url in URLs}
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as e:
                print(f"{url!r} generated an exception: {e}")
            else:
                print(f"{url!r} page is {len(data)} bytes.")
