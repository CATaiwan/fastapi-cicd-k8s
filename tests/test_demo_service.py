from fastapi_cicd_demo.services import DemoService


def test_demo_color():
    service = DemoService()

    assert service.color() == "Red"
