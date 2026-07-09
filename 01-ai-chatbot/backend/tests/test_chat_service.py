from unittest.mock import patch, MagicMock
from app.services.chat_service import get_chat_response


@patch("app.services.chat_service.model")
def test_get_chat_response_returns_text(mock_model):
    fake_response = MagicMock()
    fake_response.content = "Hello there!"
    mock_model.invoke.return_value = fake_response

    result = get_chat_response("Hi")

    assert result == "Hello there!"
    mock_model.invoke.assert_called_once_with("Hi")
