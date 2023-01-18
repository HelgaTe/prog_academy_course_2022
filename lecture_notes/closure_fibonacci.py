def factorial():
    results = [1, 1]
    def get(n):
        if n <= len(results):
            return results[n]
        res = results[-1]
        for i in range(len(results), n + 1):
            res *= i
            results.append(res)
        return res
    return get

f = factorial()
print(f(5))
print(f(6))
print(f(7))
print(f(4))
print(f(3))