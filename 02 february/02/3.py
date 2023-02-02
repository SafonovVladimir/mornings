import pytest


def get_section_id(scroll: int, sizes: list) -> int:

    if scroll < 0:
        return -1

    elif scroll >= sum(sizes):
        return -1

    else:
        result = []
        for index, value in enumerate(sizes):
            result.append(value)
            if scroll < sum(result):
                return index

# print(get_section_id(99, [100]))
# print(get_section_id(345, [346, 430, 343]))


@pytest.mark.parametrize(
    "scroll, sizes, expected_result",
    [
        (0, [100], 0),
        (99, [100], 0),
        (100, [100, 200], 1),
        (345, [346, 430, 343], 0),
        (346, [346, 430, 343, 1], 1),
        (300, [100, 200, 300], 2),
        (1600, [300, 200, 400, 600, 100], -1)
    ]
)

def test_get_section_id(scroll, sizes, expected_result):
    assert get_section_id(scroll, sizes) == expected_result, (
        f"Function should return {expected_result}"
        f" when scroll is equal to {scroll}"
        f" and sizes is equal to {sizes}"
    )

