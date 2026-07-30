import random


def windows():
    chrome_major_old = random.choice(range(100, 115))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.1; en-US) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_major_old}.0.{random.choice(range(5000, 6500))}.0 Safari/537.36"
    bz = "537.36"
    chrome_major_mid = random.choice(range(115, 125))
    B = f"Mozilla/5.0 (Windows NT {random.choice([10, 11])}.0; Win64; x64) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{chrome_major_mid}.0.{random.choice(range(6000, 6800))}.{random.choice(range(1, 150))} Safari/{bz}"
    chrome_major_wow = random.choice(range(120, 130))
    C = f"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_major_wow}.0.{random.choice(range(6000, 6900))}.{random.choice(range(1, 150))} Safari/537.36"
    chrome_latest = random.choice(range(130, 143))
    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_latest}.0.{random.choice(range(6500, 7200))}.0 Safari/537.36"
    return random.choice([A, B, C, D])


def window1():
    chrome_major = random.choice(range(120, 140))
    build_1 = random.choice(range(6000, 7100))
    A = f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_major}.0.{build_1}.0 Safari/537.36"
    chrome_major_alt = random.choice(range(125, 142))
    build_2 = random.choice(range(6200, 7150))
    patch_2 = random.choice(range(50, 250))
    B = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_major_alt}.0.{build_2}.{patch_2} Safari/537.36"
    chrome_major_ent = random.choice(range(118, 135))
    build_3 = random.choice(range(5800, 6800))
    C = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:{random.choice(range(110, 130))}.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_major_ent}.0.{build_3}.{random.choice(range(10, 190))} Safari/537.36"
    latest_build = random.randint(7000, 7500)
    latest_patch = random.randint(100, 300)
    chrome_ultra = random.choice(range(140, 146))
    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ultra}.0.{latest_build}.{latest_patch} Safari/537.36"
    return random.choice([A, B, C, D])
