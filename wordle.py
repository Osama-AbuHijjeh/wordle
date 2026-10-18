import random
import requests

response = requests.get(
    "https://darkermango.github.io/5-Letter-words/words.json"
)

words = []
response = response.json()
lst=response["words"]
words.extend(lst)

wordl = random.choice(words)

MAX_GUESSES = 10
guesses = MAX_GUESSES
while guesses > 0:
    feedback = [""] * 5
    ans = input("Enter your guess: ").strip().lower()
    if len(ans) > 5:
        print("Your guess is too long (5 letters only)")
        continue
    elif len(ans) < 5 :
        print("Your guess is too short (5 letters only)")
        continue
    elif ans not in words:
        print("Your guess is not in the list of words!")
        continue
    else:
        word_ = list(wordl)
        ans_ = list(ans)
        if ans_ == word_:
            guesses -= 1
            print(f"🟩 Your guess is correct: {wordl} You guessed it in {MAX_GUESSES-guesses} guess(es)!")
            break
        else:
            guesses -= 1
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

            if guesses == 0:
                print(f"🟥 You have reached the maximum number of guesses the word was {wordl}")
            else:
                print(f"⬜ Wrong answer! Try again. You have {guesses} guess(es) left! ")