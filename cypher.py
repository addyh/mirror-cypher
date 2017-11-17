def cypher(txt):
    ab = "qwertasdfzxcbnmhjklyuiop"
    code = list(txt.lower())

    for i,a in enumerate(code):
        for j,b in enumerate(ab):

            if (a == b):
                x = (23 - j)
                code[i] = ab[x]
                
    return "".join(code)
    
