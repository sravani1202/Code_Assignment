def main():
    num_of_testcases= int(input())

    for i in range(num_of_testcases):
        num_of_integers = int(input())
        list_of_integers= list(map(int, input().split()))

        best_case = float('inf')  # Initializing to positive infinity
        worst_case = float('-inf')  # Initializing to negative infinity

        for i in range(num_of_integers):
            #left side person infected 
            left = i
            while left > 0 and abs(list_of_integers[left] - list_of_integers[left - 1]) <= 2:
                left -= 1
            #right side person infected
            right = i
            while right < num_of_integers- 1 and abs(list_of_integers[right] - list_of_integers[right + 1]) <= 2:
                right += 1

            infected_count = right - left + 1
            best_case = min(best_case, infected_count)
            worst_case = max(worst_case, infected_count)

        print(best_case, worst_case)

if __name__ == "__main__":
    main()

