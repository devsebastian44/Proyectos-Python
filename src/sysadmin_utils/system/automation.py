import os
import sys

def clear_screen():
    """Clears the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")

def interactive_menu():
    """Runs a simple interactive menu."""
    clear_screen()
    print("--- System Automation Menu ---")
    
    while True:
        try:
            user_input = input("\nEnter option (1: Print XD, q: Quit): ").strip()
            
            if not user_input:
                print("Please enter a valid option.")
                continue
                
            if user_input == "1":
                print("XD")
            elif user_input.lower() == "q":
                print("Exiting...")
                break
            else:
                print(f"Unknown option: {user_input}")
                
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    interactive_menu()
