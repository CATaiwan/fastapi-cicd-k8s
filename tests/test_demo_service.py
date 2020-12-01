from fastapi_cicd_demo import config
from fastapi_cicd_demo.services import DemoService


def test_demo_color():
    service = DemoService()

    assert service.color() == "Red"


def test_show_env_variable():
    print(config.DB_HOST)
    print(config.DB_DATABASE)
    print(config.DB_USERNAME)
    print(config.DB_PASSWORD)

    assert True == True