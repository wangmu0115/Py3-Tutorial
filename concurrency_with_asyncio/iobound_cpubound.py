import httpx

URL = "https://www.python.org/"

if __name__ == "__main__":
    # I/O-bound
    resp = httpx.get(URL, timeout=5.0, follow_redirects=True)
    resp.raise_for_status()
    items = resp.headers.items()
    # CPU-bound
    headers = [f"{k}={v}" for k, v in items]
    # CPU-bound
    formatted_headers = "\n".join(headers)
    # I/O-bound
    with open("concurrency_with_asyncio/headers.txt", mode="w") as fp:
        fp.write(formatted_headers)
