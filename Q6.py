task = "ThiS iS aWeSoMe"

def reverse_word(sentence):
    
    words = sentence.split()                        
    for i in range(1,(len(words)+2)//2):            
        words[i-1],words[-i] = words[-i],words[i-1]   
    reversed_sentence = " ".join(words)             
    return reversed_sentence

print(reverse_word(task))
