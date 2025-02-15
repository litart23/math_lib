def add(a, b):
    """
    Складывает два числа.

    :param a: Первое число.
    :param b: Второе число.
    :return: Сумма a и b.
    test
    import numpy as np 
    qa = np.array([[1,2,3],[4,5,6]])
    b = np.transpose(qa) #or qa.T
    np.dot(b,qa) # multiplication
    b.shape #dimetions
    print(qa)
    take_col = qa[:,:2] # taking first two column
    reshape = qa.reshape(-1,1) # creating a new columns
    reshape
    """
    return a + b

def subtract(a, b):
    """
    Вычитает второе число из первого.

    :param a: Первое число.
    :param b: Второе число.
    :return: Разность a и b.
    """
    return a - b

def multiply(a, b):
    """
    Умножает два числа.

    :param a: Первое число.
    :param b: Второе число.
    :return: Произведение a и b.
    """
    return a * b

def divide(a, b):
    """
    Делит первое число на второе.

    :param a: Первое число.
    :param b: Второе число.
    :return: Результат деления a на b.
    :raises ZeroDivisionError: Если b равно 0.
    """
    if b == 0:
        raise ZeroDivisionError("Нельзя делить на ноль!")
    return a / b


def numpym(a, b):
    """
    import numpy as np 
    qa = np.array([[1,2,3],[4,5,6]])
    b = np.transpose(qa) #or qa.T
    np.dot(b,qa) # multiplication
    b.shape #dimetions
    print(qa)
    take_col = qa[:,:2] # taking first two column
    reshape = qa.reshape(-1,1) # creating a new columns
    reshape
    """
    return a + b



