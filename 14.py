def main():
    strs = ["reflower","flow","flight"]
    if (len(strs)==1):
        print(strs)
    min_str = min(strs, key = len)
    min_length = len(min_str)
    for i in range(min_length, 0, -1):
        print(i)
        dd = 1
        s = min_str[0 : 0 + i]
        for str in strs:
            if s != str[0: 0 + i]:
                dd = 0
        if (dd == 1):
            print(s)
    print("kien")

if __name__ == "__main__":
    main()