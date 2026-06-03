def digital_root(n: int) -> int:
    n = abs(int(n))
    while n >= 10:
        s = 0
        while n:
            s += n % 10
            n //= 10
        n = s
    return n


def main() -> None:
    try:
        s = input("Enter an integer: ").strip()
        if s == "":
            print("No input provided.")
            return
        n = int(s)
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    print("Single-digit sum:", digital_root(n))


if __name__ == "__main__":
    main()