import emoji


def hello():
    return emoji.emojize("Hello :earth_africa:! I :heart: Python!", language="alias")


if __name__ == "__main__":
    print(hello())
