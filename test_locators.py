from selenium.webdriver.common.by import By

class TestLocators:
    INPUT_NAME_FOR_REG = By.XPATH, ".//*[@id='name']" #локатор поля Имя формы Регистрация
    INPUT_EMAIL_FOR_REG = By.XPATH, "//*[@id='email']" #локатор поля E-mail формы Регистрация
    FIRST_BUTTON_NEXT = By.XPATH, "//*[@id='app']/main//button" #локатор первой кнопки Далее формы Регистрация
    INPUT_PASSWORD_FOR_REG = By.XPATH, "//*[@id='password']" #локатор поля Мастер-пароль формы Регистрация
    INPUT_PASSWORD_FOR_REG_REPEAT = By.XPATH, "//*[@id='password_re']" #локатор поля повторение Мастер-пароля формы Регистрация
    SECOND_BUTTON_NEXT = By.XPATH, "//*[@id='app']/main//button[2]" #локатор второй кнопки Далее формы Регистрация
    FOOTER_MISS_ADDING_CARD = By.XPATH, "//*[@id='app']/main//div[3]/div/a" #локатор футера Добавить карту позже
    BUTTON_NEXT_SECRET_KEY = By.XPATH, "//*[@id='swal2-html-container']/div/button" #локатор кнопки Далее всплывающего окна Сгенерируйте секретный ключ
    FIELD_WITH_SECRET_KEY = By.XPATH, "//*[@id='swal2-html-container']/div[1]/span[1]" #локатор поля с секретным кодом
    AREA_SECRET_KEY = By.XPATH, "//*[@id='swal2-html-container']" #локатор ВСЕГО всплывающего окна с секретным ключом
    BUTTON_DOWNLOAD_PASSWORD = By.XPATH, "//*[@id='swal2-html-container']/button/span[2]" #локатор кнопки Скачать всплывающего окна с секретным кодом
    BUTTON_IT_IS_CLEAR = By.XPATH, "//*[@id='swal2-html-container']/button" #локатор кнопки Понятно всплывающего поля секретного ключа
    FIRST_BUTTON_LATER = By.XPATH, "//*[@id='app']/div/div[1]/div/div[2]/button[1]" #локотор кнопки Позже всплывающего поля подтверждения e-mail
    SECOND_BUTTON_LATER = By.XPATH, "//*[@id='app']/div/div[1]/div/div[2]/button[1]" #локатор кнопки Позже предложения оставить отзыв
    FIELD_ID_INFO = By.XPATH, "//*[@id='app']/div/header/nav/div[3]/div[1]/div[1]" #локатор информационного поля с ID пользователя
