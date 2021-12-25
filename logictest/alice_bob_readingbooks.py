class Book:
    def __init__(self, time, alice, bob) -> None:
        self.time=time
        self.alice=alice
        self.bob=bob

        


def solve(totalChosenBooks, listBook):
    ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
    list_result = []
    total_choose = 0
    list_read_alice = []
    list_read_bob = []

    for idx, item in enumerate(listBook):
        if item.alice == 1 and item.bob == 1:
            total_choose += 1
            list_result.append(f"Alice & Bob read {ordinal(idx+1)} book together")
        elif item.alice == 1:
            list_read_alice.append(idx)                     
        elif item.bob == 1:
            list_read_bob.append(idx)   

    if total_choose <= 0:
        result = "Output get -1 cause:\n"
        if len(list_read_alice) > 0:
            alice_text = " and ".join(list_read_alice)
            result += f"Alice can only read {len(list_read_alice)} books ({alice_text})\n"
        
        if len(list_read_bob) > 0:
            bob_text = " and ".join(list_read_bob)
            result += f"Bob can only read {len(list_read_bob)} books ({bob_text})\n"

        return result
    else:
        result=""
        total_hours = 0
        for x in range(totalChosenBooks):
            if x < len(list_read_alice) and x < len(list_read_bob):
                ordinal_alice = ordinal(list_read_alice[x]+1)
                ordinal_bob = ordinal(list_read_bob[x]+1)
                result += f"Alice read {ordinal_alice} book & Bob read {ordinal_bob} book.\n"
                if ordinal_alice == ordinal_bob:
                    total_hours += listBook[x].time
                else:
                    total_hours += listBook[list_read_alice[x]].time + listBook[list_read_bob[x]].time
                

        result_title = f"Output get {total_hours} with:\n"

        result += "".join(list_result)
        return result_title + result
