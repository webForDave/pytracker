print("Welcome to PyTracker")

def main():
    return get_task()

def get_task():
    while True:
        try:
            task = input("Enter a task ").strip()
            with open("text.txt", "a") as file:
                file.write(f"{task}\n")
            return "Done"
        except (ValueError, KeyboardInterrupt):
            break

if __name__ == "__main__":
    main()