from Homework_5.pages.registration_page import RegistrationPage
from Homework_5.models.user import User

# Создаю объект пользователя
def test_registration():
    user = User(
        first_name="Анастасия",
        last_name="Кузнецова",
        email="kuznetsova@mail.com",
        gender="Female",
        phone="1234567890",
        birth_year="1984",
        birth_month="May",
        birth_day="9",
        subject="Math",
        hobby="Reading",
        picture="/Users/kuznetsova/Desktop/download.jpg",
        address="Ростов-на-Дону, ул.Города Волос",
        state="Haryana",
        city="Karnal"
    )


    registration_page = RegistrationPage() # Создаю объект страницы
    registration_page.open() # Открываю страницу формы
    registration_page.fill(user).submit() # Заполняю форму
    registration_page.should_have_registered(user) # Проверка успешной регистрации. Метод should_have_registered(user) сравнивает введенные данные user с теми, которые появились на странице после отправки формы.