# dice-roller
Simple dice roller that can parse expressions like "1d4-1"
# Options!

<b>Advantage/disadvantage:</b><p>
Number of dice defaults to 2, no matter the input; e.g.: "d20" will be parsed as 2d20, but also "6d6+5" with advantage will take the highest result of 2d6 and add 5.

<b>Exploding dice:</b><p>
When the maximum value of a die is rolled, it performs an additional roll (which can also trigger additional rolls).

<b>Drop lowest/highest:</b><p>
The stated number of dice will be rolled and the lowest or highest value will be removed before being summed, before bonuses are operated. This function only removes a single die. If only 1 die is thrown, its result will be removed and bonus will operate on 0.

<b>Reroll 1s:</b><p>
For every "1" result, the result is removed and the dice rolled again (which can trigger subsequent removal of "1" and rerolls). This option will never count a "1" result.

<b>Penetrating dice:</b><p>
Similar to exploding dice, but the explosion result has a -1 modifier before summing. Maximum value results can still trigger penetrations, they are just summed as maximum-1.

<b>Bonus operators:</b><p>
Bonuses can now use "+", "-", "/", and "*" operators, and act on the summed total of dice results.

<b>Coming soon:</b><p>
Mixed dice!
