import random
from datetime import datetime as dt
import json
import sys
import math
from colorama import init

init(autoreset=True)
blue = "\x1b[;36;3m"


class ChatBot:

    def __init__(self):
        self.user = None
        self.responses = ["Хм... Ну гаразд.", "Ну якщо ви так просите.", "Цікавий вибір!",
                          "Вам вдалось мене здивувати!", "Неочікувано)"]
        self.topics = {
            "математика": self.maths,
            "фізика": self.physics,
            "філологія": self.philology,
            "географія": self.geography,
            "робота з текстом": self.work_with_text,
            "інше": self.other_tasks
        }
        self.output = ""


    def greeting(self):
        print(f"{blue}Вітаю, мене звати Помічник. "
              "Для повернення до попередньої теми введіть 'назад', для виходу - 'вихід', а для допомоги  - 'допомога'")
        chatbot.program()

    def program(self):
        while True:
            print(
                f"{blue}Ви можете задати мені питання з наступних тем: математика, фізика, філологія, географія, робота з текстом, інше.")
            user = input("")
            chatbot.user_input(user)
            if user.lower() in chatbot.topics.keys():
                print(f"{blue}" + random.choice(chatbot.responses))
                print(f"{blue}Ви обрали тему '{user.lower()}'. У цій темі є такі підтеми:")
                chatbot.topics[user.lower()]()
            elif user.lower() == "вихід":
                break
            elif user.lower() == "допомога":
                continue
            else:
                chatbot.error()

    def user_input(self, user):
        if user.lower() == "назад":
            chatbot.program()
        elif user.lower() == "вихід":
            print(f"{blue}Радий був поспілкуватись! Якщо виникнуть нові питання, звертайтесь)")
            self.save_dialogue('dialogue.json')
            exit()
        elif user.lower() == "допомога":
            chatbot.user_help()

    def error(self):
        error = "Я не знаю цієї теми."
        print(f"{blue}" + error)

    def user_help(self):
        print(f"{blue}Для виходу, напишіть 'вихід'. Для повернення напишіть 'назад'.")
        chatbot.program()

    def maths(self):
        maths_topics = {"відстань між двома точками в просторі": chatbot.distance,
                        "площа трикутника за векторним добутком": chatbot.area_triangle,
                        "площа трикутника за основою та висотою": chatbot.s_triangle,
                        "виведення числа π": chatbot.pi
                        }
        chatbot.maths_topics = maths_topics
        print(f"{blue}" + '\n'.join(maths_topics))
        user = input("")
        chatbot.user_input(user)
        if user in maths_topics.keys():
            print(f"{blue}Ви обрали тему '{user}'")
            chatbot.maths_topics[user.lower()]()
        else:
            chatbot.error()

    def pi(self):
        print(f"{blue}π = " + str(math.pi))

    def distance(self):
        distance = lambda x1, x2, y1, y2, z1, z2: math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
        print(f"{blue}Введіть значення координат x1, y1, z1, x2, y2, z2 через пробіл: ")
        user = input("")
        chatbot.user_input(user)
        coordinates = user.split()
        try: x1, y1, z1, x2, y2, z2 = map(float, coordinates)
        except:
            print(f"{blue}Очевидно виникла якась помилка, спробуйте ще раз!")
            chatbot.distance()
        print(f"{blue}Відстань між двома точками дорівнює {round(distance(x1, x2, y1, y2, z1, z2))}")

    def area_triangle(self):
        area_triangle = lambda a, b: 1 / 2 * abs(a * b)
        print(f"{blue}Введіть довжини обох векторів через пробіл: ")
        user = input("")
        chatbot.user_input(user)
        variables = user.split()
        try: a, b = map(float, variables)
        except:
            print(f"{blue}Очевидно виникла якась помилка, спробуйте ще раз!")
            chatbot.area_triangle()
        print(f"{blue}Площа трикутника дорівнює {round(area_triangle(a, b))}")

    def s_triangle(self):
        s_triangle = lambda b, h: 1 / 2 * b * h
        print(f"{blue}Введіть довжину висоти та основи через пробіл: ")
        user = input("")
        chatbot.user_input(user)
        variables = user.split()
        try:
            h, b = map(float, variables)
        except:
            print(f"{blue}Очевидно виникла якась помилка, спробуйте ще раз!")
            chatbot.s_triangle()
        print(f"{blue}Площа трикутника дорівнює {round(s_triangle(b, h))}")

    def physics(self):
        physics_topics = {"формула Ампера": chatbot.ampere_formula,
                          "виведення сталої Планка": chatbot.planka,
                          "закон Архімеда": chatbot.archimedes_principle,
                          "знаходження маси тіла": chatbot.weight}
        self.physics_topics = physics_topics
        print(f"{blue}" + '\n'.join(physics_topics))
        user = input("")
        chatbot.user_input(user)
        if user in physics_topics.keys():
            print(f"{blue}Ви обрали тему '{user}'")
            chatbot.physics_topics[user]()
        else:
            chatbot.error()

    def planka(self):
        h = 6.62607015e-34
        print(f"{blue}Значення сталої Планка (h):", h)

    def ampere_formula(self):
        magnetic_constant = 4 * math.pi * 10 ** (-7)
        ampere_formula = lambda i, r: (magnetic_constant * i) / 2 * math.pi * r
        print(f"{blue}Введіть силу струму та відстань до провідника через пробіл: ")
        user = input("")
        chatbot.user_input(user)
        variables = user.split()
        try: i, r = map(float, variables)
        except:
            print(f"{blue}Очевидно виникла якась помилка, спробуйте ще раз!")
            chatbot.s_triangle()
        print(
            f"{blue}Індукція магнітного поля дорівнює {ampere_formula(i, r)}")

    def archimedes_principle(self):
        archimedes_principle = lambda p, v: 9.8 * p * v
        print(f"{blue}Введіть густину рідини та об'єм зануреного тіла через пробіл: ")
        user = input("")
        chatbot.user_input(user)
        variables = user.split()
        try: p, v = map(float, variables)
        except:
            print(f"{blue}Очевидно виникла якась помилка, спробуйте ще раз!")
            chatbot.s_triangle()
        print(f"{blue}Сила Архімеда дорівнює {archimedes_principle(p, v)}")

    def weight(self):
        weight = lambda v, p: p * v
        print(f"{blue}Введіть густину та об'єм тіла через пробіл: ")
        user = input("")
        chatbot.user_input(user)
        variables = user.split()
        try: p, v = map(float, variables)
        except:
            print(f"{blue}Очевидно виникла якась помилка, спробуйте ще раз!")
            chatbot.s_triangle()
        print(f"{blue}Маса тіла дорівнює {weight(p, v)}")

    def geography(self):
        geography_topics = {"яке найбільше озеро в світі за площею?": chatbot.lake,
                            "які дві держави мають найбільшу кількість кордонів з іншими державами?": chatbot.states,
                            "яка площа України?": chatbot.square,
                            "який найбільший вулкан у світі?": chatbot.volcano}
        chatbot.geography_topics = geography_topics
        print(f"{blue}" + '\n'.join(geography_topics))
        user = input("")
        chatbot.user_input(user)
        if user in geography_topics.keys():
            print(f"{blue}Ви обрали тему '{user}'")
            chatbot.geography_topics[user]()
        else:
            chatbot.error()

    def lake(self):
        lake = """Найбільше озеро в світі за площею - це Каспійське море. 
Хоча його назва містить термін "море", Каспійське море фактично вважається найбільшим озером на планеті. 
Загальна площа Каспійського моря становить близько 371 000 квадратних кілометрів. 
Це солоновате озеро розташоване між Азією та Європою, і його природні кордони включають росію, Казахстан, Туркменістан, Іран та Азербайджан."""
        print(f"{blue}" + lake)

    def states(self):
        states = """Дві держави, які мають найбільшу кількість кордонів з іншими державами, 
це російська федерація та Китай.
Російська Федерація межує з 14 країнами: Азербайджаном, Білоруссю, Китаєм, Естонією, Фінляндією, Грузією, 
Казахстаном, Латвією, Литвою, Монголією, Норвегією, Польщею, Південною Кореєю, Україною та Фінляндією.
Китай межує з 14 країнами: Афганістаном, Бутаном, М'янмою, Казахстаном, Киргизстаном, Лаосом, 
Макао (Автономна область Китаю), Монголією, Непалом, Пакистаном, Російською Федерацією, Таджикистаном, В'єтнамом та Індією."""
        print(f"{blue}" + states)

    def square(self):
        square = "Загальна площа України становить 603 700 км²"
        print(f"{blue}" + square)

    def volcano(self):
        volcano = """Найбільший вулкан у світі - це Мауна Лоа на острові Гаваї в США. 
Мауна Лоа є одним з найактивніших вулканів у світі і має величезні розміри. 
Висота вулкана від його основи під водою до вершини становить близько 9 144 метрів. 
Якщо виміряти відстань від його основи на дні океану, Мауна Лоа визначається як найвищий гора у світі. 
Вулкан займає значну частину острова Гаваї та є величезним об'єктом геологічного і наукового дослідження."""
        print(f"{blue}" + volcano)

    def philology(self):
        philology_topics = {"Які часи є в англійській мові?": chatbot.tenses,
                            "Як утворити Passive Voice в Present Simple?": chatbot.passive,
                            "Як утворюються дієслова в давальному відмінку?": chatbot.verbs}
        chatbot.philology_topics = philology_topics
        print(f"{blue}" + '\n'.join(philology_topics))
        user = input("")
        chatbot.user_input(user)
        if user in philology_topics.keys():
            print(f"{blue}Ви обрали тему '{user}'")
            chatbot.philology_topics[user]()
        else:
            chatbot.error()

    def tenses(self):
        tenses = """В англійській мові є наступні часи:
Present Simple (теперішній простий час)
Present Continuous (теперішній тривалий час)
Present Perfect (теперішній доконаний час)
Present Perfect Continuous (теперішній доконаний тривалий час)
Past Simple (минулий простий час)
Past Continuous (минулий тривалий час)
Past Perfect (минулий доконаний час)
Past Perfect Continuous (минулий доконаний тривалий час)
Future Simple (майбутній простий час)
Future Continuous (майбутній тривалий час)
Future Perfect (майбутній доконаний час)
Future Perfect Continuous (майбутній доконаний тривалий час)"""
        print(f"{blue}" + tenses)

    def passive(self):
        passive = """Утворення Passive Voice в Present Simple виконується за допомогою допоміжного дієслова "to be" в Present Simple (am/is/are) + дієслово у формі Past Participle.
Утворення Passive Voice в Present Simple має наступну структуру:
[Subject] + am/is/are + [Past Participle (3rd form of the verb)]
У Passive Voice суб'єкт дії стає об'єктом речення, а хто виконує дію може бути вказано за допомогою фрази "by + агент дії" (необов'язково)."""
        print(f"{blue}" + passive)

    def verbs(self):
        verbs = """У давальному відмінку відбуваються зміни у формі дієслів, залежно від роду та числа іменника, до якого вони відносяться.
Основні правила утворення дієслів у давальному відмінку української мови:
Якщо іменник є чоловічого роду, однини, дієслово в давальному відмінку має закінчення "-ові" або "-еві". 
Наприклад: дати комусь (дати батькові), допомогти хтось (допомогти другові).
Якщо іменник є жіночого роду, однини, дієслово в давальному відмінку має закінчення "-і" або "-ї". 
Наприклад: дати комусь (дати матері), розказати комусь (розказати подрузі).
Якщо іменник є середнього роду, однини, дієслово в давальному відмінку має закінчення "-у" або "-ю". 
Наприклад: показати чому-небудь (показати вікну), вчити когось (вчити студента).
У множині незалежно від роду іменників, дієслово в давальному відмінку має закінчення "-ам" або "-ям". 
Наприклад: допомагати комусь (допомагати друзям), говорити про щось (говорити про фактах)."""
        print(f"{blue}" + verbs)

    def work_with_text(self):
        text_topics = {
            "знайти складені з латинських літер слова, які у тексті зустрічаються більше 10 разів": chatbot.find_words_10,
            "знайти всі слова, які складаються з цифр": chatbot.digit_words,
            "вивести текст без зайвих пробілів": chatbot.spaces,
            "знайти найдовше речення в тексті": chatbot.longest_sentence,
            "знайти найбільш часто вживану літеру в тексті": chatbot.most_common_letter}
        chatbot.text_topics = text_topics
        print(f"{blue}" + '\n'.join(text_topics.keys()))
        print(f"{blue}Введіть назву вхідного файлу з текстом: ")
        user = input("")
        chatbot.user_input(user)
        input_file = user
        chatbot.read_file(input_file)
        print(f"{blue}Введіть вибрану тему:")
        user = input("")
        chatbot.user_input(user)
        if user in text_topics.keys():
            print(f"{blue}Ви обрали тему '{user}'")
            chatbot.text_topics[user.lower()](text)
        else:
            chatbot.error()
        print(f"{blue}Введіть назву вихідного файлу, куди потрібно записати відповідь: ")
        user = input("")
        chatbot.user_input(user)
        output_file = user
        output = chatbot.output
        chatbot.write_output(output_file, output)
        print(f"{blue}Відповідь записано в файл '{output_file}'")

    def read_file(self, input_file):
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()
            chatbot.text = text

    def write_output(self, output_file, output):
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(output)

    def find_words_10(self, text):
        word_count = {}
        words = text.split()
        for word in words:
            word = word.strip('.,!?:;"')
            if word.isalpha() and word.islower():
                word_count[word] = word_count.get(word, 0) + 1
        result = [word for word, count in word_count.items() if count > 10]
        if not result:
            result = "немає таких слів."
        chatbot.output = f"Слова складені з латинських літер, що зустрічаються більше 10 разів:{result}"

    def digit_words(self, text):
        words = text.split()
        result = [word for word in words if word.isdigit()]
        if result == []:
            result = "немає таких слів."
        chatbot.output = f"Слова, які складаються з цифр: {result}"

    def spaces(self, text):
        global output
        chatbot.output = ' '.join(text.split())
        return chatbot.output

    def longest_sentence(self, text):
        sentences = text.split('. ')
        chatbot.output = max(sentences, key=len)
        return chatbot.output

    def most_common_letter(self, text):
        letter_count = {}
        for letter in text:
            if letter.isalpha():
                letter = letter.lower()
                letter_count[letter] = letter_count.get(letter, 0) + 1
        most_common_letter = max(letter_count, key=letter_count.get)
        chatbot.output = f"Найбільш часто вживана літера в тексті: {most_common_letter}"
        return chatbot.output

    def other_tasks(self):
        other_tasks = {"який зараз рік?": chatbot.current_year,
                       "підкидання кубика": chatbot.dice_roll,
                       "улюблена пісня": chatbot.favourite_song,
                       "гра 'історія'": chatbot.story_game}
        chatbot.other_tasks = other_tasks
        print(f"{blue}" + '\n'.join(other_tasks))
        user = input("")
        chatbot.user_input(user)
        if user in other_tasks:
            print(f"{blue}Ви обрали тему '{user}'")
            chatbot.other_tasks[user.lower()]()
        else:
            chatbot.error()

    def current_year(self):
        current_date = dt.now()
        current_year = current_date.year
        print(f"{blue}Поточний рік: {current_year}")

    def dice_roll(self):
        print(f"{blue}Випало число:", random.randint(1, 6))

    def favourite_song(self):
        song1 = """Her name is she, queen of the kings
Running so fast, beating the wind
Nothing in this world could stop the spread of her wings 
She, queen of the kings
Broken hеr cage, threw out the keys
She will be the warrior of north and southern seas"""
        song2 = """Don’t care what you say
Don’t care how you feel
Get out of my way
‘Cause I got a heart of steel"""
        song3 = """Instead I wrote a song
‘Bout how you did me wrong
I could’ve cried at home
And spent the night alone
Instead I wrote a song
I feel much better now
Mе and my girls are out
And we all sing along
Instead I wrotе a song"""
        song4 = """No I don’t care about them all
‘Cause all I want is to be loved
And all I care about is you
You’re stuck on me like a tattoo
No I don’t care about the pain
I’ll walk through fire and through rain
Just to get closer to you
You’re stuck on me like a tattoo"""
        song5 = """And when the world got me going crazy
I carry on
‘Cause I know I’m strong
When the world got me going crazy
I carry on
And it’s all because of"""
        songs = [song1, song2, song3, song4, song5]
        print(f"{blue}Приспів моєї улюбленої пісні:", random.choice(songs))

    def story_game(self):
        print(f"{blue}Дайте відповідь на наступні питання, щоб вийшла повноцінна історія.")
        templates = [
            "Жив-був {хто} {де} {коли} і робив це {навіщо}. І отже, {що}.",
            "{хто} з'явився {де} {коли} та зробив це {навіщо}. А потім {що}.",
            "Був {хто} {де} {коли}, мав ціль {навіщо} та виконав {що}.",
            "{хто} проживав у {де} {коли} з метою {навіщо} і досяг {що}.",
            "{де} {коли} {хто} робив це {навіщо} та досяг {що}."]
        questions = {
            "хто": "Хто?",
            "де": "Де?",
            "коли": "Коли?",
            "навіщо": "Навіщо?",
            "що": "Що?"
        }
        answers = {}
        for key, question in questions.items():
            answer = input(question + " ")
            answers[key] = answer
        for template in templates:
            text = template.format(**answers)
            print(f"{blue}" + text)
            print(f"{blue}--------------------")


chatbot = ChatBot()
chatbot.greeting()
