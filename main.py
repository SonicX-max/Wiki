from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Импортируем Keys для работы с клавишами
import time


def search_wikipedia(query):
    browser = webdriver.Chrome()
    browser.get("https://ru.wikipedia.org/")

    # Находим поле поиска и вводим запрос
    search_input = browser.find_element(By.NAME, "search")
    search_input.send_keys(query)
    search_input.send_keys(Keys.RETURN)
    time.sleep(2)  # Ждем, пока страница загрузится

    return browser


def list_paragraphs(browser):
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for index, paragraph in enumerate(paragraphs):
        print(f"Paragraph {index + 1}: {paragraph.text}")
        user_choice = input("Введите 'n' для следующего параграфа, 'q' для выхода: ")
        if user_choice.lower() == 'q':
            break


def choose_link(browser):
    links = browser.find_elements(By.XPATH, "//a[@href]")
    for index, link in enumerate(links):
        print(f"Link {index + 1}: {link.get_attribute('href')}")
    choice = int(input("Выберите номер ссылки для перехода: ")) - 1
    browser.get(links[choice].get_attribute('href'))


def main():
    query = input("Введите поисковый запрос: ")
    browser = search_wikipedia(query)

    while True:
        print("\nВыберите действие:")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")

        choice = input("Ваш выбор: ")

        if choice == '1':
            list_paragraphs(browser)
        elif choice == '2':
            choose_link(browser)
        elif choice == '3':
            break
        else:
            print("Неправильный выбор, попробуйте снова.")

    browser.quit()


if __name__ == "__main__":
    main()