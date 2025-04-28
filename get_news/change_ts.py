# 定义要处理的文件路径
file_path = r'./docs\.vitepress\theme\components\NewsCard.vue'
# 定义要追加的新内容
new_content =""

try:
    # 以只读模式打开文件
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    start_index = None
    end_index = None
    # 查找起始和结束标识符的索引
    for i, line in enumerate(lines):
        if line.strip() == '//(@#':
            if start_index is None:
                start_index = i
            else:
                end_index = i
                break

    if start_index is not None and end_index is not None:
        # 删除标识符之间的内容
        del lines[start_index + 1:end_index]
        # 在标识符之间插入新内容
        lines.insert(start_index + 1, new_content)

    # 以写入模式打开文件，将修改后的内容写回文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

    print("文件修改完成。")
except FileNotFoundError:
    print(f"未找到文件: {file_path}")
except Exception as e:
    print(f"发生错误: {e}")