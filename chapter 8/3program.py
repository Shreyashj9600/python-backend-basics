# static methods
# methods that don,t use the self parameter(work at class level)


class MathUtils:
    # @staticmethod # decorator
    def add(a, b):
        return a + b

# Calling the static method
result = MathUtils.add(5, 3)
print(result)
