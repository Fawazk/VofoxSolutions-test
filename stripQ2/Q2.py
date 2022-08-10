strips = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

def test(digit):
    count = 0
    
    for i in range(len(digit)):
        count += strips[ord(digit[i]) - 48]
        
    return count
    
print(test("2"))