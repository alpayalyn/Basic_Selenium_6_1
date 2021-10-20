


class LCW:
    CATEGORY_PAGE_1 = (By.CSS_SELECTOR, '.dropdown')
    CATEGORY_PAGE_2 = (By.CSS_SELECTOR, '.image_Box.visible-lg.visible-md')
    CHOOSE_SIZE = (By.CSS_SELECTOR, '.selected')
    PRODUCT_PAGE = (By.CSS_SELECTOR, '.a_model_item')
    ADD_TO_CART = (By.CSS_SELECTOR, '.col-xl-12')
    CART_PAGE = (By.CSS_SELECTOR, '.header-cart')
    MAIN_PAGE = (By.CSS_SELECTOR, '.header-logo.img-logo')

    HEADER_CONTAINER = (By.CSS_SELECTOR, '.div-header-container') #check for first page
    MOST_SOLD = (By.CSS_SELECTOR, '.uzun.visible-lg.visible-md') #check for second page
    ADD_TO_CART_CHECK = (By.CSS_SELECTOR, '.pr-20') #check for add to cart

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.website)
        self.wait = WebDriverWait(self.driver, 15)

    def test_navigate(self):
        assert self.wait.until(ec.element_to_be_clickable(self.HEADER_CONTAINER)).is_displayed(). "En üstteki header yoktur bu da anasayfada olmadığımızı belirtir." #We are trying to be sure about are we on main page or not
        self.wait.until(ec.presence_of_all_elements_located(self.CATEGORY_PAGE_1))[2].click()
        assert self.wait.until(ec.element_to_be_clickable(self.MOST_SOLD)).is_displayed(). "En üstteki header yoktur bu da anasayfada olmadığımızı belirtir." #We are trying to be sure about are we on main page or not
        self.wait.until(ec.presence_of_all_elements_located(self.CATEGORY_PAGE_2))[2].click()
        assert self.wait.until(ec.element_to_be_clickable(self.ADD_TO_CART)).is_displayed(). "Add to cart butonu yoktur." #We are trying to be sure about are we on product page or not
        self.wait.until(ec.presence_of_all_elements_located(self.PRODUCT_PAGE))[1].click()
        self.wait.until(ec.presence_of_all_elements_located(self.CHOOSE_SIZE_PAGE))[0].click()
        self.wait.until(ec.presence_of_all_elements_located(self.ADD_TO_CART))[0].click()
        assert self.wait.until(ec.element_to_be_clickable(self.ADD_TO_CART_CHECK)).is_displayed(). "Ödeme sayfasına geçiniz kısmı yoktur butonu yoktur." #We are trying to be sure about are we on product page or not
        self.wait.until(ec.presence_of_all_elements_located(self.MAIN_PAGE))[0].click()
        assert self.wait.until(ec.element_to_be_clickable(self.HEADER_CONTAINER)).is_displayed(). "En üstteki header yoktur bu da anasayfada olmadığımızı belirtir." #We are trying to be sure about are we on main page or not



