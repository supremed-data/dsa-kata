class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        # """
        # TODO: 이 부분 효율화
        mapped = "abcdefghijklmnopqrstuvwxyz"
        reversed_mapped = mapped[::-1]
        result = ""
        
        for word in words:
            weight = 0

            for letter in word:
                # TODO: index 계산
                letter_ind = ord(letter) - 97
                weight += weights[letter_ind]

            # TODO: mapped character 구해서 더하기
            modulo = weight % 26
            mapped_char = reversed_mapped[modulo]
            result += mapped_char

        return result
