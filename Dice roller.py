from random import randint, choice
import re

def roll_dice(dice_expression):
    # Define a regular expression pattern to match dice expressions with optional negative bonus: 'NdM(+/-)B'
    pattern = re.compile(r'(\d+)?d(\d+)([+-]\d+)?')
    # Remove all whitespace
    dice_expression_clean=re.sub(r"\s+", "", dice_expression)
    # Attempt to match the regular expression to the given dice_expression
    match = pattern.match(dice_expression_clean)
    
    if match:
        # Extract the individual components of the dice expression
        num_dice_str = match.group(1)
        num_dice = int(num_dice_str) if num_dice_str else 1  # Default to 1 if not specified
        dice_faces = int(match.group(2))  # Number of faces on each die (M)
        # Check if there is a bonus specified; if not, default to 0        
        bonus_str = match.group(3)
        bonus = int(bonus_str) if bonus_str else 0
        
        # Roll the dice and calculate the total sum
        roll_total=0
        for _ in range(num_dice):
            roll=randint(1, dice_faces)
            print(roll)
            roll_total+=roll
        total=roll_total+bonus
       # total = sum(randint(1, dice_faces) for _ in range(num_dice)) + bonus
        
        # Return the total sum as the result of the dice roll
        return total
    else:
        # If the dice expression is not in the correct format, raise a ValueError
        raise ValueError("Invalid dice expression: " + dice_expression)
    
while True:
    try:
        dice_expression=input("Input dice and modifier in the format NdM(+/-)B: ").lower()
        total=roll_dice(dice_expression)
        print(f"Total: {total}")
    except (ValueError): print(f"Invalid dice expression: {dice_expression}\nTry expressions like {randint(1, 20)}d{choice([4,6,8,10,12,20])}{choice(['+','-'])}{randint(1,20)}")
