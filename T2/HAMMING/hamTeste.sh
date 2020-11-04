python3 ham_encoder.py redes # 79962C62B62C79E
python3 ham_decoder.py 79962C62B62C79E # redes
python3 ham_decoder.py 79962D62B62C79E # redes ERRO no caractere  2  -> Correção:  e
python3 ham_decoder.py 79968C62B62C79E #---
python3 ham_encoder.py politecnica # 78067E66064D7AA62C61F67964D61F606
python3 ham_decoder.py 78067E66064D7AA62C61F67964D61F606 # politecnica
python3 ham_decoder.py 78067E66064D7AA62C61F67964D65F606 # politecnica ERRO no caractere  10  -> Correção:  c
python3 ham_decoder.py 78067C66064D7AA62C61F27964D61F606 #---
python3 ham_encoder.py hamming # 64A60666766764D679635
python3 ham_decoder.py 64A60666766764D679635 # hamming
python3 ham_decoder.py 64A60666776764D679635 # hamming ERRO no caractere  4  -> Correção:  m
python3 ham_decoder.py 64A60666666764D679637 # hamming ERRO no caractere  3  -> Correção:  m  ERRO no caractere  7  -> Correção:  g

###################################################################
# python3 ham_decoder.py 79968C62B62C79E 
# rades
# ERRO no caractere  2  -> Correção:  a
# Traceback (most recent call last):
#   File "ham_decoder.py", line 59, in <module>
#     main(data[1])
#   File "ham_decoder.py", line 50, in main
#     response, error = decode(letter)
#   File "ham_decoder.py", line 30, in decode
#     if binaryLetter[xorResult-1] == '1':
# IndexError: string index out of range

# python3 ham_decoder.py 78067C66064D7AA62C61F27964D61F606 
# politecnica
# ERRO no caractere  2  -> Correção:  o
# ERRO no caractere  8  -> Correção:  n
# Traceback (most recent call last):
#   File "ham_decoder.py", line 59, in <module>
#     main(data[1])
#   File "ham_decoder.py", line 50, in main
#     response, error = decode(letter)
#   File "ham_decoder.py", line 30, in decode
#     if binaryLetter[xorResult-1] == '1':
# IndexError: string index out of range