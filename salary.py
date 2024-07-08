def total_salary(path):
    dict = {}
    try:
        with open(path, "r", encoding="UTF-8") as f:

            salary_workers = [el.strip() for el in f.readlines()]
            print(salary_workers)
            list_workers_salary = [elem.split(",") for elem in salary_workers]
            print(list_workers_salary)
            for worker, salary in list_workers_salary:
                dict[worker] = salary
            total = 0
            avarage = 0
            count_workers = 0
            for i in dict.values():
                i_int = int(i)
                total += i_int
            for a in dict.values():
                count_workers += 1
            for n in dict.values():
                n = int(n)
                avarage += n / count_workers
    except FileNotFoundError:
        print("File not found or the file was corrupted")

    print(dict)
    return total, round(avarage)

total, average = total_salary("salarys.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")