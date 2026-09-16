
def call_summary(function_name, *args, **kwargs):
    all_args = []

    for value in args:
        all_args.append(repr(value))

    for key, value in kwargs.items():
        all_args.append(f"{key}={value!r}")

    return f"{function_name}({', '.join(all_args)})"


print(call_summary("print", "hello", end="\n"))
print(call_summary("sum", 1, 2, 3))
