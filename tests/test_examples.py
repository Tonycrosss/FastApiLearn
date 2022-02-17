import json
import pytest
from typing import List
from models.schemas import Book


@pytest.mark.smoke_test
@pytest.mark.parametrize('q', [['book1', 'book4'], ['book5', 'book6']])
def test_get_book(api_client, q: List[str]):
    res = api_client.get(
        path='/book',
        params={'q': q}
    )
    expected_result = q
    fact_result = res.json()
    print(f"Expected result was {expected_result} an the fact result is {fact_result}")
    assert expected_result == fact_result


test_book_dict = {
    "title": "Magic",
    "writer": "string",
    "duration": "string",
    "date": "2022-02-17",
    "summary": "string",
    "genres": [
        {
            "name": "string"
        }
    ],
    "pages": 1
}


@pytest.mark.parametrize('item', [test_book_dict])
def test_create_book(api_client, item: Book):
    res = api_client.post(
        path='/book',
        content=json.dumps(item)
    )
    expected_result = item
    actual_result = res.json()
    assert expected_result == actual_result