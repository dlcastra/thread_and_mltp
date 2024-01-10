import concurrent.futures


def even_numbers(nums: int):
    even = [num for num in range(nums) if num % 2 == 0]
    print(even)


def odd_numbers(nums: int):
    even = [num for num in range(nums) if num % 2 != 0]
    print(even)


if __name__ == "__main__":
    nums_limit = 20

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        print_even = executor.submit(even_numbers, nums_limit)
        print_odd = executor.submit(odd_numbers, nums_limit)
