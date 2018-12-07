print("Programmed by Ethan Nadzieja, CS-118 Lesson Set 4\n\nProblem 1.\n")
cr = int(0)
qc = int(0)
questions = ("1. What is the capital of Alabama?", "2. What is the capital of Iowa?", "What is the Capital of Missouri?", "What is the capital of Vermont?", "What is the capital of South Dakota?");
responses = ("\n\tA. Sacremento\n\tB. Trenton\n\tC. Lansing\n\tD. Montgomery", "\n\tA. Des Moines\n\tB. Jackson\n\tC. Concord\n\tD. Boise", "\n\tA. Jefferson City\n\tB. Raleigh\n\tC. Charleston\n\tD. Little Rock", "\n\tA. Montplier\n\tB. Cheyenne\n\tC. Indianapolis\n\tD. Des Moines", "\n\tA. Honolulu\n\tB. Denver\n\tC. Oklahoma City\n\tD. Pierre")
answers = ("d", "a", "a", "a", "d")
for x in questions:
    print(questions[qc])
    print(responses[qc])
    a1 = input().lower()
    if a1 in answers[qc]:
        print("Correct!")
        cr = cr+1
        if qc < 4:
            qc = qc+1
    else:
        print("Incorrect, the correct answer is", answers[qc])
        if qc < 4:
            qc = qc+1
print("\nYour score was:", cr*20, "%")
