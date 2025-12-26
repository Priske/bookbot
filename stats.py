def word_count(booktext):
    woordenlist= booktext.split()
    return(f"Found {len(woordenlist)} total words")

def count_char(booktext):
    count= {}
#    text=booktext.lower()
    for char in booktext.lower():
        if(char not in count):
            count[char] = 1
        else:
            count[char] += 1
    return count 

def sorted_dict(d):
    chars = list(d.items())
    chars.sort(key=lambda x: x[1], reverse=True)
    return dict(chars)
    
    
    
  
