#sh test.sh  
python3 simulador.py a.txt n1 n2 hello
echo ""
python3 simulador.py a.txt n1 n2 helloworld
echo ""
python3 simulador.py a.txt n1 n3 hello
echo ""
python3 simulador.py a.txt n1 n3 helloworld
echo ""
echo "TRABALHO"
python3 simulador.py topo1.txt n1 n2 redes # 
echo ""
python3 simulador.py topo1.txt n1 n3 redes #
echo ""
python3 simulador.py topo1.txt n2 n3 computador #
echo ""
python3 simulador.py topo2.txt n1 n2 computador #
echo ""
python3 simulador.py topo2.txt n1 n3 computador #
echo "" 
python3 simulador.py topo2.txt n1 n4 computador #
echo ""
python3 simulador.py topo2.txt n2 n3 computador #
echo ""
python3 simulador.py topo2.txt n2 n4 computador #
echo ""
python3 simulador.py topo2.txt n3 n4 computador #
echo ""
# bug with ttl, r => n tll should be 7
# line 298 must be return 
# print all mac value
# r => r comunication