#!/usr/bin/python
import sys
lines = sys.stdin.readlines()

l1 = []
l2 = []
l3 = []
l4 = []
l = []

lemma = sys.argv[1]

out1 = open('oracle_out.txt', 'a')

out1.write("start_oracle\n")
out1.write("________________________\n")

for line in lines:
    out1.write(line)
    num = line.split(':')[0]
    if lemma == "EAP_vshared_secret":
        if "KU" in line:
            l1.append(num)
        elif "Clnt" in line:
            l2.append(num)
        elif "Serv" in line:
            l3.append(num)
        else:
            l4.append(num)
    elif lemma == "Noise_vshared_secret":
        if "KU" in line:
            l1.append(num)
        elif "Clnt" in line:
            l2.append(num)
        elif "Serv" in line:
            l3.append(num)
        else:
            l4.append(num)
    else:
        exit(0)

out1.write("________________________\n")
out1.write("fin_oracle\n")

ranked = l1 + l2 + l3 + l4

for i in ranked:
    print(i)
