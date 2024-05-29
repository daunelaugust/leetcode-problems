def encode(self, strs: List[str]) -> str:
    if strs == []:
        return []
    result = ('.').join(strs)
    return result

def decode(self, s: str) -> List[str]:
    if s == []:
        return []
    string = s.split('.')
    return string