from pathlib import Path

def gets_cats_info(path):
    if Path(path).exists() and Path(path).is_file():  #перевірка існування файлу, чи це є файл
        try:
            with open(path,'r',encoding='UTF-8') as file:  #відкриваємо файл
                cat_list=[]                                 #створюємо пустий список
                cat_data=[line.split(',') for line in file.readlines()]  #читаємо файл по рядку і розділяємо ","
                for cat in cat_data:
                    cat_list.append({'id':cat[0],'name':cat[1],'age':cat[2].strip()})      # додаємо до списку словники із даними котів
                return cat_list         # виводимо результати
        except:
            print("wrong data")    # помилка з даними у файлі
    else:
        print("wrong path")   # файл не існує або це не файл 
                
                
x=gets_cats_info('cats.txt')
print(x)