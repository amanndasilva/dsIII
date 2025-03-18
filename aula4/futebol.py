time1 = int(input("Insira os gols do time 1: "))
time2 = int(input("Insira os gols do time 2: "))

if time1 > time2:
    print("Vitoria do time 1!")
elif time1 == time2:
    print("Empate!")
else:
    print("Vitoria do time 2!")