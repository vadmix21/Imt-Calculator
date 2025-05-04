
messages = {
    'ru': {
        'welcome': "Калькулятор ИМТ",
        'language_prompt': "Выберите язык (ru/en): ",
        'invalid_language': "Пожалуйста, выберите 'ru' или 'en'",
        'weight_prompt': "Введите вес в кг (20-300): ",
        'height_prompt': "Введите рост в метрах (0.5-2.5): ",
        'weight_error': "Ошибка: вес должен быть от 20 до 300 кг!",
        'height_error': "Ошибка: рост должен быть от 0.5 до 2.5 метров!",
        'numeric_error': "Ошибка! Введите числовое значение.",
        'results': "\nРезультаты:",
        'weight': "Вес: {} кг",
        'height': "Рост: {} м",
        'bmi': "Индекс массы тела (ИМТ): {:.1f}",
        'categories': {
            18.5: "Недостаток веса",
            25: "Норма",
            30: "Избыточный вес",
            'else': "Ожирение"
        },
        'recommendations': {
            18.5: "Рекомендация: увеличьте калорийность питания",
            25: "Рекомендация: поддерживайте текущий образ жизни",
            30: "Рекомендация: увеличьте физическую активность",
            'else': "Рекомендация: обратитесь к диетологу"
        },
        'repeat_prompt': "\nСделать еще один расчет? (y/n): ",
        'goodbye': "До свидания!",
        'repeat_error': "Пожалуйста, введите 'y' или 'n'"
    },
    'en': {
        'welcome': "BMI Calculator",
        'language_prompt': "Select language (ru/en): ",
        'invalid_language': "Please select 'ru' or 'en'",
        'weight_prompt': "Enter weight in kg (20-300): ",
        'height_prompt': "Enter height in meters (0.5-2.5): ",
        'weight_error': "Error: Weight must be between 20-300 kg!",
        'height_error': "Error: Height must be between 0.5-2.5 meters!",
        'numeric_error': "Error! Please enter numeric values.",
        'results': "\nResults:",
        'weight': "Weight: {} kg",
        'height': "Height: {} m",
        'bmi': "Body Mass Index (BMI): {:.1f}",
        'categories': {
            18.5: "Underweight",
            25: "Normal weight",
            30: "Overweight",
            'else': "Obesity"
        },
        'recommendations': {
            18.5: "Recommendation: Increase calorie intake",
            25: "Recommendation: Maintain your lifestyle",
            30: "Recommendation: Increase physical activity",
            'else': "Recommendation: Consult a nutritionist"
        },
        'repeat_prompt': "\nCalculate again? (y/n): ",
        'goodbye': "Goodbye!",
        'repeat_error': "Please enter 'y' or 'n'"
    }
}

def get_language():
    while True:
        lang = input(messages['ru']['language_prompt']).lower()
        if lang in messages:
            return lang
        print(messages['ru']['invalid_language'])

def calculate_bmi(lang):
    msg = messages[lang]
    print(f"\n{msg['welcome']}")
    
    while True:
        try:
            
            while True:
                weight = float(input(msg['weight_prompt']))
                if 20 <= weight <= 300:
                    break
                print(msg['weight_error'])
            
            
            while True:
                height = float(input(msg['height_prompt']))
                if 0.5 <= height <= 2.5:
                    break
                print(msg['height_error'])
            
            
            bmi = weight / (height ** 2)
            
           
            current_category = "Unknown"
            recommendation = "No recommendation available"
            
            for threshold, category in msg['categories'].items():
                if threshold == 'else':
                    break
                if bmi < threshold:
                    current_category = category
                    recommendation = msg['recommendations'][threshold]
                    break
            else:
                current_category = msg['categories']['else']
                recommendation = msg['recommendations']['else']
            
           
            print(msg['results'])
            print(msg['weight'].format(float(weight)))
            print(msg['height'].format(height))
            print(msg['bmi'].format(bmi))
            print(f"{current_category}\n{recommendation}")
            
            return  
            
        except ValueError:
            print(msg['numeric_error'])

def ask_repeat(lang):
    while True:
        answer = input(messages[lang]['repeat_prompt']).lower()
        if answer in ['y', 'n']:
            return answer == 'y'
        print(messages[lang]['repeat_error'])


if __name__ == "__main__":
    language = get_language()
    
    while True:
        calculate_bmi(language)
        if not ask_repeat(language):
            print(messages[language]['goodbye'])
            break
