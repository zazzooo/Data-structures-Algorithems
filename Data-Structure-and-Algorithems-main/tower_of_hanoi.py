def TowerOfHanoi(n , from_rod, to_rod, aux_rod, out):
    if n == 1:
        out.write("Move disk 1 from rod "+from_rod+" to rod "+to_rod+"\n")
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod,out)
    out.write("Move disk " + str(n) + " from rod "+ from_rod+" to rod "+to_rod+"\n")
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod,out)


def TowerOfHanoi_for_test(n , from_rod, to_rod, aux_rod, out):
    if n == 1:
        writeToFile(n, from_rod, to_rod, out)
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod,out)
    writeToFile(n, from_rod, to_rod, out)
    # out.write("Move disk " + str(n) + " fwriteToFile(n, from_rod, to_rod, out)rom rod "+ from_rod+" to rod "+to_rod+"\n")
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod,out)

def writeToFile(n, from_rod, to_rod, out):
    out.write('Move disk ' + str(n) + ' from rod ' + from_rod+" to rod "+to_rod+"\n")

out = open("output.txt","a")
TowerOfHanoi_for_test(3, 'A', 'C', 'B',out)
out.write('Finished \n')
out.close()
