
import random
import requests

def main():
    words, wordl = secret()
    max_guesses = 10
    guesses = max_guesses
    while guesses > 0:
        answer=guess(words)
        guesses -= 1
        flag=validate_guess(wordl,max_guesses,guesses,answer)
        if flag:
            break
    else:
        print(f"🟥 You have reached the maximum number of guesses the word was {wordl}")

def secret():
    response = requests.get("https://darkermango.github.io/5-Letter-words/words.json")

    words = []
    response = response.json()
    lst = response["words"]
    words.extend(lst)

    wordl = random.choice(words)
    return words, wordl
def guess(words):
    while True:
        ans = input("Enter your guess: ").strip().lower()
        if len(ans) > 5:
            print("Your guess is too long (5 letters only)")
        elif len(ans) < 5:
            print("Your guess is too short (5 letters only)")
        elif ans not in words:
            print("Your guess is not in the list of words!")
        else:
            return ans
def validate_guess(wordl,max_guesses,guesses,answer):
    word_ = list(wordl)
    ans_ = list(answer)
    feedback = [""] * 5
    if ans_ == word_:
        print(f"🟩 Your guess is correct: {wordl} You guessed it in {max_guesses - guesses} guess(es)!")
        flag = True
    else:
        i = 0
        wrdCopy = word_.copy()
        greenPos = []
        while i < len(word_):
            if ans_[i] == word_[i]:
                feedback[i] = "🟩"
                greenPos.append(i)
                wrdCopy.remove(ans_[i])
            i += 1
        i = 0
        while i < len(word_):
            if i in greenPos:
                i += 1
            else:
                if ans_[i] in wrdCopy:
                    feedback[i] = "🟨"
                    wrdCopy.remove(ans_[i])
                    i += 1
                else:
                    feedback[i] = "🟥"
                    i += 1

        print("".join(feedback))
        if guesses > 0:
            print(f"⬜ Wrong answer! Try again. You have {guesses} guess(es) left! ")
        flag = False
    return flag

main()