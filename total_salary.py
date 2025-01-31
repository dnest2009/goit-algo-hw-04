from pathlib import Path

def total_salary(path):
    if Path(path).exists() and Path(path).is_file():  #перевірка існування файлу, чи це є файл
        try:
            with open(path,'r',encoding='UTF-8') as file: 
                workers_cards=[line.split(',') for line in file.readlines()]  #читаємо файл по рядку і розділяємо ""
                salary=[int(i[1]) for i in workers_cards] #з/п конкретного робітника
                total = sum(salary)  # сума всіх з/п
                average = total/len(salary) #середня з/п
                return total, average  # результати ф-ії
        except:
            print("wrong data")    # помилка з даними у файлі
    else:
        print("wrong path")   # файл не існує або це не файл

total, average = total_salary("salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")