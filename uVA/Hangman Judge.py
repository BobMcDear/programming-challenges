answers = []
while True:
    n = int(input())
    if n == -1:
        break
    ans = input()    
    guess = input()
    correct_guesses = 0
    fails = 0
    right_chrs = set()
    wrong_chrs = set()
    f = True
    for i in guess:
        if correct_guesses == len(ans):
            answers.append("Round {}\nYou win.".format(n))
            f = False
            break
        if fails == 7:
            answers.append("Round {}\nYou lose.".format(n))
            f = False
            break
        if i in ans and i not in right_chrs:
            right_chrs.add(i)
            correct_guesses += ans.count(i)
        if i not in ans and i not in wrong_chrs:
            fails += 1
            wrong_chrs.add(i)
    if correct_guesses == len(ans) and f:
        answers.append("Round {}\nYou win.".format(n))
        f = False
    if fails == 7 and f:
        answers.append("Round {}\nYou lose.".format(n))
        f = False
    if f:
        answers.append("Round {}\nYou chickened out.".format(n))

for i in answers:
    print(i)