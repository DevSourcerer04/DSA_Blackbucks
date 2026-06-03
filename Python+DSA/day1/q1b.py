def digital_root_mod(n: int) -> int:
    n = abs(int(n))
    while n >= 10:
        s = 0
        while n > 0:
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

    print("Single-digit sum:", digital_root_mod(n))


if __name__ == "__main__":
    main()
