import pytest
import httpx
from typing import List


@pytest.mark.smoke_test
@pytest.mark.parametrize('q', [['book1', 'book4'], ['book5', 'book6']])
def test_get_book(q: List[str]):
    resp = httpx.get(
        url='http://127.0.0.1:8080/book',
        params={'q': q}
    )
    expected_result = q
    fact_result = resp.json()
    print(f"Expected result was {expected_result} an the fact result is {fact_result}")
    assert expected_result == fact_result


