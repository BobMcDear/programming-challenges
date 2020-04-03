def has_upper(s):
    for i in s:
        if i.isupper():
            return True
    return False

def is_pretty(s):
    if has_upper(s):
        return False
    return True

def get_all_substrings(s):
  length = len(s)
  return [s[i:j+1] for i in range(length) for j in range(i,length)]

n = int(input())
s = input()
len_of_all_pretty = [0]
subs = get_all_substrings(s)
for i in subs:
    if is_pretty(i):
        len_of_all_pretty.append(len(set(i)))
print(max(len_of_all_pretty))