def count_word_frequency(sentence):
   
    sentence = sentence.lower()
    
    words = sentence.split()
    
    
    frequency_dict = {}
   
    for word in words:
        
        if word in frequency_dict:
            frequency_dict[word] += 1
        
        else:
            frequency_dict[word] = 1
            
    return frequency_dict

input_sentence = "The quick brown fox jumps over the lazy dog"
result = count_word_frequency(input_sentence)

print("Word Frequencies:")
print(result)
