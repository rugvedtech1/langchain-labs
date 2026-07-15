from unittest.mock import patch, MagicMock
from app.services.chat_service import get_chat_response


@patch("app.services.chat_service.chain_with_history")
def test_get_chat_response_returns_text(mock_chain):
    fake_response = MagicMock()
    fake_response.content = "Hello there!"
    mock_chain.invoke.return_value = fake_response

    result = get_chat_response("Hi", "session-123")

    assert result == "Hello there!"
    mock_chain.invoke.assert_called_once_with(
        "Hi", config={"configurable": {"session_id": "session-123"}}
    )
