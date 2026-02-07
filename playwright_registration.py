from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()

    try:
        # Переходим на страницу входа
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        # Заполняем поле Email
        page.get_by_label("Email").click()
        page.get_by_label("Email").fill("user.name@gmail.com")

        # Заполняем поле Username
        page.get_by_label("Username").click()
        page.get_by_label("Username").fill("username")

        # Заполняем поле Password
        page.get_by_label("Password").click()
        page.get_by_label("Password").fill("password")

        # Нажимаем на кнопку Registration
        page.get_by_test_id("registration-page-registration-button").click()

        # Проверяем наличие заголовка Dashboard
        element = page.get_by_test_id("dashboard-toolbar-title-text")
        element.wait_for(state="visible")

        if element.is_visible():
            print("Dashboard появился на странице.")
        else:
            print("Dashboard не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        # Закрываем браузер
        browser.close()