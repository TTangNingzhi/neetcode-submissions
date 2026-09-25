class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        start_index = 0
        cur_index = 0
        while cur_index < len(s):
            if s[cur_index] == "#":
                cur_len = int(s[start_index : cur_index])
                decoded_strs.append(s[cur_index + 1 : cur_index + 1 + cur_len])
                start_index = cur_index + 1 + cur_len
                cur_index = start_index
            else:
                cur_index += 1
        return decoded_strs
