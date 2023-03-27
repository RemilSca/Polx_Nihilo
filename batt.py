

def fajto(p1, p2):
    u1 = p1.get_roster()
    u2 = p2.get_roster()

    u1.slot1.debug()
    u1.slot2.debug()
    u1.slot3.debug()
    u1.slot4.debug()
    u1.slot5.debug()
    u1.slot6.debug()
    u2.slot1.debug()
    u2.slot2.debug()
    u2.slot3.debug()
    u2.slot4.debug()
    u2.slot5.debug()
    u2.slot6.debug()

    check = True

    while check:

        #faza 1
        if u1.slot1 != None and u2.slot1 != None:
            u1.slot1.hp -= u2.slot1.ak - u1.slot1.df
        if u2.slot1 != None and u1.slot1 != None:
            u2.slot1.hp -= u1.slot1.ak - u2.slot1.df

        if u1.slot2 != None and u2.slot2 != None:
            u1.slot2.hp -= u2.slot2.ak - u1.slot1.df
        if u2.slot2 != None and u1.slot2 != None:
            u2.slot2.hp -= u1.slot2.ak - u2.slot1.df

        if u1.slot3 != None and u2.slot3 != None:
            u1.slot3.hp -= u2.slot3.ak - u1.slot1.df
        if u2.slot3 != None and u1.slot3 != None:
            u2.slot3.hp -= u1.slot3.ak - u2.slot1.df

        #check
        if u1.slot1.hp <= 0:
            if u1.slot4 != None:
                u1.slot1 = u1.slot4
                u1.slot4 = None
            else:
                u1.slot1.alive = False
        if u1.slot2.hp <= 0:
            if u1.slot5 != None:
                u1.slot2 = u1.slot5
                u1.slot5 = None
            else:
                u1.slot2.alive = False
        if u1.slot3.hp <= 0:
            if u1.slot6 != None:
                u1.slot3 = u1.slot6
                u1.slot6 = None
            else:
                u1.slot3.alive = False

        if u2.slot1.hp <= 0:
            if u2.slot4 != None:
                u2.slot1 = u2.slot4
                u2.slot4 = None
            else:
                u2.slot1.alive = False
        if u2.slot2.hp <= 0:
            if u2.slot5 != None:
                u2.slot2 = u2.slot5
                u2.slot5 = None
            else:
                u2.slot2.alive = False
        if u2.slot3.hp <= 0:
            if u2.slot6 != None:
                u2.slot3 = u2.slot6
                u2.slot6 = None
            else:
                u2.slot3.alive = False

        if u1.slot1.alive == False and u1.slot2.alive == False and u1.slot3.alive == False:
            check = False
            return p2
        if u2.slot1.alive == False and u2.slot2.alive == False and u2.slot3.alive == False:
            check = False
            return p1

        #status
        try:
            print(f"user1: {u1.slot1.name} hp: {u1.slot1.hp}, {u1.slot2.name} hp: {u1.slot2.hp}, {u1.slot3.name} hp: {u1.slot3.hp}")
            print(f"user2: {u2.slot1.name} hp: {u2.slot1.hp}, {u2.slot2.name} hp: {u2.slot2.hp}, {u2.slot3.name} hp: {u2.slot3.hp}")
        except:
            print("error")

        #faza 2

        if u1.slot1 != None and u2.slot4 != None:
            u1.slot1.hp -= u2.slot4.mg
        if u2.slot1 != None and u1.slot4 != None:
            u2.slot1.hp -= u1.slot4.mg

        if u1.slot2 != None and u2.slot5 != None:
            u1.slot2.hp -= u2.slot5.mg
        if u2.slot2 != None and u1.slot5 != None:
            u2.slot2.hp -= u1.slot5.mg

        if u1.slot3 != None and u2.slot6 != None:
            u1.slot3.hp -= u2.slot6.mg
        if u2.slot3 != None and u1.slot6 != None:
            u2.slot3.hp -= u1.slot6.mg

        #check
        if u1.slot1.hp <= 0:
            if u1.slot4 != None:
                u1.slot1 = u1.slot4
                u1.slot4 = None
            else:
                u1.slot1.alive = False
        if u1.slot2.hp <= 0:
            if u1.slot5 != None:
                u1.slot2 = u1.slot5
                u1.slot5 = None
            else:
                u1.slot2.alive = False
        if u1.slot3.hp <= 0:
            if u1.slot6 != None:
                u1.slot3 = u1.slot6
                u1.slot6 = None
            else:
                u1.slot3.alive = False

        if u2.slot1.hp <= 0:
            if u2.slot4 != None:
                u2.slot1 = u2.slot4
                u2.slot4 = None
            else:
                u2.slot1.alive = False
        if u2.slot2.hp <= 0:
            if u2.slot5 != None:
                u2.slot2 = u2.slot5
                u2.slot5 = None
            else:
                u2.slot2.alive = False
        if u2.slot3.hp <= 0:
            if u2.slot6 != None:
                u2.slot3 = u2.slot6
                u2.slot6 = None
            else:
                u2.slot3.alive = False

        if u1.slot1.alive == False and u1.slot2.alive == False and u1.slot3.alive == False:
            check = False
            return p2
        if u2.slot1.alive == False and u2.slot2.alive == False and u2.slot3.alive == False:
            check = False
            return p1

        #status
        try:
            print(f"user1: {u1.slot1.name} hp: {u1.slot1.hp}, {u1.slot2.name} hp: {u1.slot2.hp}, {u1.slot3.name} hp: {u1.slot3.hp}")
            print(f"user2: {u2.slot1.name} hp: {u2.slot1.hp}, {u2.slot2.name} hp: {u2.slot2.hp}, {u2.slot3.name} hp: {u2.slot3.hp}")
        except:
            print("error")


        #faza 3

        s1 = u1.get_list()
        s2 = u2.get_list()

        for x in s1:
            if x != None:
                if x.mp == x.mpu:
                    x.mp = 0
                else:
                    x.mp += 1

        for x in s2:
            if x != None:
                if x.mp == x.mpu:
                    x.mp = 0
                else:
                    x.mp += 1


        #check
        if u1.slot1.hp <= 0:
            if u1.slot4 != None:
                u1.slot1 = u1.slot4
                u1.slot4 = None
            else:
                u1.slot1.alive = False
        if u1.slot2.hp <= 0:
            if u1.slot5 != None:
                u1.slot2 = u1.slot5
                u1.slot5 = None
            else:
                u1.slot2.alive = False
        if u1.slot3.hp <= 0:
            if u1.slot6 != None:
                u1.slot3 = u1.slot6
                u1.slot6 = None
            else:
                u1.slot3.alive = False

        if u2.slot1.hp <= 0:
            if u2.slot4 != None:
                u2.slot1 = u2.slot4
                u2.slot4 = None
            else:
                u2.slot1.alive = False
        if u2.slot2.hp <= 0:
            if u2.slot5 != None:
                u2.slot2 = u2.slot5
                u2.slot5 = None
            else:
                u2.slot2.alive = False
        if u2.slot3.hp <= 0:
            if u2.slot6 != None:
                u2.slot3 = u2.slot6
                u2.slot6 = None
            else:
                u2.slot3.alive = False

        if u1.slot1.alive == False and u1.slot2.alive == False and u1.slot3.alive == False:
            check = False
            return p2
        if u2.slot1.alive == False and u2.slot2.alive == False and u2.slot3.alive == False:
            check = False
            return p1



