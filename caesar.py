import sys

###########
# FUNÇÕES #
###########

def showHelp():
    print("""
        arguments: 
            -h | mostra a lista de argumentos
            -c "CRYPT" | mensagem a ser criptografada

            -d "DECRPT" | mesagem a ser decriptografada

            -r ROT | número de rotações 
    """)
    exit()

def formatText(text):
    return text.replace(" ", "")

##########
# CÓDIGO #
##########

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
operationType = 0

args = sys.argv[1:len(sys.argv)]

if "-r" in args:
    global rotateAmount
    rotateAmount = int(args[args.index("-r") + 1])
else:
    showHelp()

if "-c" in args:
    global rawEncryptText
    rawEncryptText = args[args.index("-c") + 1].upper()

    operationType = 1

    if "-d" in args:
        showHelp()

elif "-d" in args:
    global rawDecryptText
    rawDecryptText = args[args.index("-d") + 1].upper()

    operationType = 2

else:
    showHelp()
    
if "-h" in args:
    showHelp()

if operationType == 1:

    encryptedText = ""

    encryptText = formatText(rawEncryptText)

    for i in range(len(encryptText)):

        if not encryptText[i].isalpha():

            encryptedText += encryptText[i]

        else:

            actualPosition = alphabet.find(encryptText[i])

            replacePosition = actualPosition + rotateAmount

            if replacePosition > len(alphabet) - 1:
                __temp = replacePosition - len(alphabet)
                replacePosition = __temp

            replaceChar = alphabet[replacePosition]

            encryptedText += replaceChar

    print(f"\nTexto criptografado: {encryptedText}\nRotações: {rotateAmount}\n")

elif operationType == 2:

    decryptedText = ""

    decryptText = formatText(rawDecryptText)

    for i in range(len(decryptText)):

        if not decryptText[i].isalpha():

            decryptedText += decryptText[i]
        
        else:

            actualPosition = alphabet.find(decryptText[i])

            replacePosition = actualPosition - rotateAmount

            if replacePosition < 0:
                __temp = rotateAmount - actualPosition
                replacePosition = len(alphabet) - __temp

            replaceChar = alphabet[replacePosition]

            decryptedText += replaceChar

    print(f"\nTexto decriptografado: {decryptedText}\nRotações: {rotateAmount}\n")