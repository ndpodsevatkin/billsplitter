import random

print('Enter the number of friends joining (including you): ')
n_people = int(input())

if n_people <= 0:
    print("No one is joining for the party")
else:
    print('Enter the name of every friend (including you), each on a new line: ')
    names = [input() for _ in range(n_people)]
    bill = int(input('Enter the total bill value:\n'))
    is_lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if is_lucky == 'Yes':
        lucky_person = random.choice(names)
        print(f"{lucky_person} is the lucky one!")
        final_bill = round(bill / (len(names) - 1), 2)
        friends_bills = {key: final_bill for key in names}
        friends_bills[lucky_person] = 0
        print(friends_bills)
    elif is_lucky == 'No':
        print('No one is going to be lucky')
        final_bill = round(bill / len(names), 2)
        friends_bills = {key: final_bill for key in names}
        print(friends_bills)

