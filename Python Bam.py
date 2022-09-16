def tax(information):
    for j in information:
        tax= j[2] * (j[3] / 100)
        price = tax +j[2]
        j.append('%.2f' % tax)
        j.append(price)
    return information

def maxtax(information):
    zata = information
    data = []
    for j in zata:
        data.append(j[3])
    for j in zata:
        if j [3] == sorted(data)[-1]:
            print("สินค้าที่มีการจ่ายภาษีมากที่สุดคือ" ,j[1], "ภาษีที่ต้องจ่ายเท่ากับ" ,j[3] ,"%. รวมเป็นเงิน" , (j[2] * (j[3] / 100)) + j[2], "บาท")

def mintax(information):
    zata = information
    data = []
    for j in zata:
        data.append(j[3])
    for j in zata:
        if j[3] == sorted(data)[0]:
            print("สินค้าที่มีการจ่ายภาษีน้อยที่สุดคือ" ,j[1], "ภาษีที่ต้องจ่ายเท่ากับ" ,j[3], "%. รวมเป็นเงิน",  (j[2] * (j[3] / 100)) + j[2], "บาท")

def getavgvat(information):
    zata = information
    sumVat = 0
    for j in zata:
        sumVat += j[3]
    print('ค่าเฉลี่ยเงินภาษีของสินค้าทุกชิ้นเท่ากับ %0.2f' %
        (sumVat / len(zata)))

def maxprice(information):
    zata = information
    maxPrice = []
    for j in zata:
        maxPrice.append(j[2])
    for j in zata:
      if j[2] == sorted(maxPrice)[-1]:
          print("สินค้าราคาสูงสุดคือ", j[1], "ราคา" ,j[2], "บาท")

def minprice(information):
    zata = information
    minprice = []
    for j in zata:
        minprice.append(j[2])
    for j in zata:
        if j[2] == sorted(minprice)[0]:
            print("สินค้าราคาต่ำสุดคือ" ,j[1], "ราคา" ,j[2], "บาท")
            break

def display(information):
    zata = information
    print("รหัสสินค้า\t\tชื่อสินค้า\t\tราคา\t\tภาษี\t\tราคาทั้งหมด")
    for j in zata:
        print(j[0],'\t\t',j[1],'\t\t',j[2],'\t\t',j[4],'\t\t',j[5])

form = [
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

chodata = tax(form)

display(chodata)
maxprice(chodata)
minprice(chodata)
maxtax(chodata)
mintax(chodata)
getavgvat(chodata)