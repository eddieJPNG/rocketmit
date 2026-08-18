import argparse


ROCKET = ":rocket:"


def format_commit(message: str) -> str:
    message = message.strip()

    if not message:
        raise ValueError("A mensagem não pode estar vazia.")

    return f"git commit -m \"{ROCKET} {message} {ROCKET}\""


def main():
    parser = argparse.ArgumentParser(
        description="Formata mensagens de commit com emojis."
    )

    parser.add_argument(
        "message",
        nargs="+",
        help="Mensagem do commit"
    )

    args = parser.parse_args()

    message = " ".join(args.message)

    print(format_commit(message))


if __name__ == "__main__":
    main()