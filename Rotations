def is_rotation(s1, s2):
    if len(s1) != len(s2) or len(s1) == 0:
        return False
    
    temp = s1 + s1
    if s2 in temp:
        return True
    else:
        return False

print(is_rotation("abcde", "cdeab"))
print(is_rotation("abcde", "abced"))
