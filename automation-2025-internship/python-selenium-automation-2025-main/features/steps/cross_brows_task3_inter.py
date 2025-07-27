from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
from app.application import Application

def before_all(context):
   context.driver = webdriver.Chrome()
   context.driver.maximize_window()
   context.app = Applicatioz   (context.driver)

def browser_init(context):
    #Initialize headless Firefox browser
    options = FirefoxOptions()
    options.add_argument("--headless")
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")


    service = FirefoxService(GeckoDriverManager().install())
    context.driver = webdriver.Firefox(service=service, options=options)


    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario:', scenario.name)
    browser_init(context)

def before_step(context, step):
    print('\nStarted step:', step)


def after_step(context, step):
    if step.status == 'failed':
     print('\nStep failed:', step)


def after_scenario(context, scenario):
    print('\nFinished scenario:', scenario.name)
    context.driver.quit()








