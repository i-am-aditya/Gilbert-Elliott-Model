from sim2net.packet_loss.gilbert_elliott import GilbertElliott
import random
import pandas as pd

col_names = ['p', 'r', 'h', 'k']
pkt_name = list()
for i in range(1, 10001):
    pkt_name.append("Packet_" + str(i))
col_names.extend(pkt_name)

col_values = list()
prhk = list()
pkt = list()

for i in range(12000):
    p = random.random()
    r = random.random()
    h = random.random()
    k = random.random()
    prhk.append(p)
    prhk.append(r)
    prhk.append(h)
    prhk.append(k)
    for j in range(10000):        
        ge = GilbertElliott([p,r,h,k])
        pl = int(ge.packet_loss()) 
        pkt.append(pl)
    prhk.extend(pkt)
    col_values.append(prhk)
    pkt = list() 
    prhk = list()
    
df = pd.DataFrame(col_values, columns = col_names)
df.to_csv("E:/Documents/SRPF 2020/Packet Delivery Performance/GE-dataset.csv", index = False)