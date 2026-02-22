class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        # """
        result = []
        
        for word in words:
            weight = 0
            base = ord("a")
            z = ord("z")

            for char in word:
                weight += weights[ord(char) - base]

            modulo = weight % 26
            result.append(chr(z - modulo))
            
        return "".join(result)
