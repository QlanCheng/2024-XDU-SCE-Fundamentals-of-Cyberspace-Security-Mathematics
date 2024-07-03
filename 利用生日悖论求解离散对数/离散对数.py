def discrete_logarithm(result, base, mod, max_iterations=10):
    if not all(isinstance(arg, int) for arg in [result, base, mod]):
        raise TypeError("All parameters must be integers.  参数必须是整数")

    success_probability = 1 - 0.5**max_iterations

    def create_tableA(base, mod):
        import random
        tableA = dict()
        for counter in range(0, int(mod ** 0.5)):
            a = random.randint(0, mod - 1)
            ga = pow(base, a, mod)
            tableA[ga] = a  # 键是ga,值是a,方便查询
        return tableA  # 用字典是因为字典是底层是用哈希表实现的，查找速度非常快。

    def create_tableB(result, base, mod):
        import random
        tableB = dict()
        for counter in range(0, int(mod ** 0.5)):
            b = random.randint(0, mod - 1)
            ygb = (result * pow(base, b, mod)) % mod
            tableB[ygb] = b
        return tableB

    while max_iterations:
        max_iterations -= 1

        tableA = create_tableA(base, mod)
        tableB = create_tableB(result, base, mod)
        keysA = set(tableA.keys())
        keysB = set(tableB.keys())
        common_results = keysA & keysB
        if common_results:
            common_item = common_results.pop()
            a, b = tableA[common_item], tableB[common_item]
            return (a - b) % (mod - 1)
        else:
            continue

    raise TimeoutError(f"""
    Exceeded maximum iterations ({max_iterations}) without finding a solution.
超过最大循环次数({max_iterations})次.若确定参数无误.尝试改变max_iterations的值? 或再试一次? 当前成功概率为{success_probability}
""")



if __name__ == '__main__':
    y = 66132073
    g = 3
    p = 104857601

    print(discrete_logarithm(y, g, p))


