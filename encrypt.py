# -*- coding: utf-8 -*-

import random

message = raw_input("Enter a messege >>>")

message_list = list(message)

message_ascii = [""]*len(message)
message_bit = [""]*len(message)


for i in range (0,len(message)):
    message_ascii[i] = ord(message_list[i])
    message_bit[i] = format(message_ascii[i],'08b')


message_bit_temp = "".join(message_bit)

bit_number = "0" + str(len(message)*8) +"b"

key = random.randint(10000, 10000)
key_bit = format (key,bit_number)

message_temp = int(message_bit_temp,2)




#print "message"+ message_bit_temp



print "Your encrypted message is[" + format (message_temp ^ key,bit_number) + "]"
print "Your key is [" +key_bit + "]"

print "Your message is " + str(len(message)*8) + "bits" 


encrypted_message = int(format (message_temp ^ key,bit_number),2)

decrypted_message = format(encrypted_message ^ key,bit_number)

decrypted_message_list_bit = [decrypted_message[i: i+8] for i in range(0, len(decrypted_message), 8)]


decrypted_message_list = [""]*len(message)
decrypted_message_list_ascii = [""]*len(message)

for i in range (0,len(message)):
    decrypted_message_list[i] = int(decrypted_message_list_bit[i],2)
    decrypted_message_list_ascii[i] = chr(decrypted_message_list[i])



ans = "".join(decrypted_message_list_ascii)

print "." +"\n"
print "Decrypting..." +"\n"
print "." +"\n"

print "Your decrypted message is["+ ans + "]"