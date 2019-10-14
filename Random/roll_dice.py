# https://leetcode.com/discuss/interview-question/331158/Amazon-or-Online-Assessment-2019-or-Roll-Dice
def roll_dice(arr) -> int:
    count = [0]*7
    for i in arr:
        count[i] += 1

    min_turns = float('inf')
    for i in range(1, 6):
        # print(2*count[7-i] + len(arr) - count[i] - count[7-i])
        min_turns = min(
            min_turns, 2*count[7-i] + len(arr) - count[i] - count[7-i])

    return min_turns


assert roll_dice([1, 1, 6]) == 2
assert roll_dice([1, 2, 3]) == 2
assert roll_dice([1, 6, 2, 3]) == 3
