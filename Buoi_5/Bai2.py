registered_name = { 'hieu', 'tu', 'duyen', 'ha', 'mai', 'nguyen','anh', 'truong', 'khuong', 'linh',}
checkin_name = {"tan", "tu", 'thanh', 'truong', 'mai', 'van', 'quyet', 'hieu', 'cao', 'linh'}

notface = registered_name - checkin_name
print("Chua check in: ")
print(notface)

print("So luong dang ki:",len(registered_name))
print("So luong check in:",len(checkin_name))

sorted= sorted(registered_name)
print("Sap xep ten theo A-Z: ")
print(sorted)