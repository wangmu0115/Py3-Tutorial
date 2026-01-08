from _builtins.pprint import console_print, head_print, tail_print

# cd ${MyPy3 Path}
# python -m fluent_python_2nd.chapter07.example07
if __name__ == "__main__":
    head_print("Example 7.7 sort by `lambda`")

    fruits = ["strawberry", "fig", "apple", "cherry", "raspberry", "banana"]
    console_print(sorted(fruits, key=lambda w: w))
    console_print(sorted(fruits, key=lambda w: w[::-1]))

    tail_print("Example 7.7 sort by `lambda`")
