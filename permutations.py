def permutations(array):
    if len(array)==0:
        return [array]
    elif len(array) == 1:
        return [array]
    else:
        list = []
        for i in array:
            elements = [x for x in array if x != i]
            result = permutations(elements)
            for it in result:
                list.append([i] + it)

        return list
