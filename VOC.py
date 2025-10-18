def feed_pet(pet):
    """
    Feeds the pet:
    - Decreases hunger by 15 (minimum 0).
    - Slightly decreases happiness by 5 (minimum 0).
    """
    pet['hunger'] = max(0, pet['hunger'] - 15)  # Reduce hunger safely
    pet['happiness'] = max(0, pet['happiness'] - 5)  # Slight happiness drop
    print(f"You fed {pet['name']}.")

def play_with_pet(pet):
    """
    Plays with the pet:
    - Increases happiness by 15 (maximum 100).
    - Increases hunger by 10 (maximum 100).
    """
    pet['happiness'] = min(100, pet['happiness'] + 15)  # Increase happiness
    pet['hunger'] = min(100, pet['hunger'] + 10)  # Increase hunger
    print(f"You played with {pet['name']}.")

def check_status(pet):
    """
    Displays the current hunger and happiness levels of the pet.
    """
    print(f"\n{pet['name']}'s current status:")
    print(f"Hunger: {pet['hunger']} / 100")
    print(f"Happiness: {pet['happiness']} / 100")

def update_pet_status(pet):
    """
    Simulates time passing:
    - Hunger increases by 5 (max 100).
    - Happiness decreases by 5 (min 0).
    - If hunger > 80, happiness decreases by an additional 10.
    """
    pet['hunger'] = min(100, pet['hunger'] + 5)
    pet['happiness'] = max(0, pet['happiness'] - 5)

    if pet['hunger'] > 80:
        pet['happiness'] = max(0, pet['happiness'] - 10)
        print(f"{pet['name']} is very hungry and feels sad!")

def main():
    # Ask the user to name their pet
    pet_name = input("What would you like to name your pet? ").strip()
    if not pet_name:
        pet_name = "Fluffy"  # Default name if none given

    # Initialize pet attributes
    pet = {
        'name': pet_name,
        'hunger': 50,
        'happiness': 50
    }

    while True:
        print("\n--- Virtual Pet Simulator ---")
        print("1. Feed the pet")
        print("2. Play with the pet")
        print("3. Check pet status")
        print("4. Quit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            feed_pet(pet)
        elif choice == '2':
            play_with_pet(pet)
        elif choice == '3':
            check_status(pet)
        elif choice == '4':
            print(f"Thanks for playing! Goodbye from {pet['name']}!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 4.")
            continue

        update_pet_status(pet)

        # Check for game over conditions
        if pet['hunger'] >= 100:
            print(f"Oh no! {pet['name']} became too hungry! Game over.")
            break
        if pet['happiness'] <= 0:
            print(f"Oh no! {pet['name']} became too sad! Game over.")
            break

if __name__ == "__main__":
    main()
