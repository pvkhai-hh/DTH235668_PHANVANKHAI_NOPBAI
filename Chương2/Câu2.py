t=int(input("Nhập số giây: "))
hour=(t//3600)%24
minute=(t%3600)//60
second=(t%3600)%60
if(hour>=12):
    hour-=12
    str="PM"
else : str="AM"
print(hour,":",minute,":",second,str)