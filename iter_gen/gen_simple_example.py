def echo(value):
    print("Execution starts when `next()` is called for the first time.")
    try:
        while True:
            try:
                value = yield value
            except Exception as e:
                print(f"{e!r}")
                value = e
    finally:
        print("Don't forget to clean up when `close()` is called.")


if __name__ == "__main__":
    gen = echo(1)
    print(next(gen))
    print(next(gen))
    print(gen.send(2))
    print(f"{gen.throw(TypeError('spam'))!r}")
    print(gen.close())
