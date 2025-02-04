# echo.py


def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""

    i = 3
    while i > 0:
        repeated = text[-i:]
        print(repeated)
        i -= 1

    print(".")


if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
