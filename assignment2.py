import sys
word = sys.argv[1]
L = []
K = []
P = []
guess_right = 5
for i in range(1, int(len(word)+1)):
    L.append('-')
kelimenin_listesi = list(word)
letter = sys.argv[2].split(',')
print("\nYou have {} guesses left".format(guess_right))
print(L)
print("--------------------------------------------")
IN_mode = 1
OUT_mode = 2
t = IN_mode
for harf in letter:
        if t == IN_mode:
            if harf in word and harf not in K:
                K.append(harf)
                for j, value in enumerate(kelimenin_listesi):
                    if value == harf:
                        L[j] = value
                print("Guessed word: {} You are in IN mode".format(harf))
                print('You have {} guesses left'.format(guess_right))
                print(list(L))
                print("--------------------------------------------")
            elif harf not in word or harf in K:
                if harf not in K:
                    K.append(harf)
                    guess_right = guess_right - 1
                    print("Guessed word: {} The game turned into OUT mode".format(harf))
                    print('You have {} guesses left'.format(guess_right))
                    print(L)
                    print("--------------------------------------------")
                    t = OUT_mode
                else:
                    K.append(harf)
                    print("Guessed word: {} is used in IN mode. The game turned into OUT mode".format(harf))
                    guess_right = guess_right - 1
                    print('You have {} guesses left'.format(guess_right))
                    print(L)
                    print("--------------------------------------------")
                    t = OUT_mode
        else:
            if harf not in word and harf not in P:
                P.append(harf)
                print("Guessed word: {} The game turned into IN mode".format(harf))
                print('You have {} guesses left'.format(guess_right))
                print(L)
                print("--------------------------------------------")
                t = IN_mode

            else:
                P.append(harf)
                guess_right = guess_right - 1
                print("Guessed word: {} You are in OUT mode".format(harf))
                print('You have {} guesses left'.format(guess_right))
                print(L)
                print("--------------------------------------------")
                t = OUT_mode
        if guess_right > 0 and L == kelimenin_listesi:
                    print()
                    print("You won the game")
                    break
        if guess_right <= 0 and letter != K:
                    print()
                    print("You lost the game")
                    break
        if guess_right > 0 and letter == K+P and L != kelimenin_listesi:
                    print()
                    print("You finished all letters")
                    print("You lost the game")
                    break