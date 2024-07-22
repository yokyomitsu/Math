import math
from collections import Counter

def calculate_entropy_binary(bit_string):
    # カウントする
    count = Counter(bit_string)
    total = len(bit_string)
    
    # 発生確率を計算する
    p1 = count['1'] / total
    p0 = count['0'] / total
    
    # エントロピーを計算する
    if p1 == 0 or p0 == 0:  # ログの計算で0が発生しないようにチェック
        entropy = 0.0
    else:
        entropy = - (p1 * math.log2(p1) + p0 * math.log2(p0))
    
    return entropy

if __name__ == "__main__":
    # 例としてAとBを計算する
    A = "000010000"
    B = "0101101001"

    entropy_A = calculate_entropy_binary(A)
    entropy_B = calculate_entropy_binary(B)

    print(f"Entropy of A: {entropy_A}")
    print(f"Entropy of B: {entropy_B}")