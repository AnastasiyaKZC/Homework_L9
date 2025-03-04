from selene import browser, have, be, command
from Homework_5.models.user import User


class RegistrationPage:

    def open(self):
        browser.open("https://demoqa.com/automation-practice-form")

    def fill(self, user: User):
        browser.element("#firstName").type(user.first_name)
        browser.element("#lastName").type(user.last_name)
        browser.element("#userEmail").type(user.email)

        browser.element(f'[for="gender-radio-{self.get_gender_value(user.gender)}"]').click()
        browser.element("#userNumber").type(user.phone)

        # Выбор даты рождения
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__year-select").type(user.birth_year)
        browser.element(".react-datepicker__month-select").type(user.birth_month)
        browser.element(f".react-datepicker__day--{int(user.birth_day):03}").click()

        # Ввод предметов
        browser.element("#subjectsInput").type(user.subject).press_enter()

        # Выбор хобби
        browser.element(f'[for="hobbies-checkbox-{self.get_hobby_value(user.hobby)}"]').click()

        # Загрузка изображения
        browser.element("#uploadPicture").send_keys(user.picture)

        # Ввод адреса
        browser.element("#currentAddress").type(user.address)

        # Выбор штата и города
        browser.element("#state").perform(command.js.scroll_into_view).click()
        browser.all("div.css-11unzgr").element_by(have.text(user.state)).click()

        browser.element("#city").should(be.clickable).click()
        browser.all("div.css-11unzgr").element_by(have.text(user.city)).click()

        return self  # Для чейнинга методов

    def submit(self):
        browser.element("#submit").press_enter()

    def should_have_registered(self, user: User):
        browser.element(".modal-title").should(have.text("Thanks for submitting the form"))
        browser.element(".table-responsive").should(have.text(user.first_name))
        browser.element(".table-responsive").should(have.text(user.last_name))
        browser.element(".table-responsive").should(have.text(user.email))

    @staticmethod
    def get_gender_value(gender: str):
        return {"Male": 1, "Female": 2, "Other": 3}[gender]

    @staticmethod
    def get_hobby_value(hobby: str):
        return {"Sports": 1, "Reading": 2, "Music": 3}[hobby]