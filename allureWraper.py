import allure
from functools import wraps

# allure wrapper class will try to add names to steps in allure report dynamically
#hence we do not need to add the aallure.step name at diferent fucntions in our pages
# we need to call the allurewrapper and BasePage class in all the page classes and inherit the BasePage class
# for example class LoginPage(): will be changed to class LoginPage(BasePage): in loginPage.py file


class BasePage:
    def __getattribute__(self, name):
        attr = super().__getattribute__(name)
        if callable(attr) and not name.startswith("__"):
            @wraps(attr)
            def wrapper(*args, **kwargs):
                step_name = f"{self.__class__.__name__}.{name}"
                with allure.step(step_name):
                    return attr(*args, **kwargs)
            return wrapper
        return attr