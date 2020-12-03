# Move n-1 disks from A to B using C as the temp pillar
# Move nth disk from A to C
# Move n-1 disk from B to C using A as the temp pillar


def toh(n, src=None, temp=None, dest=None):
    if n == 1:
        print(src, dest)

    toh(n-1, src, dest, temp)
    toh(n, src, dest)
    toh(n-1, temp, src, dest)
