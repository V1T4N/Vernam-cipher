# -*- coding: utf-8 -*-

import random

message = raw_input("Enter a messege >>>")

message_list = list(message)

message_ascii = [""]*len(message)
message_bit = [""]*len(message)


for i in range (0,len(message)):                    #入力された文字をASCIIコード化し，さらにそれを２進数に変換してリストに格納する
    message_ascii[i] = ord(message_list[i])         #10進数のACSIIコード化
    message_bit[i] = format(message_ascii[i],'08b') #2進数に変換


message_bit_temp = "".join(message_bit)             #入力された文字の２進数リストを結合する

bit_number = "0" + str(len(message)*8) +"b" #入力された文字のビット数の取得(0b{n}の形)

key = random.randint(0, 2**(len(message)*8)) #復号のための鍵は入力された文字数分のビットの最大値以下でランダムに生成される
key_bit = format (key,bit_number)            #鍵を二進数に変換

message_temp = int(message_bit_temp,2)      #結合した２進数表記の文字列を10進数に変換する






print "Your encrypted message is[" + format (message_temp ^ key,bit_number) + "]"
print "Your key is [" +key_bit + "]"

print "Your message is " + str(len(message)*8) + "bits" 






encrypted_message = int(format (message_temp ^ key,bit_number),2)   #入力された文字を排他的論理和によって暗号化する．　復号のために10進数の整数型に直しておく


print "Your encrypted message is[" + format (message_temp ^ key,bit_number) + "]" ##表示(2進数)
print "Your key is [" +key_bit + "]"

print "Your message is " + str(len(message)*8) + "bits" 







decrypted_message = format(encrypted_message ^ key,bit_number)      #復号

decrypted_message_list_bit = [decrypted_message[i: i+8] for i in range(0, len(decrypted_message), 8)]
#復号された文字は2進数表記なので８ビットごとに分けてリストに格納する．


decrypted_message_list = [""]*len(message)
decrypted_message_list_ascii = [""]*len(message) #リストの定義

for i in range (0,len(message)):                                        ##復号された2進数表記のリストをASCII文字に直す
    decrypted_message_list[i] = int(decrypted_message_list_bit[i],2)
    decrypted_message_list_ascii[i] = chr(decrypted_message_list[i])



ans = "".join(decrypted_message_list_ascii)         ##リストを結合する

print "." +"\n"
print "Decrypting..." +"\n"
print "." +"\n"

print "Your decrypted message is["+ ans + "]"