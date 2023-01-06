from string import ascii_letters,ascii_lowercase
toDecrypt = str("nanzrevpnacebsrffvbanyenyylqevirejvgugurubbavtnaenpvatqvivfvbasbezreylxabjanfgurzbafgrejbeyqenyylgrnzoybpxjnfnyfbbarbsgurpbsbhaqrefbsqpfubrfurnyfbpbzcrgrqvaznalnpgvbafcbegfriragfvapyhqvatfxngrobneqvatfabjobneqvatnaqzbgbpebffnsgrefryyvatuvfbjarefuvcbsqpfubrfoybpxfuvsgrquvfohfvarffsbphfgbubbavtnavaqhfgevrfnanccneryoenaqsbenhgbraguhfvnfgfurjnfgurpbbjarenaqnggurpbzcnalorsberuvfqrngu")
abecedazjedlaDeda = ["a","b", "c", "d", "e", "f", "g" ,"h" ,"i", "j" ,"k" ,"l", "m" ,"n", "o", "p", "q", "r" ,"s" ,"t" ,"u" ,"v" ,"w", "x", "y" ,"z"]
array = []
def split_str(toDecrypt):
    return [c for c in toDecrypt]
arrayDecryptToneviem = split_str(toDecrypt)
dekryptovanaarraynacisielkahaha = [ascii_letters.index(letter) + 1 for letter in arrayDecryptToneviem]
for pismenko in dekryptovanaarraynacisielkahaha:
    newPismenko = pismenko - 13
    if newPismenko<0:
      pismenkoZero = newPismenko +26
      array.append(pismenkoZero)
    else:
     array.append(newPismenko)
    
print(array)
def convert_to_letters(array: list) -> str:
  
    letters = [ascii_lowercase[num - 1] for num in array]
  
    return ''.join(letters)
    
letters = convert_to_letters(array)
print(letters)


