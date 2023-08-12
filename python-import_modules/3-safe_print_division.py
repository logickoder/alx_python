def safe_print_division(a: int, b: int):
    result: float | None = None
    try:
        result = a / b
    except ZeroDivisionError:
        return result
    finally:
        print("Inside result: {}".format(result))
        return result
