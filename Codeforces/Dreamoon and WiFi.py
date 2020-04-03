def fac(n):
    if n == 0:
        return 1
    return n * fac(n-1)

def comb(n, r):
    return fac(n) / (fac(n-r)*fac(r))

orig_s = input()
s = input()
intended = orig_s.count("+") - orig_s.count("-")
our_final_pos = s.count("+") - s.count("-") 
if s.count("?") == 0:
    if s.count("+") - s.count("-") == intended:
        print(1)
    else:
        print(0)
else:
    num_of_question = s.count("?")
    n_s = 2**num_of_question
    df = abs(intended - our_final_pos)
    if df > num_of_question:
        print(0)
    else:
        x = (num_of_question - df)//2
        print(comb(num_of_question, x+df) / n_s)