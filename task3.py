import search_algorithms

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "Файл не знайдено."

# Завантаження текстів
if read_file("стаття 1.txt") != "Файл не знайдено.": 
    text1 = read_file("стаття 1.txt") 
else:
    print('Файл не знайдено !')

# Підрядки для пошуку
pattern1 = "бізнес"  # Існує в text1
pattern2 = "learning"      # Існує в text2

        
if __name__ == '__main__': 

    import timeit
    print('Пошук за допомогою алгоритма Кнута-Морріса-Пратта: ' + str(timeit.timeit("kmp_search(text1, pattern1)", globals=globals())))




