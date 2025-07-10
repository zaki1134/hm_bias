from Utils import bellcurve, linear, exponential


def pre_main():
    main()


def main():
    (exponential(3.0, 10, 3.0))
    (exponential(3.0, 10, -3.0))


if __name__ == "__main__":
    try:
        pre_main()
        print(f"{'=' * 60}")
    except Exception as e:
        print(e)
