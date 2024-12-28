import subprocess

def main():
    # Ask for the user's age
    while True:
        try:
            age = int(input("What is your age? "))
            
            if 0 <= age <= 999:
                break  # Valid input
            else:
                print("Please enter a valid age (a number with up to 3 digits).")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"Your age is {age}")

    # Ask if the user wants to open the Python file
    user_choice = input("\nDo you want to open the Python file (example.py)? (yes/no): ").strip().lower()

    if user_choice == 'yes':
        try:
            # Attempt to run example.py
            subprocess.run(["python", "example.py"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error launching Python file: {e}")
        except FileNotFoundError:
            print("Python is not installed or not in the system PATH.")
        except Exception as ex:
            print(f"An error occurred: {ex}")
    else:
        print("You chose not to open the Python file.")

    input("Press Enter to exit.")

if __name__ == "__main__":
    main()
