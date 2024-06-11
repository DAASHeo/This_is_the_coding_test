class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        freq = [0] * 26 #알파벳 갯수
        output = []

        for i in range(len(words)):
            if i == 0 :
                for j in words[i]:
                    freq[ord(j) - ord("a")] += 1
            else:
                alphabet = list(set(words[i]))
                for j in alphabet:
                    if words[i].count(j) < freq[ord(j) - ord("a")]:
                        freq[ord(j) - ord("a")] = words[i].count(j)

        for i in range(len(freq)):
            if freq[i] != 0:
                for j in words:
                    if chr(i + ord("a")) not in j:
                        freq[i] = 0
                        break

        for i in range(len(freq)):
            if freq[i] != 0:
                for _ in range(freq[i]):
                    output.append(chr(i + ord("a")))

        return output  