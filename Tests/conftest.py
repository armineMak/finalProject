import json
import pytest
import selenium.webdriver
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture
def config(scope='session'):
    cwd = os.getcwd()
    files = os.listdir(cwd)
    print("files in %r: %s" % (cwd, files))
    with open('config.json') as config_file:
        config = json.load(config_file)

    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome', 'Chrome_Remote']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0
    return config


@pytest.fixture
def browser(config):
    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()

    elif config['browser'] == 'Chrome_Remote':
        b = selenium.webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)

    elif config['browser'] == "Headless Chrome":
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser"{config["browser"]}" is not supported')

    b.implicitly_wait(config['implicit_wait'])

    b.maximize_window()

    b.get(config["baseURL"])

    yield b

    b.quit()