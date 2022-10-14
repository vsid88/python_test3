def upperlower():
    sent = input('provide sentence')
    upper_case = 0
    lower_case = 0
    for letters in sent:
        if (letters.islower()):
            lower_case = lower_case + 1
        elif (letters.isupper()):
            upper_case = upper_case + 1
    print(f'{lower_case} - lower case occurrences')
    print(f'{upper_case} - upper case occurences')
upperlower()
