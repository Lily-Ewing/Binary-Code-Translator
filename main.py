import binary_code

code = input('Type "encode" to encode or "decode" to decode.\n').lower()
#encode
if code == "encode":
    encode_text = input("What do you want to encode?\n")
    encode_text.replace(" ", "")
    encoded_code = []
    encoded_letters = []
    for letter in encode_text:
        encoded_letters += letter
    for user_letter in encoded_letters:
        for index, letter in enumerate(binary_code.alphabet):
            if user_letter == letter:
                encoded_code.append(binary_code.binary_num[index])
    print(" ".join(encoded_code))

#decode
if code == "decode":
    decode_text = input("What do you want to decode?\n")
    decoded_code = []
    decoded_numbers = decode_text.split()
    for user_number in decoded_numbers:
        for index, number in enumerate(binary_code.binary_num):
            if user_number == number:
                decoded_code.append(binary_code.alphabet[index])
    print("".join(decoded_code))
    
