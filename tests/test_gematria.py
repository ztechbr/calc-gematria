from gematria import calculate_value, normalize_hebrew


def test_chai_is_18():
    assert calculate_value("חי") == 18


def test_tetragrammaton_is_26():
    assert calculate_value("יהוה") == 26


def test_lev_is_32():
    assert calculate_value("לב") == 32


def test_torah_is_611():
    assert calculate_value("תורה") == 611


def test_niqqud_is_ignored():
    assert normalize_hebrew("חַי") == "חי"
    assert calculate_value("חַי") == 18


def test_final_letter_standard_and_gadol():
    assert calculate_value("ך", "standard") == 20
    assert calculate_value("ך", "gadol") == 500


def test_katan():
    assert calculate_value("תורה", "katan") == 17  # 4 + 6 + 2 + 5


def test_ordinal():
    assert calculate_value("אבג", "ordinal") == 6
