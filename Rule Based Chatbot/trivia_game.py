import random #module for generating random variables
import time #module used here for time delay

def load_qs(filename=r"trivia_questions.txt"):
    questions = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split("|")
                    if len(parts) == 4:
                        category, question, options, correct_answer = parts
                        questions.append({
                            "category": category.lower(),
                            "question": question,
                            "options": options.split(", "),
                            "correct_answer": correct_answer.strip().upper(),
                        })
                    else:
                        print(f"Skipping invalid line: {line}")
        if not questions:
            print(f"Error: No valid questions found in {filename}.")
            return []

#Exception Handliing
    except FileNotFoundError:
        print(f"Error: File not found: {filename}")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []
    return questions

#Categorising trivia question

def get_available_categories(questions):
    return sorted(set(q["category"] for q in questions))


def choose_category(categories):
    print("Available categories:")
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat.title()}")
    while True:
        choice = input("Choose a category by number: ").strip()
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(categories):
                return categories[choice - 1]
        print("Invalid choice. Please enter a valid number.")


def display_qs(qs_data):
    print("\n" + qs_data["question"])
    for option in qs_data["options"]:
        print(option)


def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer


def display_feedback(is_correct):
    if is_correct:
        print("Correct!")
    else:
        print("Incorrect.")


def calculate_score(correct_answers, total_questions):
    if total_questions == 0:
        return 0.0
    return (correct_answers / total_questions) * 100


def display_score(score):
    print(f"\nYour current score is: {score:.2f}%")

#Replaying trivia game

def ask_retry():
    while True:
        retry = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if retry in ["yes", "y"]:
            return True
        elif retry in ["no", "n"]:
            return False
        else:
            print("Please enter yes or no.")

#Trivia Game Code block

def play_trivia_game():
    questions = load_qs()
    if not questions:
        print("No questions to play. Exiting.")
        return

    while True:
        categories = get_available_categories(questions)
        selected_category = choose_category(categories)
        filtered_questions = [q for q in questions if q["category"] == selected_category]

        if not filtered_questions:
            print(f"No questions found for category '{selected_category}'.")
            continue

        correct_answers = 0
        total_questions = 0
        asked_questions = set()

        print(f"\n🎮 Starting Trivia: Category - {selected_category.title()}")
        print("Type 'exit' anytime to quit and see your score.\n")

        while True:
            remaining_qs = [q for q in filtered_questions if q["question"] not in asked_questions]
            if not remaining_qs:
                print("\nYou've answered all questions in this category!")
                break

            qs_data = random.choice(remaining_qs)
            asked_questions.add(qs_data["question"])

            display_qs(qs_data)
            user_answer = input("Your answer (A, B, C, D or 'exit'): ").strip().upper()

            if user_answer == "EXIT":
                print("\nYou chose to exit the game early.")
                score = calculate_score(correct_answers, total_questions)
                display_score(score)
                print("Thanks for playing!")
                return

            if user_answer not in ["A", "B", "C", "D"]:
                print("Invalid input. Please enter A, B, C, D or 'exit'.")
                continue

            is_correct = check_answer(user_answer, qs_data["correct_answer"])
            display_feedback(is_correct)

            if is_correct:
                correct_answers += 1
            total_questions += 1
            time.sleep(1.5)

        score = calculate_score(correct_answers, total_questions)
        display_score(score)

        if not ask_retry():
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    play_trivia_game()