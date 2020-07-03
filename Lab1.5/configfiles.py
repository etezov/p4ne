import glob

dir=glob.glob("E:\работа\Python\p4ne_training\config_files\*.txt")

iplist=[]

for i in dir:
    with open(i) as f:
        for l in f:
            if (l.find("ip address")>=0) & (l.find(".")>=0):
                l = l.strip()
                l = l.replace("ip address", "")
                iplist.append(l)
iplist = list(set(iplist))

for i in iplist:
    print(i)
