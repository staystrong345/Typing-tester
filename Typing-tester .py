import time
import random
def calculate_wpm(start_time, end_time, typed_text):
    time_taken = end_time - start_time
    minutes = time_taken / 60
    # Standard WPM calculation: (characters / 5) / minutes
    words_count = len(typed_text) / 5
    return round(words_count / minutes)

def calculate_accuracy(original, typed):
    original_words = original.split()
    typed_words = typed.split()
    correct_words = 0

    # Compare words one by one
    for o, t in zip(original_words, typed_words):
        if o == t:
            correct_words += 1

    accuracy = (correct_words / len(original_words)) * 100
    return round(accuracy, 2)

def run_test():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is an interpreted high-level general-purpose programming language.",
        "Smart energy systems are the future of Ethiopia's power grid.",
        "Hardware and software are two sides of the same coin."
    ]

    target_text = random.choice(sentences)

    print("\n--- Python Typing Tester ---")
    print("Type the following sentence exactly as it appears:")
    print(f"\nTarget: {target_text}\n")

    input("Press ENTER when you are ready to start...")

    start_time = time.time()
    user_input = input("\nStart Typing: ")
    end_time = time.time()

    # Results
    wpm = calculate_wpm(start_time, end_time, user_input)
    accuracy = calculate_accuracy(target_text, user_input)

    print("\n" + "-" * 30)
    print(f"Time Taken: {round(end_time - start_time, 2)} seconds")
    print(f"Your Speed: {wpm} WPM")
    print(f"Accuracy  : {accuracy}%")
    print("-" * 30)
if __name__ == "__main__":
    run_test()
