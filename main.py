import asyncio
import random

async def view_message():
    name = 'Вячеслав'
    vacancy = 'Стажёр-программист Python / Python Developer Trainee'
    last_year_salary = '80+ т.р.'
    print(f'Моя имя: {name}')
    await asyncio.sleep(random.randint(1, 5))
    print(f'Я откликаюсь на вакансию: {vacancy}')
    await asyncio.sleep(random.randint(1, 5))
    print(f'Мои ожидания по з/п через год: {last_year_salary}')

ioloop = asyncio.get_event_loop()
tasks = [ioloop.create_task(view_message())]
wait_tasks = asyncio.wait(tasks)
ioloop.run_until_complete(wait_tasks)
ioloop.close()