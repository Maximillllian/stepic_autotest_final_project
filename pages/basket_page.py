from .base_page import BasePage
from .locators import BasketPageLocators, BasePageLocators
from selenium.common.exceptions import NoSuchElementException

languages = {
    "ar": "سلة التسوق فارغة",
    "ca": "La seva cistella està buida.",
    "cs": "Váš košík je prázdný.",
    "da": "Din indkøbskurv er tom.",
    "de": "Ihr Warenkorb ist leer.",
    "en": "Your basket is empty.",
    "el": "Το καλάθι σας είναι άδειο.",
    "es": "Tu carrito esta vacío.",
    "fi": "Korisi on tyhjä",
    "fr": "Votre panier est vide.",
    "it": "Il tuo carrello è vuoto.",
    "ko": "장바구니가 비었습니다.",
    "nl": "Je winkelmand is leeg",
    "pl": "Twój koszyk jest pusty.",
    "pt": "O carrinho está vazio.",
    "pt-br": "Sua cesta está vazia.",
    "ro": "Cosul tau este gol.",
    "ru": "Ваша корзина пуста",
    "sk": "Váš košík je prázdny",
    "uk": "Ваш кошик пустий.",
    "zh-cn": "Your basket is empty.",
}


class BasketPage(BasePage):
    def should_basket_text_is_empty(self):
        basket_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text
        continue_shopping_text = self.browser.find_element(*BasketPageLocators.CONTINUE_SHOPPING_TEXT).text
        basket_text = basket_text.replace(continue_shopping_text, '')
        basket_text = basket_text[:-1]
        language_tag = self.browser.find_element(*BasePageLocators.CURRENT_LANGUAGE)
        language = language_tag.get_attribute('value')
        print(f'Язык - {language}, тип - {type(language)}')
        print(basket_text, languages[language])
        return basket_text == languages[language]

    def should_basket_contains_no_products(self):
        try:
            items = self.browser.find_element(*BasketPageLocators.BASKET_ITEMS)
        except NoSuchElementException:
            return True
        return False
