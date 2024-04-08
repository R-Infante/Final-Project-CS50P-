"""

- Financial Responsibility Program

- Your personal Budget Advisor

"""

import sys
import time
from tabulate import tabulate


Y, YR, G, GR = "\033[93m", "\033[0m", "\033[32m", "\033[0m"

currency, salary, c_sign = None, None, None


def main():
    """
    Main function to start the program and welcome user

    """
    global currency, salary, c_sign

    print(
        "\n"
        + "_" * 71
        + "\n\n\nWelcome to your Financial Responsibility Program!"
        + "\n\nIf you are here, it means you want to get your personal finances right!"
        )

    while True:
        try:
            y_n = input(f"\n{Y}Are you ready? (Y/N) {YR}").lower().strip()

            if y_n == "y":
                print("\n" + "_" * 22 + "\n")
                currency, salary, c_sign = currency_salary(currency, salary, c_sign)
                print(currency, salary, c_sign)
                main_menu()
            elif y_n == "n":
                sys.exit(
                    "\n"
                    + "_" * 40
                    + "\n\nCome back anytime! Hope to see you soon!\n"
                    + "_" * 40 + "\n\n"
                    )
            else:
                continue
        except EOFError:
            sys.exit("\n\n")


def currency_salary(c, s, cs):
    """
    This function will ask the user for its salary and preferred currency
    It will also assign the correct fiat symbol to the chosen currency
    This will then assign values to global variables

    """
    while True:
        c = (input(
            '\nBefore we start, let us know what currency would you like us to display values in:'
            f'{Y}(Type "EUR" or "USD" or "GBP") {YR}')
            .lower().strip())

        if c in ["eur", "usd", "gbp"]:
            c_symbols = {"eur": "€", "usd": "$", "gbp": "£"}

            while True:
                try:
                    s = int(input(
                        "\nAlso, in order to calculate the best budget allocation for you,"
                        f"{Y} what is your monthly salary? {YR}")
                        )
                    if isinstance(s, int):
                        cs = c_symbols.get(c.lower())
                        return (c, s, cs)
                except ValueError:
                    continue
        else:
            continue


def main_menu():
    """
    This is the main menu

    """
    main_menu_header = [["Main Menu"]]
    main_menu_table = tabulate(main_menu_header, tablefmt="mixed_grid")

    menu = [
        ["Option", "Description"],
        [1, "Budget | 50-30-20 Rule"],
        [2, "Savings Plan"],
        [3, "Exit"],]

    menu_table = tabulate(menu, headers="firstrow", tablefmt="mixed_grid", numalign="center")

    print(f"\n\n{main_menu_table}")

    print(f"\n{menu_table}\n\n")
    print("What would you like to do?")

    while True:
        try:
            choice = int(input(f"\n{Y}Choose an option from the menu above: {YR}"))

            if choice == 1:
                print(
                    "\n" + "_" * 80
                    + "\n\n"
                    "Creating a budget can help you make confident decisions "
                    "and enjoy peace of mind."
                    "\n" + "_" * 80 + "\n")

                time.sleep(1)
                print(
                    "\nIn brief:"
                    "\n\nUnderstanding your spending can help you better plan for the future."
                    "\nThe 50-30-20 rule organizes spending into needs, wants, and savings."
                    )

                time.sleep(2)
                budget_menu()

            elif choice == 2:
                savings_plan()

            elif choice == 3:
                sys.exit(
                    "\n" + "_" * 40
                    + "\n\nCome back anytime! Hope to see you soon!\n"
                    + "_" * 40 + "\n\n")

        except ValueError:
            continue


def budget_menu():
    """
    This is the budget menu

    """
    budget_menu_header = [["Budget Menu"]]
    budget_menu_header_table = tabulate(budget_menu_header, tablefmt="mixed_grid")

    budget_menu_data = [
        ["Option ", "Description"],
        [1, "50 | Needs"],
        [2, "30 | Wants"],
        [3, "20 | Savings"],
        [4, "Main menu"],]

    budget_menu_table = tabulate(budget_menu_data,
                                 headers="firstrow",
                                 tablefmt="mixed_grid",
                                 numalign="center",
                                 )

    print(f"\n\n{budget_menu_header_table}")
    print(f"\n{budget_menu_table}\n\n")
    print("What would you like to check?")

    while True:
        try:
            choice = int(input(f"\n{Y}Choose an option from the menu above: {YR}"))

            if choice == 1:
                needs()
            elif choice == 2:
                wants()
            elif choice == 3:
                savings()
            elif choice == 4:
                main_menu()

        except ValueError:
            continue


def back_menu():
    """
    This is the going back menu

    """
    back_menu_data = [
        ["Option ", "Description"],
        [1, "Main Menu"],
        [2, "Budget Menu"],
        [3, "Exit"]]

    back_menu_table = tabulate(back_menu_data,
                               headers="firstrow",
                               tablefmt="mixed_grid",
                               numalign="center",
                               )

    print(f"\n{back_menu_table}\n")

    while True:
        try:

            back_decision = int(input(f"\n{Y}Where to next? {YR}"))

            if back_decision == 1:
                main_menu()
            elif back_decision == 2:
                budget_menu()
            elif back_decision == 3:
                sys.exit(
                    "\n" + "_" * 40 + "\n\n"
                    "Come back anytime! Hope to see you soon!"
                    "\n" + "_" * 40 + "\n\n"
                    )

        except ValueError:
            continue


def needs():
    """
    Calculates the needs budget allocation

    """
    needs_budget = salary * 0.5

    print("\n" + "_" * 39 + "\n\n\n"
          "NEEDS: 50%\n\n"
          "About half of your budget should go toward needs. "
          "These are expenses that must be met no matter what, such as:"
          "\n\n- Rent or mortgage payments"
          "\n- Utility bills"
          "\n- Groceries"
          "\n- Health care"
          "\n- Minimum debt payments"
          "\n\nIf you can honestly say “I can’t live without it”, you have identified a need."
          "\nMinimum required payments on a credit card or a loan also belong in this category."
          "\n"
          )

    print('So, how much should you spend in this "needs" category? '
          f"Around {G}{needs_budget:.0f}{c_sign}{GR}.\n"
          )

    while True:
        try:
            next_step = (input(
                f"\n{Y}Should we dive deeper into each item allocation? (Y/N) {YR}"
                ).lower().strip())

            if next_step == "y":

                print("\n" + "_" * 56 + "\n")
                print(
                    '\nAccording to experts, here is a more detailed outlook '
                    'of how much you should spend in each item of the "needs" category:')

                needs_table_detail = tabulate([
                    ["Expense", "%", "Amount"],
                    ["Rent", 50, f"{needs_budget * 0.5:.0f} {c_sign}"],
                    ["Utility Bills", 15, f"{needs_budget * 0.15:.0f} {c_sign}"],
                    ["Groceries", 25, f"{needs_budget * 0.25:.0f} {c_sign}"],
                    ["Health / Loan", 10, f"{needs_budget * 0.10:.0f} {c_sign}"],],
                    headers="firstrow",tablefmt="mixed_grid",numalign="center",)

                print(f" \n\n{needs_table_detail}\n\n")

                print(
                    'Remember, you should adjust percentage allocation to your particular needs!'
                    '\n\n'
                    'Percentages are attributed to your "needs" budget, not your overall salary.'
                    '\n')

                time.sleep(10)
                print("_" * 76 + "\n")
                back_menu()

            elif next_step == "n":
                print("\n" + "_" * 56)
                budget_menu()

        except ValueError:
            continue


def wants():
    """
    Calculates the wants budget allocation

    """
    wants_budget = salary * 0.3

    print("\n" + "_" * 39 + "\n\n\n"
          "WANTS: 30%\n\n"
          "You subscribe to a streaming service to watch your favorite show, "
          "not because you need the subscription to live.\n"
          "Wants are things you enjoy that you spend money on by choice, such as:"
          "\n\n"
          "- Subscriptions\n- Hobbies \n- Restaurant meals\n- Vacations"
          "\n\n"
          "Basically, wants are all those little extras you spend money on,"
          " that make life more enjoyable and entertaining."
          "\n")

    print(
        'So, how much should you spend in this "wants" category? '
        f'Around {G}{wants_budget:.0f}{c_sign}{GR}.'
        '\n')

    while True:
        try:
            next_step = input(
                f"\n{Y}Should we dive deeper into each item allocation? (Y/N) {YR}"
                ).lower().strip()

            if next_step == "y":

                print("\n" + "_" * 56 + "\n\n"
                      'According to experts, here is a more detailed outlook of '
                      'how much you should spend in each item of the "wants" category:')


                wants_table_detail = tabulate([
                        ["Expense", "%", "Amount"],
                        ["Subscription", 10, f"{wants_budget * 0.10:.0f} {c_sign}"],
                        ["Hobbies", 20, f"{wants_budget * 0.2:.0f} {c_sign}"],
                        ["Restaurant meals", 10, f"{wants_budget * 0.1:.0f} {c_sign}"],
                        ["Vacations", 60, f"{wants_budget * 0.6:.0f} {c_sign}"],],
                        headers="firstrow",tablefmt="mixed_grid",numalign="center",)

                print(f" \n\n{wants_table_detail}\n\n")

                print(
                    'Remember, you should adjust percentage allocation to your particular wants!'
                    '\n\n'
                    'Percentages are attributed to your "wants" budget, not your overall salary.'
                    '\n')

                time.sleep(10)
                print("_" * 76 + "\n")
                back_menu()

            elif next_step == "n":
                print("\n" + "_" * 56)
                budget_menu()

        except ValueError:
            continue


def savings():
    """
    Calculates the savings budget allocation

    """
    savings_budget = salary * 0.3

    print(
        "\n" + "_" * 39 + "\n\n\n"
        'SAVINGS: 20%'
        '\n\n'
        f'The remaining 20% of your budget should go toward the future.'
        '\n'
        'You may put money in an emergency fund, contribute to a retirement account, '
        'or save toward a down payment on a home.'
        '\n'
        'Paying down debt beyond the minimum payment amount belongs in this category, too.'
        '\n')

    print(
        'So, how much should you spend in this "savings" category? '
        f'Around {G}{savings_budget:.0f}{c_sign}{GR}.'
        '\n')

    while True:
        try:
            next_step = input(
                "\n"
                f"{Y}Should we dive deeper into how to create a savings plan? "
                f"(Y/N) {YR}"
                ).lower().strip()

            if next_step == "y":
                savings_plan()

            elif next_step == "n":
                print("\n" + "_" * 64)
                budget_menu()

        except ValueError:
            continue


def savings_plan():
    """
    Savings plan asks the user if he has debt,
    if he has 6 months of income saved,
    and how much he has saved.

    It then calculates the user's emergency fund amount,
    and creates a progress bar towards its goal.

    """

    while True:
        try:
            user_debt = input(
                f"\n{Y}Before we dive in, let me ask you, do you have any debt? (Y/N) {YR}"
                ).lower().strip()

            if user_debt == "y":

                print("\n\n"
                      "Paying off your whole debt should be your number one priority!"
                      "\n"
                      "Make sure to clear all debt in your name before considering "
                      "any investments or savings plan."
                      "\n")

                time.sleep(6)
                print("_" * 92 + "\n")
                back_menu()

            elif user_debt == "n":

                e_fund = salary * 6

                print("\n\n"
                      "That's great! "
                      "It means you can think about saving and investing for the future!"
                      "\n\n"
                      "The term “emergency fund” refers to money stashed away "
                      "that people can use in times of financial distress."
                      "\n"
                      "The purpose of an emergency fund is to improve financial security "
                      "by creating a safety net that can be used "
                      "to meet unanticipated expenses, such as an illness or layoffs."
                      "\n")

                print(
                    "Normally an emergency fund should have at least 6 months "
                    "of your current income saved up, which in your case would be "
                    f"{G}{e_fund:.0f}{c_sign}{GR}."
                    "\n")

                s_emergency_fund()

        except ValueError:
            continue


def s_emergency_fund():
    """
    This function asks if the user has 6 months
    of income saved aside, and if not will
    guide the user to s_progress_bar function

    """

    while True:
        try:
            e_f = input(
                "\n"
                f"{Y}Do you have at least 6 months of income saved? "
                f"(Y/N) {YR}"
                ).lower().strip()

            if e_f == "y":

                print(
                    "\n\n"
                    "That is great, it appears you have everything in order!"
                    "\n"
                    "You can now think about investing into assets "
                    "that will grow your wealth overtime!"
                    "\n")

                time.sleep(5)
                print("_" * 82 + "\n")
                back_menu()

            elif e_f == "n":
                print()
                s_progress_bar()

        except ValueError:
            continue


def s_progress_bar():
    """
    This function asks how much the user has saved
    and calculates the progress towards the emergency fund.

    """
    e_fund = salary * 6

    while True:
        try:
            saved_input = input(f"\n{Y}How much do you have saved up? {YR}")
            s_amount = int("".join(filter(str.isdigit, saved_input)))
            goal = e_fund - s_amount

            if s_amount <= e_fund:
                print(
                    "\n\n"
                    "Calculating your progress towards the emergency fund..."
                    "\n\n")
                time.sleep(1)

                progress_bar_length = 50
                progress = min(s_amount / e_fund, 1)

                for i in range(int(progress * 50) + 1):
                    current_progress = i / 50
                    filled_length = int(current_progress * progress_bar_length)
                    empty_length = progress_bar_length - filled_length
                    progress_percentage = current_progress * 100
                    progress_bar = "|" + f"{G}█{GR}" * filled_length + "-" * empty_length + "|"
                    progress_info = f" {s_amount} / {G}{e_fund:.0f} {c_sign}{GR}".format(s_amount, e_fund)

                    print(
                        "\rProgress: {:.0f}% {} {}".format(
                        progress_percentage, progress_bar, progress_info,),
                        end="", flush=True,
                        )

                    time.sleep(0.15)

                time.sleep(1)

                print(
                    "\n\n\n"
                    "Great job! "
                    f"You are only {goal}{c_sign} away from your goal! "
                    "Stay focused!"
                    )

                time.sleep(3)
                print("\n\n" + "_" * 29 + "\n")
                back_menu()
            else:
                print(
                    "\nYou gave a value that is higher than "
                    "6 months of income.\n")
                s_emergency_fund()


        except ValueError:
            continue


if __name__ == "__main__":
    main()
