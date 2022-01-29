import asyncio
import random
from typing import Dict
from hashlib import sha256


async def view_message(context: Dict) -> Dict:
    '''
        Функция принимает 3 аргумента (имя, вакансия, желаемая з/п через год)
        и выводит в консоль готовые предложения, далее необходимо ввести произволный
        текст для хэширования.
    '''
    # Словарь для формирования сообщений
    message_queue = {
        'message1': ('Моя имя: ', context['name']),
        'message2': ('Я откликаюсь на вакансию: ', context['vacancy']),
        'message3': ('Мои ожидания по з/п через год: ', f"{str(context['salary'])}+"),
    }

    # Вывод сообщений
    for message in message_queue:
        print(f'{message_queue[message][0]}{message_queue[message][1]}')
        pause = random.randint(1, 5)
        await asyncio.sleep(pause)

    # Ввод сообщения и дальнейшие хэширование
    text_hash = context['text_hash']
    if context['text_hash'] is None:
        text_hash = input('Введите текст для хэширования: ')
    hash = sha256(text_hash.encode('utf-8')).hexdigest()
    print(f'Хэш: {hash}')

    message_queue['message4'] = (text_hash, hash)
    return message_queue


# Вызов функции с необходимыми аргументами
def start_script(name: str, vacancy: str, salary: int, text_hash=None) -> Dict:
    context = {
        'name': name,
        'vacancy': vacancy,
        'salary': salary,
        'text_hash': text_hash,
    }
    result = asyncio.run(view_message(context))
    return result


if __name__ == "__main__":
    start_script('Вячеслав', 'Стажёр-программист Python / Python Developer Trainee', 60)
