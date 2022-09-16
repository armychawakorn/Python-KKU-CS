def AddVat(obj):
    for i in obj:
        Vat = i[2] * (i[3] / 100)
        VatandPrice = Vat + i[2]
        i.append('%.2f' % Vat)
        i.append(VatandPrice)
    return obj

def GetMaxVat(obj):
    Def = []
    for i in obj:
        Def.append(i[3])
    for i in obj:
        if i[3] == sorted(Def)[-1]:
            print("สินค้าที่จ่ายภาษีมากที่สุดคือ", i[1], "ภาษีที่ต้องจ่ายคือ", i[3], "%." "รวมเป็นเงิน", (i[2] * (i[3] / 100)) + i[2], "บาท") ##<< แก้ตรงนี้ด้วยให้เป็นแบบของตัวเอง >>##

def GetMinVat(obj):
    Def = []
    for i in obj:
        Def.append(i[3])
    for i in obj:
        if i[3] == sorted(Def)[0]:
            print(
                f"สินค้าที่จ่ายภาษีน้อยที่สุดคือ {i[1]} ภาษีที่ต้องจ่ายคือ {i[3]} %. รวมเป็นเงิน { (i[2] * (i[3] / 100)) + i[2]} บาท") ##<< แก้ตรงนี้ด้วยให้เป็นแบบของตัวเอง >>##

def GetAvarageVat(obj):
    Def = 0
    for i in obj:
        Def += i[3]
    print('ค่าเฉลี่ยเงินภาษี ของสินค้าทุกชิ้นคือ %0.2f' % (Def / len(obj))) ##<< แก้ตรงนี้ด้วยให้เป็นแบบของตัวเอง >>##

def GetMaxPrice(obj):
    Def = []
    for i in obj:
        Def.append(i[2])
    for i in obj:
        if i[2] == sorted(Def)[-1]:
            print(f"สินค้าที่มีราคาสูงสุดคือ {i[1]} ราคา {i[2]} บาท") ##<< แก้ตรงนี้ด้วยให้เป็นแบบของตัวเอง >>##

def GetMinPrice(obj):
    Def = []
    for i in obj:
        Def.append(i[2])
    for i in obj:
        if i[2] == sorted(Def)[0]:
            print(f"สินค้าที่มีราคาต่ำสุดคือ {i[1]} ราคา {i[2]} บาท") ##<< แก้ตรงนี้ด้วยให้เป็นแบบของตัวเอง >>##
            break

def ShowProduct(obj):
    print("รหัสสินค้า\t\tชื่อสินค้า\t\tราคา\t\tภาษี\t\tราคาสุทธิ") ##<< แก้ตรงนี้ด้วยให้เป็นแบบของตัวเอง >>##
    for i in obj:
        print(f"{i[0]}\t\t{i[1]}\t\t{i[2]}\t\t{i[4]}\t\t{i[5]}") ##<< แก้ตรงนี้ด้วยให้เป็นแบบของตัวเอง >>##

InputProduct = [
    ['801', 'Coconut', 5.00, 3],
    ['810', 'Kiwi', 3.00, 2],
    ['807', 'Watermelon', 7.00, 5],
    ['808', 'Apple', 4.00, 4],
    ['809', 'Apricot', 3.00, 5],
    ['811', 'Jackfruit', 9.00, 5],
    ['815', 'Orange', 8.00, 6],
    ['814', 'Guava', 4.00, 7],
    ['813', 'Lemon', 7.00, 5]
]

ShowProduct(AddVat(InputProduct))
GetMaxVat(AddVat(InputProduct))
GetMinVat(AddVat(InputProduct))
GetAvarageVat(AddVat(InputProduct))
GetMaxPrice(AddVat(InputProduct))
GetMinPrice(AddVat(InputProduct))