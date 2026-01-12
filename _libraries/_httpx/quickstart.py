import httpx

from _builtins.pprint import console_print, head_print

if __name__ == "__main__":
    head_print("HTTPX GET")
    get_resp = httpx.get("https://httpbin.org/get")
    console_print(get_resp)
    head_print("HTTPX POST")
    post_resp = httpx.post("https://httpbin.org/post", data={"key": "value"})
    console_print(post_resp)
    head_print("HTTPX PUT")
    put_resp = httpx.put("https://httpbin.org/put", data={"key": "value"})
    console_print(put_resp)

    