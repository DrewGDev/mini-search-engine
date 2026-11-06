import math

from src.domain.term_frequency import get_concordance


class VectorCompare:
    async def magnitude(self, concordance: dict[str, int]) -> float:
        """Calculate the magnitude of vector."""
        total = sum(count ** 2 for count in concordance.values())
        return math.sqrt(total)

    async def relation(self, concordance_one: dict[str, int], concordance_two: dict[str, int]) -> float:
        """
        Calculate the cos similarity between two vector words.
        Returns a value between 0 and 1 (how bigger, more relevant).
        """
        topvalue = 0.0
        
        for word, count in concordance_one.items():
            if word in concordance_two:
                topvalue += count * concordance_two[word]
                
        mag_mult = await self.magnitude(concordance_one) * await self.magnitude(concordance_two)
        
        if mag_mult != 0:
            return topvalue / mag_mult
        return 0.0
    
    async def search(self, query: str, index: dict[int, dict[str, int]]) -> list[tuple[int, float]]:
        query_concordance = await get_concordance(query)
        matches = []

        for doc_id, doc_concordance in index.items():
            score = await self.relation(query_concordance, doc_concordance)
            if score > 0:
                matches.append((doc_id, score))

        matches.sort(key=lambda x: x[1], reverse=True)
        return matches