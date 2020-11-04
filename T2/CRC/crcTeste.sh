python3 crc_encoder.py redes 10101 # 72365964C659736
python3 crc_decoder.py 72365964C659736 10101 # redes
python3 crc_decoder.py 72365964C759736 10101 # red_s ERRO nos caracteres: [4]
python3 crc_decoder.py 32365964C659716 10101 #---
python3 crc_encoder.py politecnica 10101 # 7096F16CE69A7486596326E469A632618
python3 crc_decoder.py 7096F16CE69A7486596326E469A632618 10101 # politecnica
python3 crc_decoder.py 7096F16CE69A74865D6326E469A632618 10101 # polit_cnica  ERRO nos caracteres: [6]
python3 crc_decoder.py 7096F16CE6BA7486596326E069A632618 10101 #---
python3 crc_encoder.py hamming 10101 # 68F6186DB6DB69A6E4673
python3 crc_decoder.py 68F6186DB6DB69A6E4673 10101 # hamming
python3 crc_decoder.py 68F6186DB65B69A6E4673 10101 # ham_ing ERRO nos caracteres: [4]
python3 crc_decoder.py 68F6186DB69B69A6F4673 10101 # ham_i_g ERRO nos caracteres: [4, 6]
###############################################################
# 21  if int(result,16) != 0:

# python3 crc_decoder.py 32365964C659716 10101
# _ede_
# ERRO nos caracteres: [1, 5]
# Traceback (most recent call last):
#   File "crc_decoder.py", line 41, in <module>
#     main(data[1], data[2])
#   File "crc_decoder.py", line 30, in main
#     response = decode(letter,generator)
#   File "crc_decoder.py", line 21, in decode
#     if int(result) != 0:
# ValueError: invalid literal for int() with base 10: 'a'

# python3 crc_decoder.py 7096F16CE6BA7486596326E069A632618 10101
# pol_tec_ica
# ERRO nos caracteres: [4, 8]
# Traceback (most recent call last):
#   File "crc_decoder.py", line 41, in <module>
#     main(data[1], data[2])
#   File "crc_decoder.py", line 30, in main
#     response = decode(letter,generator)
#   File "crc_decoder.py", line 21, in decode
#     if int(result) != 0:
# ValueError: invalid literal for int() with base 10: 'a'
