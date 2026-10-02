# adventure.py
# Name: [Your Name Here]
# Date: October 2, 2026

# Track player health (starts at 10)
health = 10

# Requirement: Print initial health before taking any input
print(f"Health: {health}")

# First Choice
choice1 = input("Do you go left or right? ")

if choice1 == "left":
    # Health decreases on left path
    health = health - 3
    print(f"Health: {health}")
    
    # Second Choice
    choice2 = input("Do you fight or run? ")
    
    if choice2 == "fight":
        # Health decreases during fight
        health = health - 2
        print(f"Health: {health}")
        
        # Third Choice
        choice3 = input("Do you take or leave? ")
        
        if choice3 == "take":
            # Graded Win Path (left -> fight -> take)
            # Health increases and satisfies numeric comparison (health >= 8)
            health = health + 3
            print(f"Health: {health}")
            
            # Numeric comparison + Compound condition requirement (and/or)
            if health >= 8 and health <= 20:
                print("You found a powerful treasure!")
            
            print("=== YOU WIN ===")
            
        elif choice3 == "leave":
            print("You walked away empty handed.")
            print("=== GAME OVER ===")
        else:
            print("Invalid choice.")
            
    elif choice2 == "run":
        print("You ran away safely.")
        print("=== GAME OVER ===")
    else:
        print("Invalid choice.")

elif choice1 == "right":
    # Health decreases on right path
    health = health - 4
    print(f"Health: {health}")
    
    # Second Choice
    choice2 = input("Do you fight or run? ")
    
    if choice2 == "run":
        # Health decreases while running
        health = health - 1
        print(f"Health: {health}")
        
        # Third Choice
        choice3 = input("Do you take or leave? ")
        
        if choice3 == "leave":
            # Graded Loss Path (right -> run -> leave)
            health = health - 1
            print(f"Health: {health}")
            print("=== GAME OVER ===")
            
        elif choice3 == "take":
            print("=== YOU WIN ===")
        else:
            print("Invalid choice.")
            
    elif choice2 == "fight":
        print("You were overwhelmed in combat.")
        print("=== GAME OVER ===")
    else:
        print("Invalid choice.")

else:
    # Invalid first choice halts immediately
    print("Invalid choice.")
