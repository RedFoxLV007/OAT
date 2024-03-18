# CLI - Command line interface
# ----------------------------------------------------------------#

money = input("Enter money: ")


while True:
    command = input("""
    1. add money 100
    2. spend money 100
    3. print balance
    4. exit
    """)
    if command == "4":
        break
    if command == "1":
        pass
    if command == "2":
        pass
    if command == "3":
        print(money)