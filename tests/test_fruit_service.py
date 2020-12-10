from app.services import FruitService

service = FruitService()


def test_get_apple_color():
    assert service.get_apple_color() == "Red"
