import random
import time 

MIN_VALUE = 2
MAX_VALUE = 12
operators = ["+", "-", "*"]
TOTAL_PROBLEMS = 10

def generate_problem():
    op = random.choice(operators)
    first = random.randint(MIN_VALUE, MAX_VALUE)
    second = random.randint(MIN_VALUE, MAX_VALUE)

    expr = str(first) + " " + op + " " + str(second)
    evalAnswer = eval(expr)
    return expr, evalAnswer

wrong = 0
input("Press Enter to Start")
print("-----------------------------------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input(f"Problem Number {i + 1} : {expr} = " )
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)
print(f"You finished in {total_time}")

print("-----------------------------------------------")
