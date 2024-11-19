#khoi tao
docker_compose = {
    "version": "3.8",
    "services": {
        "app": {
            "image": "python:3.10-slim",
            "command": "python app.py",
            "volumes": ["./app:/app"],
            "restart": "always",
            "ports": ["5000:5000"],
            "depends_on": ["db"]
        }
    }
}
print(docker_compose)

#sua phien ban
docker_compose["version"] = "3.10"
print(docker_compose)

#in image
print(docker_compose["services"]["app"]["image"])

# Thêm key 'environment' với giá trị ['PYTHONUNBUFFERED=1'], in kết quả.
docker_compose["services"]["app"]["environment"] = {"PYTHONUNBUFFERED": "1"}
print(docker_compose)

# ● Kiểm tra xem dictionary có chứa key 'volumes' hay không?
if "volumes" in docker_compose["services"]["app"]:
    print("dict co chua key 'volumes'")
else:
    print("dict khong chua key 'volumes'")

# Xóa key 'depends_on' khỏi dictionary, in kết quả.
docker_compose["services"]["app"].pop("depends_on")
print(docker_compose)

# ● Đếm số lượng key trong dictionary.
print(f"So luong key dict: {len(docker_compose)}")

# Tạo một list chứa tất cả các giá trị trong dictionary và in kết quả.
temp = list(docker_compose.values())
print(f"Tat ca gia tri cua dict: {temp}")

# Kiểm tra xem 'always' có phải là giá trị của bất kỳ key nào không?
found_always = False
for value in docker_compose["services"]["app"].values():
    if value == "always":
        found_always = True
        break

if found_always:
    print("'always' la gia tri")
else:
    print("'always' khong la gia tri")

new_key = input("Nhap key moi: ")
new_value = input("Nhap value moi: ")

# Nhập vào từ bàn phím một key mới và giá trị tương ứng, sau đó thêm vào dictionary và in lại kết quả.
docker_compose[new_key] = new_value
print(docker_compose)
