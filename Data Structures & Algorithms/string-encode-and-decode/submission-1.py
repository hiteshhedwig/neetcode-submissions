
class Solution:

    def encode(self, strs: List[str]) -> str:
        output=""
        delimiter = "#"
        for st in strs:
            string_len = len(st)
            output+=str(string_len)
            output+=delimiter
            output+=st
        return output

    def decode(self, s: str) -> List[str]:
        i=0
        output = []
        print(s)
        while (i<len(s)) :
            j=i
            while(s[j]!="#"):
                j+=1
            length = int(s[i:j])
            start = j+1
            end = start+length
            output.append(s[start:end])
            i=end

        return output
