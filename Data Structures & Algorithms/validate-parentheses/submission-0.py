class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_pairs = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for ch in s:
            if ch in matching_pairs:
                stack.append(ch)
            elif ch in matching_pairs.values():
                if len(stack) == 0:
                    return False

                if matching_pairs[stack[-1]] == ch:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0