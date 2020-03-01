import sys
import CryptoTools


if __name__ == "__main__":
    try:
        inName = sys.argv[1]
    except:
        print("Arguments not passed correctly")
        exit(1)

    f = open(inName, "r")
    if f.mode == 'r':
        letters = f.read()
    letters = CryptoTools.format_list(letters, 1)
    psiValue = CryptoTools.psi_test(letters)

    letters = CryptoTools.bestCaesarCipher(letters)
    print(psiValue)

    f1 = open("oneSolution.txt", "w")
    for i in letters:
        f1.write(i)

