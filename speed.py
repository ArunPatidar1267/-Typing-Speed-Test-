import time
import random

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a great programming language to learn.",
    "Typing speed can be improved with regular practice.",
    "Debugging code is like solving a puzzle.",
    "Consistency is more important than perfection."
]

def typing_test():
    print("------ Typing Speed Test ------")
    input("Press Enter to start...")

    test_sentence = random.choice(sentences)
    print("\nType this:\n")
    print(test_sentence)
    print("\n")

    start_time = time.time()
    typed_sentence = input("Start typing here:\n")
    end_time = time.time()

    time_taken = end_time - start_time
    time_taken = round(time_taken, 2)

    word_count = len(typed_sentence.split())
    wpm = round(word_count / (time_taken / 60), 2)

    original_words = test_sentence.split()
    typed_words = typed_sentence.split()
    correct_words = sum(1 for o, t in zip(original_words, typed_words) if o == t)
    accuracy = round((correct_words / len(original_words)) * 100, 2)

    print("\n------ Results ------")
    print(f"Time Taken: {time_taken} seconds")
    print(f"Your Speed: {wpm} WPM")
    print(f"Accuracy: {accuracy}%")

typing_test()
