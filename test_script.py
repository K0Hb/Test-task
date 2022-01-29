from main import start_script


def test_view():
    fixture = {
        'message1': ('Моя имя: ', 'Петя'),
        'message2': ('Я откликаюсь на вакансию: ', 'Хорошая вакансия'),
        'message3': ('Мои ожидания по з/п через год: ', '10+'),
        'message4':
            ('текст для хэширования',
             '3f6aa1c613acd7b7b37e13f817734a3273892c9d3e4400a0947e4e369c5f4250')}
    assert start_script('Петя',
                        'Хорошая вакансия',
                        10,
                        'текст для хэширования',
                        ) == fixture
