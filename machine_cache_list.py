def machine_cache_list(machine: str, cache: int) -> list:
    """
    Finds all machines with CACH values greater than the cache parameter.
    """
    machines = open(machine, "r+")
    machine = machines.read().split("\n")
    machines.close()
    machine_cache_req = []
    for i in range(1, len(machine) - 1):
        if int(machine[i].split(",")[5]) >= cache:
            machine_cache_req.append({"vendor": machine[i].split(",")[0],
                                      "model":  machine[i].split(",")[1],
                                      "MYCT":   int(machine[i].split(",")[2]),
                                      "MMIN":   int(machine[i].split(",")[3]),
                                      "MMAX":   int(machine[i].split(",")[4]),
                                      "PRP":    int(machine[i].split(",")[6]),
                                      "ERP":    int(machine[i].split(",")[7])})
    
    return machine_cache_req
machine_cache_list("machine.csv", 22
                   )