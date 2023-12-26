import random
def generate_random_ipv4():
    """产生一个随机的IPv4地址."""
    return '.'.join(map(str, (random.randint(0, 255) for _ in range(4))))

# 打印一个随机的IPv4地址
print(generate_random_ipv4())

