# mirror-cypher
### Decode and encode secret messages!

Try it out. Encode a secret message with it, and send it to a friend to see if they can figure out how to decode it! (If they need a hint, tell them to look at their keyboard and imagine it was mirrored from left-to-right down the middle.)

```python
# An encoding/decoding cypher algorithm
# That acts as if your keyboard buttons have been mirrored in place!
def cypher(txt):
    
    # Define an alphabet, as a mirror,
    # first letter (q) encodes to last letter (p)
    # second (w) = second to last (o),
    # (e) -> (i) .... etc.
    ab = "qwertasdfzxcbnmhjklyuiop"
    code = list(txt.lower())

    # Loop through the inputted text
    for i,a in enumerate(code):
        
        # For each input letter,
        # Also loop through the alphabet string (ab)
        for j,b in enumerate(ab):

            # Until we come accross a letter that matches
            if (a == b):

                # Subtracting the index of the matching letter in the alphabet
                # from the length of the alphabet string minus one (23)
                # gives us the mirrored index of the character
                x = (23 - j)

                # Now, use this mirrored index to set the mirrored character
                # in the encoded string. Letters that can't be mirrored
                # (g and v) simply stay the same in the cypher
                code[i] = ab[x]
                
    return "".join(code)
```
