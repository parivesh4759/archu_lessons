vowels=['a','e','i','o','u']
Name="android_paranoid"
namelist=list(Name)
result = {}
for letter in namelist:
         if letter in vowels and letter in result:
            result[letter]=result[letter]+1
         elif letter in vowels and letter not in result:
             result[letter] = 1
         else:
             continue
print(result)

#Using set instead
vowels=['a','e','i','o','u']
Name="android_paranoid"
namelist=list(Name)
setresult= set()
for letter in namelist:
    if letter in vowels:
            setresult.add(letter)
    else:
        continue
print(setresult)









