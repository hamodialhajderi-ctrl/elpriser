class Prisobservation:
    def __init__(self, tid, pris):
        self.tid = tid
        self.pris = pris
    def är_dyrt(self):
        return self.pris > 1.50

class ToppPrisObservation(Prisobservation):
    def __init__(self, tid, pris, anledning):
        super().__init__(tid, pris)
        self.anledning = anledning

    

p1 = Prisobservation("08:00", 1.20)
p2 = Prisobservation("14:00", 2.10)


print(p1.är_dyrt())  
print(p2.är_dyrt())  

vip = ToppPrisObservation("18:00", 3.50, "hög efterfrågan")
print(vip.tid)
print(vip.pris)
print(vip.anledning)
print(vip.är_dyrt())
