"""
HW 4
Problem 3
Author: Vijay Kumar Kamsani
"""
import random

# Main function to run the program
if __name__ == '__main__':
    file = open('salary.txt', 'w')
    # Assigning the 3 ranks
    rank = ["assistant", "associate", "full"]
    # Using loop function assigning the firstname and lastname
    for i in range(1, 1001):
        file.write("FirstName" + str(i) + " ")
        file.write("LastName" + str(i) + " ")
        # Generating the random ranking using random keyword
        rank_i = random.choice(rank)
        file.write(rank_i + " ")
        # Assigning salary ranges to the ranking positions
        if rank_i == "assistant":
            sal = round(random.uniform(50000, 80000), 2)
        elif rank_i == "associate":
            sal = round(random.uniform(60000, 110000), 2)
        else:
            sal = round(random.uniform(75000, 130000), 2)
        file.write(str(sal) + "\n")
    file = open('salary.txt', 'r')
    # Initializing the ranking, salary,f_name and l_name
    assistant_total = 0
    assistant_count = 0
    associate_total = 0
    associate_count = 0
    full_total = 0
    full_count = 0
    total = 0
    count = 0
    for record in file:
        firstName, lastName, rank, sal = record.split()
        if rank == "assistant":
            assistant_total += float(sal)
            assistant_count += 1
            total += float(sal)
            count += 1
        elif rank == "associate":
            associate_total += float(sal)
            associate_count += 1
            total += float(sal)
            count += 1
        else:
            full_total += float(sal)
            full_count += 1
            total += float(sal)
            count += 1
    print(f'Assistant ( {assistant_count}): ${(assistant_total / assistant_count):,.2f}')
    print(f'Associate ( {associate_count}): ${(associate_total / associate_count):,.2f}')
    print(f'Full ( {full_count}): ${(full_total / full_count):,.2f}')
    print(f'All Faculty ( {count}): ${(total / count):,.2f}')
