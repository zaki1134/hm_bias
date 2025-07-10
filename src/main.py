def pre_main():
    main()


def main():
    pass


if __name__ == "__main__":
    try:
        pre_main()
        print(f"{'=' * 60}")
    except Exception as e:
        print(e)
