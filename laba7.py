import PIL.Image
from PIL import Image, ImageFilter


print("Задача 1")
name_file = "perva2.jpg"
with Image.open(name_file) as img:
    img.load()
img.show()
width, height = img.size
format = img.format
mode = img.mode
print('Ширина: ', width)
print('Высота: ', height)
print('Формат: ', format)
print('Цветовая модель1: ', mode)

def zadacha2():
    print("Задача 2")
    file2 = "perva2.jpg"
    with Image.open(file2) as img:
        img.load()
    img.show()
    new_kartinka = img.resize((img.height // 3, img.width // 3))
    new_kartinka.show()
    new_kartinka = img.rotate(180)
    new_kartinka.show()
    new_kartinka = img.transpose(PIL.Image.FLIP_LEFT_RIGHT)
    new_kartinka.show()
    new_kartinka.save("perva2_new_new.jpg")
    new_kartinka.save("perva2_new_new_new.jpg")
    new_kartinka.save("pervanew.jpg")

def zadacha3():
    print("Задача 3")
    kartinki = ['perva2.jpg', 'perva3.jpg', 'perva4.jpg', 'perva5.jpeg', 'perva6.jpg']
    for i in kartinki:
        with Image.open(i) as pic:
            pic.load()
        new_pic = pic.filter(ImageFilter.FIND_EDGES)
        new_pic.show()
        new_pic.save('new_' + i)

def zadacha4():
    print("Задача 4")
    file4 = Image.open("perva3.jpg")
    znak = Image.open("vvodniy_znak.png")
    width = 380
    height = 300
    umenshenie = znak.resize((width,height), Image.LANCZOS)
    file4.paste(umenshenie, (30,10), umenshenie)
    file4.show()
    file4.save("karninka_s_vvodznak.png")


zadacha2()