from random import randint, choice
import re

def dice_choice():
    dice_expression=input("Input dice and modifier in the format NdM(+/-)B: ").lower()
    return dice_expression

def roll_dice():

    def roller(num_dice, dice_faces, bonus_str, explode, advantage, drop, reroll, pen):
        rolls=[]
        reroll_count=0
        rerolls=None
        for _ in range(num_dice):
            roll=randint(1, dice_faces)
            print(roll)
            rolls.append(roll)
            if explode:
                rerolls="explosions"
                while roll== dice_faces:
                    new_roll = randint(1, dice_faces)
                    print(f"!!{new_roll}!!")
                    reroll_count+=1
                    rolls.append(new_roll)
                    roll=new_roll
            if reroll:
                rerolls="rerolls"
                while roll==1:
                    rolls.pop()
                    new_roll = randint(1, dice_faces)
                    print(f"!!{new_roll}!!")
                    reroll_count+=1
                    rolls.append(new_roll)
                    roll=new_roll
            if pen:
                rerolls="penetrations"
                while roll== dice_faces:
                    new_roll = randint(1, dice_faces)
                    penetrating_die=new_roll-1
                    print(f"!!{penetrating_die}!!")
                    reroll_count+=1
                    rolls.append(penetrating_die)
                    roll=new_roll
        if reroll_count>0:
            print(f"\n{reroll_count} {rerolls}!")

        dropped=0
        if advantage==True or drop==True:
            rolls.sort()
            dropped=rolls.pop(0)
        elif advantage==False or drop==False:
            rolls.sort()
            dropped=rolls.pop()      
        if dropped>0:    
            print(f"\n'{dropped}' dropped")
            
        total=sum(rolls)

        
        if bonus_str:

            bonus_operator = bonus_str[0]
            bonus_value = int(bonus_str[1:])
            
            if bonus_operator == '+':
                total += bonus_value
            elif bonus_operator == '-':
                total -= -bonus_value
            elif bonus_operator == '*':
                total *= bonus_value
            elif bonus_operator == '/':
                total //= bonus_value
            else:
                raise ValueError("Invalid bonus operator: " + dice_expression)
            return total
        else:
            return total
    while True:
        dice_expression=dice_choice()
        pattern = re.compile(r'(\d+)?d(\d+)([*\/+-]\d+)?')
        dice_expression_clean=re.sub(r"\s+", "", dice_expression)
        matches = pattern.findall(dice_expression_clean)
        total=0
        if matches:
            advantage, explode, drop, reroll, pen=options()

            for match in matches:
                num_dice_str = match[0]
                num_dice = int(num_dice_str) if num_dice_str else 1
                if advantage is not None:
                    num_dice=2
                dice_faces = int(match[1])    
                bonus_str = match[2]

                subtotal=roller(num_dice, dice_faces, bonus_str, explode, advantage, drop, reroll, pen)
                total+=subtotal
            print(f"\nTotal: {total}\n")
            return total
        else: print(f"\nInvalid dice expression: {dice_expression}\nTry expressions like: {randint(1, 10)}d{choice([4, 6, 8, 10, 12, 20])} {choice(['+', '-', '/', '*'])}{randint(1, 10)}\n")
    
def options():
    advantage=None
    explode=False
    drop=None
    reroll=False
    pen=False
    adv_dis=input("(a)dvantage? (d)isadvantage? (e)xploding? Drop (l)owest? Drop (h)ighest? (r)e-roll 1s? (p)enetrating? [enter to skip]: ").lower().strip()
    if adv_dis=="a":
        advantage=True
    elif adv_dis=="d":
        advantage=False
    elif adv_dis=="e":
        explode=True
    elif adv_dis=="l":
        drop=True
    elif adv_dis=="h":
        drop=False
    elif adv_dis=="r":
        reroll=True
    elif adv_dis=="p":
        pen=True
    
    return advantage, explode, drop, reroll, pen
while True:
    roll_dice()