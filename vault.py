# Shadow-Sec Knowledge Vault
import os  # Ensure the 'os' module is imported

# ASCII Art Header
ascii_art = r"""
  ____  _               _                   ____
 / ___|| |__   __ _  __| | _____      __   / ___|  ___  ___
 \___ \| '_ \ / _` |/ _` |/ _ \ \ /\ / /___\___ \ / _ \/ __|
  ___) | | | | (_| | (_| | (_) \ V  V /_____|__) |  __/ (__
 |____/|_| |_|\__,_|\__,_|\___/ \_/\_/     |____/ \___|\___|
"""
print(ascii_art)

# Menu Function
def main_menu():
    print("\nWelcome to the Decentralised Shadow-Sec Vault!")
    print("1. List Tools")
    print("2. Add Tool (Admin Only)")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        list_tools()
    elif choice == "2":
        add_tool()
    elif choice == "3":
        confirm_exit()
    else:
        print("Invalid choice. Please try again.")
        main_menu()

# Function to List Tools
def list_tools():
    tools_dir = "./tools"
    if not os.path.exists(tools_dir):
        print("No tools directory found. Please create one!")
        return
    categories = os.listdir(tools_dir)
    if categories:
        print("Tool Categories:")
        tool_paths = []
        for category in categories:
            category_path = os.path.join(tools_dir, category)
            if os.path.isdir(category_path):
                print(f"\n[{category.upper()}]")
                tools = os.listdir(category_path)
                if tools:
                    for i, tool in enumerate(tools, start=1):
                        print(f"  {i}. {tool}")
                        tool_paths.append(os.path.join(category_path, tool))
                else:
                    print("  No tools available in this category.")
        if tool_paths:
            try:
                choice = int(input("\nEnter the number of the tool to execute: ")) - 1
                if 0 <= choice < len(tool_paths):
                    os.system(tool_paths[choice])
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid input.")
    else:
        print("No tools available yet.")

 #function to Add Tool (Placeholder)
def add_tool():
    tools_dir = "./tools"
    print("\nAdd a New Tool")
    category = input("Enter the category (e.g., recon, exploit, utility): ").lower()
    category_path = os.path.join(tools_dir, category)
    if not os.path.exists(category_path):
        os.makedirs(category_path)
    tool_name = input("Enter the tool name (e.g., tool.sh): ")
    tool_path = os.path.join(category_path, tool_name)
    print("Paste the tool code below. Press CTRL+D when done.")
    try:
        with open(tool_path, "w") as f:
            while True:
                line = input()
                f.write(line + "\n")
        os.chmod(tool_path, 0o755)  # Make the tool executable
        print(f"Tool '{tool_name}' added successfully to '{category}'.")
    except EOFError:
        print(f"Finished adding tool '{tool_name}'.")


# Exit Confirmation
def confirm_exit():
    confirm = input("Are you sure you want to exit the Shadow-Sec Network (y/n): ")
    if confirm.lower() == "y":
        print("Exiting The Decentralised Shadow-Sec Network... Goodbye!")
        exit()
    else:
        main_menu()

# Run the Menu System
if __name__ == "__main__":
    main_menu()
