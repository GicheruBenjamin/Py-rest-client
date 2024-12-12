from public.Config import load_config
from public.Input import get_input
from public import Comments, Users, Posts, Todos

def main():
    config = load_config()
    base_url = config["BASE_URL"]

    menu = """
    Choose an entity to fetch:
    1. Comments
    2. Users
    3. Posts
    4. Todos
    5. Exit
    """
    while True:
        print(menu)
        choice = get_input("Enter your choice (1-5): ")
        
        if choice == "1":
            handle_entity(Comments, base_url, "Comment")
        elif choice == "2":
            handle_entity(Users, base_url, "User")
        elif choice == "3":
            handle_entity(Posts, base_url, "Post")
        elif choice == "4":
            handle_entity(Todos, base_url, "Todo")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def handle_entity(module, base_url, entity_name):
    print(f"\nFetching {entity_name}s...")
    option = get_input(f"Do you want to fetch all {entity_name}s or a specific one? (all/id): ").lower()
    
    if option == "all":
        data = module.fetch_all(base_url)
        for item in data[:5]:  # Display the first 5 items
            print(item)
    elif option == "id":
        entity_id = int(get_input(f"Enter {entity_name} ID: "))
        data = module.fetch_by_id(base_url, entity_id)
        print(data)
    else:
        print("Invalid option. Returning to main menu.")

if __name__ == "__main__":
    main()
