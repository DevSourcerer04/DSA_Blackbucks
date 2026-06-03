def digital_root_mod9(n: int) -> int:
    n = abs(int(n))
    if n == 0:
        return 0
    r = n % 9
    return 9 if r == 0 else r


def main() -> None:
    s = input("Enter an integer: ").strip()
    if s == "":
        print("No input provided.")
        return
    try:
        n = int(s)
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    print("Single-digit sum:", digital_root_mod9(n))


if __name__ == "__main__":
    main()
