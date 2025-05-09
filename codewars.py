# Solution to 'Even or Odd': 
def even_or_odd(number):
    return "Even" if number%2 == 0 else "Odd"

# Solution to 'Convert a Number to a String':
def number_to_string(num):
    return str(num)

# Solution for 'Remove String Spaces':
def no_space(x):
    return x.replace(' ', '') 

# Solution for 'Vowel Count(if you want to try a challenge with loops!)': 
def get_count(sentence):
    count = 0 
    vowel = ['a', 'e', 'i', 'o', 'u']
    for char in sentence:
        if char in vowel: 
            count += 1
            
    return count 

