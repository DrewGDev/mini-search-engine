import pytest

from src.domain.term_frequency import get_concordance
from src.domain.vector_space import VectorCompare

@pytest.mark.asyncio
async def test_get_concordance():
    text = "teste de busca busca"
    result = await get_concordance(text)

    assert result == {"teste": 1, "de": 1, "busca": 2}

@pytest.mark.asyncio
async def test_relation_identical_texts():
    vector_compare: VectorCompare = VectorCompare()
    bag_of_terms = {"python": 1, "rag": 1}

    assert await vector_compare.relation(bag_of_terms, bag_of_terms) == pytest.approx(1.0)

@pytest.mark.asyncio
async def test_relation_differently_texts():
    vector_compare: VectorCompare = VectorCompare()
    bag_one = {"backend": 1}
    bag_two = {"frontend": 1}

    assert await vector_compare.relation(bag_one, bag_two) == 0.0

@pytest.mark.asyncio
async def test_search_ranking():
    vector_compare: VectorCompare = VectorCompare()
    
    simulated_index = {
        1: await get_concordance("cachorro quente é bom"),
        2: await get_concordance("gato legal"),
        3: await get_concordance("o cachorro e o gato")
    }
    
    results = await vector_compare.search("cachorro", simulated_index)
    
    # Just the documents 1 and 3 has the word "cachorro"
    assert len(results) == 2
    
    # The document 1 must win from 3, because the word "cachorro" represents
    # a larger chunk of text (text 1 is smaller than text 3).
    first_place_id = results[0][0]
    second_place_id = results[1][0]
    
    assert first_place_id == 1
    assert second_place_id == 3