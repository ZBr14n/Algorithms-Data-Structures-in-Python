"""
Given a phone number, return all valid words that can be created using that phone number.

For instance, given the phone number 364
we can construct the words ['dog', 'fog'].

Here's a starting point:

lettersMaps = {
    1: [],
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
    0: []
}

validWords = ['dog', 'fish', 'cat', 'fog']

def makeWords(phone):
  #Fill this in

print(makeWords('364'))
# ['dog', 'fog']


-use dictionaries, match "364" to it.
-after a digit is matched in the dict, we get the corresponding array that is returned.
-we need to modularize the code and retrieve all the correspoinding arrays for each digit.
-use extend() to merge all the arrays together.
-use two for loops to loop thru validWords array and then check to see if each character
matches the list of letters.

"""

# 364, 
def extendArrays(s):
  lettersMaps = {
      1: [],
      2: ['a', 'b', 'c'],
      3: ['d', 'e', 'f'],
      4: ['g', 'h', 'i'],
      5: ['j', 'k', 'l'],
      6: ['m', 'n', 'o'],
      7: ['p', 'q', 'r', 's'],
      8: ['t', 'u', 'v'],
      9: ['w', 'x', 'y', 'z'],
      0: []
  }  
  store=[]
  for digit in s:
    if int(digit) in lettersMaps:
      store.extend(lettersMaps.get(int(digit)))
  
  return store


def makeWords(phone):
  
  validWords = ['dog', 'fish', 'cat', 'fog']
  keep=[]
  for word in validWords:
    for char in word:
      if char not in extendArrays(phone):
        break
    else:
      keep.append(word)
  
  return keep

print(makeWords("79"))