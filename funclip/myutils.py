import re
def count_spk_occurrences(filename):
    spk_counts = {}  # 创建一个字典来存储每个spk的出现次数
    pattern = r'(\d+)\s+spk\d+'
    spk_pattern = r'spk\d+'

    with open(filename, 'r') as file:
        lines = file.readlines()

        for i in range(0, len(lines)):
            # 判断lines[i]是否满足pattern
            if re.match(pattern, lines[i]):
                # spk = lines[i].strip()  # 获取spk编号
                spk = re.search(spk_pattern, lines[i]).group(0)  # 获取spk编号
                spk_counts[spk] = spk_counts.get(spk, 0) + 1  # 更新spk的出现次数

    # 按照出现次数从多到少排序
    sorted_spk_counts = sorted(spk_counts.items(), key=lambda x: x[1], reverse=True)

    return sorted_spk_counts

if __name__ == '__main__':
    # 使用示例
    filename = '/Users/huan/Documents/xuyinghuan/vscodestextsetc/codes/FunClipAli/output/total.srt'
    result = count_spk_occurrences(filename)

    for spk, count in result:
        print(f"spk{spk}: {count} 次")
