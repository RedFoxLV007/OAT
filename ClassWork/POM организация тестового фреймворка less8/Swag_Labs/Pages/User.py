# test_login.py
# {'key: 'value', ...} -> ('value', ...)
def data_login(data):# data = [{},{}]
    for i, l in enumerate(data):
        data[i] = (l['username'], l['password'], l['expected_result'])  # [(),(), ...]
    return data

test_cases = [
    {
        "description": "Успешный вход с правильными учетными данными",
        "username": "standard_user",
        "password": "secret_sauce",
        "expected_result": "inventory.html"
    },
    {
        "description": "Вход с заблокированным аккаунтом",
        "username": "locked_out_user",
        "password": "secret_sauce",
        "expected_result": ""
    },
    {
        "description": "Вход с неверными учетными данными",
        "username": "invalid_username",
        "password": "invalid_password",
        "expected_result": ""
    },
    {
        "description": "Вход с пустым полем пароля",
        "username": "standard_user",
        "password": "",
        "expected_result": ""
    },
    {
        "description": "Вход с пустым полем имени пользователя",
        "username": "",
        "password": "secret_sauce",
        "expected_result": ""
    },
    {
        "description": "Вход с неправильным форматом имени пользователя",
        "username": "@#%$^",
        "password": "secret_sauce",
        "expected_result": ""
    },

    {
        "description": "Вход с проблемами учетной записи",
        "username": "problem_user",
        "password": "secret_sauce",
        "expected_result": "inventory.html"
    },
    {
        "description": "Вход с проблемами производительности",
        "username": "performance_glitch_user",
        "password": "secret_sauce",
        "expected_result": "inventory.html"
    },
    {
        "description": "Вход с ошибкой",
        "username": "error_user",
        "password": "secret_sauce",
        "expected_result": "inventory.html"
    },
    {
        "description": "Вход с визуальными проблемами",
        "username": "visual_user",
        "password": "secret_sauce",
        "expected_result": "inventory.html"
    },
]
#print(data_login(test_cases))