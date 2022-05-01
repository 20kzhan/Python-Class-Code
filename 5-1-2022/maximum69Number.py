def maximum69Number(num: int) -> int:
    l = [x for x in str(num)] # 9969
    # l = ['9', '6', '9', '6']
    if '6' in l:
        for i, x in enumerate(l):
            if x == '6':
                l[i] = '9'
                return int(''.join(l))
    else:
        return num
