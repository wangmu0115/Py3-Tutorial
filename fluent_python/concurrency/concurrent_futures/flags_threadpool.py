from concurrent.futures import ThreadPoolExecutor

from .flags import DEST_DIR, get_flag, main, save_flag


def download_one(cc: str):
    image = get_flag(cc)
    save_flag(image, f"{cc}.gif", DEST_DIR)
    print(cc, end=" ", flush=True)
    return cc


def download_many(cc_list: list[str]) -> int:
    print(cc_list)
    with ThreadPoolExecutor(max_workers=20) as executor:
        res = executor.map(download_one, cc_list)
    print(list(res))
    return len(list(res))


if __name__ == "__main__":
    main(download_many)
