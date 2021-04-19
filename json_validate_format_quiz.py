"""
Input: {'key1':[v1,v2,v3], 'key2':(val1,val2)} -> True
Input: {'key1':[v1,v2,v3 , 'key2':(val1,val2)} -> False
Input: {'key1':[v1,v2,v3 } ], 'key2':(val1,val2)} -> False
"""


def validate_json_format(chars: str) -> bool:
    lookup = {'{': '}', '[': ']', '(': ')'}
    stack = []
    for char in chars:
        if char in lookup.keys():
            stack.append(lookup[char])
        if char in lookup.values():
            if not stack:
                return False
            if char != stack.pop():
                return False


    if stack:
        return False

    return True


if __name__ == "__main__":
    chars = "{'key1':[v1,v2,v3], 'key2':(val1,val2)}"
    chars = "{'key1':[v1,v2,v3 } ], 'key2':(val1,val2)}"
    print(validate_json_format(chars))
