def feedback(student, *comments):
    print(f"Feedback for {student}:")
    for comment in comments:
        print("-", comment)

feedback("Alice", "Good structure", "Clear variable names")
feedback("Bob", "Needs comments", "Incorrect loop condition", "Late submission")
