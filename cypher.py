def caeser_cypher(cypher_input, shift_key): # defining "caeser_cypher"
   
    final_cypher = ""
    for char in cypher_input:

        if char.isalpha():  # This checks if the character is a letter
            
            if char.islower():  # This checks if the character is lowercase
                ascii_value = ord('a')
            
            else:  # The character is uppercase
                ascii_value = ord('A')

            # This ecrypts the characters by shifting it by 15
            encrypted_char = chr((ord(char) - ascii_value + shift_key) % 26 + ascii_value)
            final_cypher += encrypted_char

        else:
            # characters that are not alphabetic remain unchanged
            final_cypher += char

    return final_cypher 

cypher_input = input("Enter a message to be encrypted: ") # User inputs their message here
shift_key = 15 # This is how many shifts of characters once encrypted

cypher = caeser_cypher(cypher_input, shift_key)# Encryption
print("Your cyphered message:",cypher) # Encryption result