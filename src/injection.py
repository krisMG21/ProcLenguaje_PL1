def main():
    while True:
        try:
            eval(input())
        except SyntaxError:
            print("Error")

if __name__ == "__main__":
    main()
