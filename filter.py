companies=["accenture","wipro","IBM","L&T"]
def vowels(companey):
    vow="AEIOUaeiou"
    for letter in companey:
        if letter in vow:
            return companey
print(list(filter(vowels,companies)))
