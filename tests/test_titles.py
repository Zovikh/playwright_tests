from playwright.sync_api import Page

def test_main_page_title(page: Page):
    page.goto("https://www.litres.ru")
    assert page.title() == "Литрес – сервис электронных и аудиокниг, скачать в fb2 и mp3, читать и слушать онлайн на Litres"
