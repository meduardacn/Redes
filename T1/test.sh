echo "NRZI"
python3 encode.py nrzi 616263
python3 encode.py nrzi A0C301
python3 encode.py nrzi 012012
python3 decode.py nrzi -+-----++-++++---+----+-
python3 decode.py nrzi -++----++-+++----+----+-
python3 decode.py nrzi -+-----+-+---------+++--
echo ""
echo "MDIF"
python3 encode.py mdif 616263
python3 encode.py mdif A0C301
python3 encode.py mdif 012012
python3 decode.py mdif -+-++-+-+-+-+-+--++-+-+-+-+--++-+-+-+-+-+-+-+--+
python3 decode.py mdif -++++++-+-+-+-+--++-+-+------++-+-+-+-+-+-+-+--+ # ERRO / F0CF01
python3 decode.py mdif +-++++--+-+-+--+-+-++-+-+---+-+-+-+-+--+-+-++-+- # ERRO / 212412
echo ""
echo "HDB3"
python3 encode.py hdb3 616263
python3 encode.py hdb3 A0C301
python3 encode.py hdb3 012012
python3 decode.py hdb3 +00+000-00+-00-+00+-00+0 
python3 decode.py hdb3 000+00+-++-00-+00-+000-+ # ERRO / 1C263
python3 decode.py hdb3 +--+00+00+-00-+-+00+000- # ERRO / E00301
echo ""
echo "8B6T"
python3 encode.py 8b6t 616263
python3 encode.py 8b6t A0C301
python3 encode.py 8b6t 012012
python3 decode.py 8b6t +0+-00-0-0+0+0+00-
python3 decode.py 8b6t +-+-00-000+0+0+00-
python3 decode.py 8b6t 0++-+0-+--00-0-+0+
echo ""
echo "6B8B"
python3 encode.py 6b8b 616263
python3 encode.py 6b8b A0C301
python3 encode.py 6b8b 012012
python3 decode.py 6b8b -++-+++-+--+++---++-+++-+--+++-- # 012012 / KeyError: '10110011'
python3 decode.py 6b8b +-----+-+++--+--+---+++-++----+- 
python3 decode.py 6b8b +-+---+-+---+---+---+----+-++++- # ERRO / KeyError: '11110011'