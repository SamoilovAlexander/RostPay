import random
import string

class DataHelper:

    @staticmethod
    def get_name():
        names = ["Александр", "Дмитрий", "Максим", "Сергей", "Андрей", "Иван", "Петр", "Николай", "Владимир", "Артем",
                 "Екатерина", "Мария", "Анна", "Ольга", "Елена"]
        return random.choice(names)

    @staticmethod
    def get_email(min_length, max_length):
        letters = string.ascii_lowercase
        name_of_email = ''.join(random.choice(letters) for i in range(min_length, max_length))
        mail = random.choice(["gmail.com", "mail.ru", "yandex.ru", "yahoo.com"])
        return f'{name_of_email}@{mail}'

    @staticmethod
    def get_password():
        return random.randint(100000, 9999999999)
