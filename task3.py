from search_algorithms import kmp_search, boyer_moore_search, rabin_karp_search
import timeit

def measure_time(algorithm, text, pattern):
    if not text or not pattern:
        return float('inf')  # Якщо текст або шаблон порожні, час "нескінченний"
    setup_code = f"from search_algorithms import {algorithm.__name__}"
    test_code = f"{algorithm.__name__}(text, pattern)"
    return timeit.timeit(test_code, setup=setup_code, globals={'text': text, 'pattern': pattern}, number=1000)

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "Файл не знайдено."
    
def find_fastest(results):
    overall = {}
    for text_name in results:
        print(f"Найшвидші результати для {text_name}:")
        fastest_existing = min(results[text_name], key=lambda x: results[text_name][x]["existing"])
        fastest_fake = min(results[text_name], key=lambda x: results[text_name][x]["fake"])
        print(f"  Існуючий підрядок: {fastest_existing} ({results[text_name][fastest_existing]['existing']:.6f} сек)")
        print(f"  Не існуючий підрядок: {fastest_fake} ({results[text_name][fastest_fake]['fake']:.6f} сек)")
        
        # Агрегація для загального результату
        for algo in results[text_name]:
            if algo not in overall:
                overall[algo] = {"existing": 0, "fake": 0}
            overall[algo]["existing"] += results[text_name][algo]["existing"]
            overall[algo]["fake"] += results[text_name][algo]["fake"]
    
    print("\nЗагальні результати:")
    fastest_existing_overall = min(overall, key=lambda x: overall[x]["existing"])
    fastest_fake_overall = min(overall, key=lambda x: overall[x]["fake"])
    print(f"  Найшвидші для існуючого підрядка: {fastest_existing_overall} ({overall[fastest_existing_overall]['existing']:.6f} сек)")
    print(f"  Найшвидші для не існуючого підрядка: {fastest_fake_overall} ({overall[fastest_fake_overall]['fake']:.6f} сек)")

# Завантаження текстів
if read_file("стаття 1.txt") != "Файл не знайдено.": 
    text1 = read_file("стаття 1.txt") 
else:
    print('Файл не знайдено !')
if read_file("стаття 2.txt") != "Файл не знайдено.": 
    text2 = read_file("стаття 2.txt") 
else:
    print('Файл не знайдено !')

# Підрядки для пошуку
pattern1 = "даних"         # Існує в стаття 1, стаття 2
pattern2 = "fake"       # Не Існує 

        
if __name__ == '__main__': 

    algorithms = [kmp_search, rabin_karp_search] # boyer_moore_search - працює нескінченно довго, тому виключений із аналізу
    results = {}

    for text_name, text, existing, fake in [
        ("Стаття 1", text1, pattern1, pattern2),
        ("Стаття 2", text2, pattern1, pattern2)]:
        results[text_name] = {}
        for algo in algorithms:
            time_existing = measure_time(algo, text, existing)
            time_fake = measure_time(algo, text, fake)
            results[text_name][algo.__name__] = {
                "existing": time_existing,
                "fake": time_fake
            }
    find_fastest(results)





