# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/9 20:46
@Auth ： sy 
@Function ：请输入模块功能描述
"""
# 针对布尔值的运算
# not and or
b1 = True
b2 = False
print(b1 and b2)
print(b1 or b2)
print(not b2)

# 优先级not>and>or
b1 = True
b2 = False
# not>and
print(b1 and not b2)
# and>or
print(b1 or b1 and b2)
print((b1 or b1) and b2)

# and的短路原则
print(False and b3)
# or的短路
print(True or b3)

# 混合运算
x = 1
y = 2
z = 3

# 短路原则：如果前面的条件构成的短路，已经决定了整个结果，后面的就会短路
b = x > y and x + 2 > 3 or y + 1 > z
print(b)

print(False or False or False)
print(True or False or e)
