import concurrent.futures
import time


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def check_prime_numbers(nums):
    counter = 0

    for num in nums:
        if num == 2 or (num > 2 and is_prime(num)):
            counter += 1

    return counter


def run_future(_executor, name, _nums):
    start_time = time.time()
    future = _executor.submit(check_prime_numbers, _nums)
    result = future.result()
    time.sleep(2)
    end_time = time.time()

    total_count = result

    ex_time = round(end_time - start_time, 4)
    print(f"{name}: {ex_time} секунд")
    print(f"Кількість проcтих чисел: {total_count}")
    return ex_time


if __name__ == "__main__":
    num_list = list(range(1, 1000000))

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        threading_time = run_future(executor, "Thread", num_list)

    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
        process_time = run_future(executor, "Process", num_list)

    if threading_time < process_time:
        print(f"Thread швидше на: {abs(threading_time - process_time)}")
    else:
        print(f"Process швидше на: {abs(process_time - threading_time)}")
