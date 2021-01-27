import os
from discord_webhook import DiscordWebhook
def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

def list_string(l):
    out_str=' '.join(map(str, l))
    return out_str

def formatter(catergory):
    return chunkstring(list_string(catergory),1950)

def discord_output_split(out):
    print("In")
    low=[]
    medium=[]
    high=[]
    critical=[]
    info=[]
    for line in out:
        if("[low]" in line):
            low.append(line)
        if("[medium]" in line): 
            medium.append(line)
        if("[high]" in line):
            high.append(line)
        if("[critical]" in line):
            critical.append(line)
        if("[info]" in line):
            info.append(line)
    for f in formatter(low):
        DiscordWebhook(url="DISCORD WEB HOOK HERE",content=f).execute()
    for f in formatter(medium):
        DiscordWebhook(url="DISCORD WEB HOOK HERE",content=f).execute()
    for f in formatter(high):
        DiscordWebhook(url="DISCORD WEB HOOK HERE",content=f).execute()
    for f in formatter(critical):
        DiscordWebhook(url="DISCORD WEB HOOK HERE",content=f).execute()
    for f in formatter(info):
        DiscordWebhook(url="DISCORD WEB HOOK HERE",content=f).execute()
for i in range(3,32,2):
        n=str(i).zfill(2)
        webhook=DiscordWebhook(url="DISCORD WEB HOOK HERE",content="Starting {}".format(n))
        webhook.execute()
        cmd=("~/go/bin/nuclei -c 500 -l file{}.txt -silent -t ~/Tools/nuclei-templates/ -o O_{}.txt".format(n,i)) # EDIT it accordingly
        os.system(cmd)
        f=open("O_{}.txt".format(i),"r")
        out=f.readlines()
        # print(out)
        discord_output_split(out)
        # out_str=list_string(out)
        # itr=list(chunkstring(out_str,1950))
        webhook=DiscordWebhook(url="DISCORD WEB HOOK HERE",content="Finished {}".format(n))
        webhook.execute()
