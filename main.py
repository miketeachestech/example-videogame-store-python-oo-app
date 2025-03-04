# main.py
# Entry point of the program. It runs the CLI menu system.

from cli.menu import show_main_menu

def main():
    """
    Main function that starts the program by displaying the menu.
    - Follows single responsibility principle (only responsible for starting the app).
    """
    show_main_menu()

if __name__ == "__main__":
    main()