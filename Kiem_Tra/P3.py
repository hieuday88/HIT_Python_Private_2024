# Input: coded_str = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"

coded_str = input("Nhap chuoi ma hoa: ")

stack = []
current_num = 0
current_str = ''

for char in coded_str:
    if char.isdigit():
        current_num = int(char)
    elif char == '[':
        stack.append((current_str, current_num))
        current_str = ''
        current_num = 0
    elif char == ']':
        prev_str, num = stack.pop()
        current_str = prev_str + current_str * num
    else:
        current_str += char

print(current_str)
