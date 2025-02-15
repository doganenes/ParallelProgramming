
custom_power = lambda x=0,/, e=1: x**e


def custom_equation(x:int = 0,y:int=0,/,a:int = 1,b:int=1,*,c:int=1) -> float:
    """
    :param x: The positional-only integer base parameter for the equation , default is 0
    :param y: The positional-only integer base parameter for the equation , default is 0
    :param a: The positional-or-keyword integer exponent parameter for the equation , default is 1
    :param b: The positional-or-keyword integer exponent parameter for the equation , default is 1
    :param c: The keyword-only integer divisor parameter for the equation , default is 1
    :return: The result of the calculation as a float and the equation is (x**a + y**b)/c
    :rtype: float
    """
    return (x**a + y**b)/c

def fn_w_counter() -> (int, dict[str, int]):
    if not hasattr(fn_w_counter,'_call_counter'):
        fn_w_counter._call_counter = 0
        fn_w_counter._caller_dict = {}
    caller = __name__
    fn_w_counter._call_counter += 1
    if caller in fn_w_counter._caller_dict:
        fn_w_counter._caller_dict[caller] += 1
    else:
        fn_w_counter._caller_dict[caller] = 1
    return fn_w_counter._call_counter,fn_w_counter._caller_dict
