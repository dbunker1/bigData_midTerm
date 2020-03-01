import string
from itertools import permutations


# Run this method to test if the code is a caeser cipher
def bestCaesarCipher(letters):
    key = 1
    asciiLetters = list(string.ascii_lowercase)
    counts = []
    for char in asciiLetters:
        counts.append((letters.count(char), char))
    counts.sort(reverse=True)
    print(counts)

    x = 0
    max = maximizePower(counts)[1]
    while x in range(0, 26):
        letters = encryptCaesar(letters, key)
        counts = []
        for char in asciiLetters:
            counts.append((letters.count(char), char))
        counts.sort(reverse=True)
        if letters.count('e') + letters.count('t') + letters.count('o') == max:
            print(counts[x])
            break
        x = x + 1

    return ''.join(letters)

# encrypt for a caesar cipher
def encryptCaesar(plain, key):
    encrypted_letters = []
    for letter in plain:
        if not ord(letter.lower()) >= ord('a') and ord(letter.lower()) <= ord('z'):
            encrypted_letters.append(letter)
            continue
        encrypted_letters.append(chr(ord('a')+((ord(letter.lower()) + int(key) - ord('a'))%26)))

    return encrypted_letters

# Method for Caesar Cipher
def maximizePower(counts):
    maxKey = 0
    key = 0
    power = 0
    tempPower = 0
    commonChars = ["e", "t", "o"]
    for x in commonChars:
        if ord(x) < ord(counts[0][1]):
            key = ord(counts[0][1]) - ord(x)
        else:
            key = 26 - (ord(x) - ord(counts[0][1]))
        for y in commonChars:
            newChar = chr(ord('a')+((ord(y) + key - ord('a'))%26))
            for c in counts:
                if c[1] == newChar:
                    val = c[0]
                    break
            tempPower = tempPower + val
        if tempPower > power:
            power = tempPower
            maxKey = key
        tempPower = 0
        key = 0
    return (maxKey, power)


def format_list(letter_list, tuple_size = 1):
    new_letters = ""
    ascii_lower = string.ascii_lowercase
    for letter in letter_list.lower():
        if not ascii_lower.find(letter) == -1:
            new_letters = new_letters + letter
    if tuple_size > 1:
        temp = []
        for i in range(0, len(new_letters)-1, tuple_size):
            temp.append(new_letters[i] + new_letters[i+1])
        new_letters = temp
    return new_letters


def psi_test(letter_list):
    letter_set = set(letter_list)
    psi = 0
    for letter in letter_set:
        num = letter_list.count(letter)
        psi = psi + (num/len(letter_list)*(num/len(letter_list)))
    return psi


def find_permutation(letter_list, lower_bound, upper_bound):
    for i in range(lower_bound, upper_bound):
        perm_list = []
        count = 1
        for j in range(0, len(letter_list), i):
            perm_list.append(list(permutations(letter_list[j:i*count])))
            count = count + 1
        constructed_lists = []
        temp = ""
        if len(perm_list[len(perm_list)-1]) < len(perm_list[0]):
            perm_list = perm_list[0:len(perm_list)-1]

        for k in range(0, len(perm_list[0])):
            for m in perm_list:
                curr = ''.join(m[k])
                temp = temp + curr
            constructed_lists.append(temp)
            temp = ""
        for x in constructed_lists:
            y = format_list(x, 2)
            psi = psi_test(y)
            if psi > 0.06:
             print(psi)
             print(x)
             a_set = set(y)
             print(len(a_set))
             print(a_set)
             print("Permutation Length: " + str(i))
