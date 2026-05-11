import sys


def display_menu():
    print("\n" + "=" * 60)
    print(" " * 15 + "MAZE ALGORITHMS PROJECT")
    print("=" * 60)
    print("\nSelect a problem to execute:")
    print("  [1] Problem 1 - Maze Generation (Kruskal & Prim)")
    print("  [2] Problem 2 - Solve 60x80 Maze (BFS & A*)")
    print("  [3] Problem 3 - Algorithm Comparison (25 mazes)")
    print("  [4] Run All Problems")
    print("  [0] Exit")
    print("=" * 60)


def run_problem1():
    import problem1
    problem1.main()


def run_problem2():
    import problem2
    problem2.main()


def run_problem3():
    import problem3
    problem3.main()


def run_all_problems():
    print("\n" + "=" * 60)
    print("Running all problems sequentially...")
    print("=" * 60)
    run_problem1()
    run_problem2()
    run_problem3()
    print("\n" + "=" * 60)
    print("All problems completed!")
    print("=" * 60)


def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            run_problem1()
        elif choice == "2":
            run_problem2()
        elif choice == "3":
            run_problem3()
        elif choice == "4":
            run_all_problems()
        elif choice == "0":
            print("\nExiting program. Goodbye!")
            sys.exit(0)
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
