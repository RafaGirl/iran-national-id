from iran_national_id import is_valid, compute_check_digit, describe

def test_compute():
    assert compute_check_digit("136291941") == 1

def test_valid():
    assert is_valid("1360000003") is True

def test_describe_shape():
    info = describe("1360000003")
    assert isinstance(info, dict)
    assert "issuance" in info
    assert "province_fa" in info["issuance"]
