from random import choice

chars = "abcdefghijklmnopqrstuvwxyz"
vocal = "aeiou"
n_vocal = "bcdfghjklmnpqrstvwxyz"
length = None

times = 100
timeout = 20
result = set({})
pattern_matching = []
breakword = None

def match_word(word: str, match_pattern: tuple=(n_vocal,vocal,n_vocal,vocal)):
    for index, token in enumerate(match_pattern):
        if word[index] not in token:
            return False
    return True

def init():
    global length, times, timeout, breakword
    length = input("Enter the word length: ")
    try:length = int(length)
    except ValueError:
        print("Invalid input. Required number (0123456789)+")
        exit(1)
    times = input("How many words should the engine search?: ")
    try:times = int(times)
    except ValueError:
        print("Invalid input. Required number (0123456789)+")
        exit(1)
    if times > 9999:
        print(f"Warning: times above 9999. Engine may use a lot of memory(storing the possible words)")
    print("Enter Pattern Matching")
    print("enter VOCAL for vocal letter")
    print("enter N_VOCAL for non-vocal letter")
    print("enter ALL for all letter")
    print("enter any letter if you want your own letters")
    print("Example: N_VOCAL VOCAL st sl\n\t Possible Word: Natl")
    i = 0
    while True:
        if i > length-1:
            break
        p = input(f"Pattern({i+1}): ").lower()
        if p:
            if p == "n_vocal":
                pattern_matching.append(n_vocal)
            elif p == "vocal":
                pattern_matching.append(vocal)
            elif p == "all":
                pattern_matching.append(chars)
            else:
                if not p.isalpha():
                    print(f"Invalid character ({p}); Only allowed [a-z]")
                    exit(-1)
                pattern_matching.append(p)
        else:
            continue
        i += 1
    print("Your pattern matching: ",pattern_matching)
    print("\nTimeout is the maximum of comparing the generate word with word pattern")
    print("This can be used to prevent endless loop because there's a chance that all possible words left")
    print("is none and the engine keep searching the possible words although there's none")
    print("Not recommend to set it to 0 if your word has low possible words")
    print("Note: if you don't get any result, try increase the value but it may make the engine bit slow")
    print("Eg: word length: 1, pattern matching: a")
    timeout = input("Timeout(default: 20): ")
    if timeout:
        try:timeout = int(timeout)
        except ValueError:
            print("Invalid input. Required number (0123456789)+")
            exit(1)
    else:
        timeout = 20
    print("breakword: Engine will stop searching after found this word")
    print("leave it empty if you don't want a breakword")
    breakword = input("Enter breakword: ")
    if breakword:
        breakword = breakword.lower()
        if not breakword.isalpha():
            print("Word can only contain [a-z]")
            exit(-1)
        if not match_word(breakword, pattern_matching):
            print("Word must meet the pattern matching rules")
            exit(-1)
        breakword = breakword.capitalize()
    else:
        breakword = None

try:
    init()
except KeyboardInterrupt:
    print("\nExit")
    exit(0)

def out():
    print("\nDONE!")
    exit(0)

print("SEARCHING...\n")
while True:
    try:
        for _ in range(times):
            check_time = 1
            while True:
                if check_time == timeout:
                    out()
                word = "".join((choice(chars) for i in range(length)))
                if word in result:
                    check_time += 1
                    continue
                if not match_word(word, pattern_matching):
                    check_time += 1
                    continue
                result.add(word)
                if len(word) >= 3:
                    word = word.capitalize()
                print(f"{_+1}."+word)
                if word == breakword:
                    out()
                break
        break
    except KeyboardInterrupt:
        break

out()