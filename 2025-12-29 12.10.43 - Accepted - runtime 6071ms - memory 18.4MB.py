class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        
        # Count frequency of each character
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1
        
        # Perform t transformations
        for _ in range(t):
            new_freq = [0] * 26
            for i in range(26):
                if freq[i] > 0:
                    if i == 25:  # 'z' -> 'ab'
                        new_freq[0] = (new_freq[0] + freq[i]) % MOD
                        new_freq[1] = (new_freq[1] + freq[i]) % MOD
                    else:  # other chars -> next char
                        new_freq[i + 1] = (new_freq[i + 1] + freq[i]) % MOD
            freq = new_freq
        
        return sum(freq) % MOD