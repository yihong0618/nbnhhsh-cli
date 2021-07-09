from hhsh import make_payload_text


def test_make_payload_text():
    assert make_payload_text("什么test, 22哈哈") == ["test", "22"]
