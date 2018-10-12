from helpers import math_helpers

print(math_helpers.smart_divide(4, 2))
print(math_helpers.smart_divide(1, False))
print(math_helpers.smart_divide(1431.84, 456))
print(math_helpers.smart_divide(12, 0))
print(math_helpers.smart_divide(100, None))
print(math_helpers.smart_divide(0, 1))
print(math_helpers.smart_divide(False, 99))
print(math_helpers.smart_divide(None, 11))
print(math_helpers.smart_divide(8426859910050, 75))

# 1 / false
# 1431.84 / 456
# 12 / 0
# 100 / null
# 8 / undefined
# 8426859910050 / 75