def max_sequence(seq):
    """
    Функция ищет пять соседних элементов списка, сумма значений которых максимальна.
    >>> max_sequence([1, 3, 1, 1, 4, 4, 3, 1, 4, 4, 4, 3, 4, 4, 1, 3, 2, 4, 4, 4])
    [4, 4, 4, 3, 4]
    >>> max_sequence([1, 5, 7, 2, 9, 2, 9, 2, 5, 3, 7, 6, 3, 3, 7, 4, 4, 1, 9, 5])
    [7, 2, 9, 2, 9]
    """

    max5=sum(seq[:5])
    last=4
    for i in list(range(len(seq))[5:]):
        tempsum=sum(seq[i-4:i+1])
        if tempsum>max5:
            max5=tempsum
            last=i
    return seq[last-4:last+1]
    

if __name__ == '__main__':
    import doctest
doctest.testmod()
