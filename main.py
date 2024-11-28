from PIL import Image, ImageDraw, ImageFont #импорт библиотеки Pillow
print("Генератор мемов запущен!") #Вывод начального текста

top_text = input("Введите верхний текст: ") #Запрос верхнего текста
bottom_text = input("Введите нижний текст: ") #Запрос нижнего текста



print("Список картинок:") #Вывод меню картинок
print("1. Кот в ресторане") #№1
print("2. Кот в очках") #№2

image_number = int(input("Введите номер картинки: ")) #Запрос картинки

if image_number == 1: #если номер фото 1:
    image_file = "Кот в ресторане.png" # начинает редактировать Фото "Кот в ресторане.png"
elif image_number == 2: #если номер фото 2:
    image_file = "Кот в очках.png" # начинает редактировать Фото "Кот в очках.png"

image = Image.open(image_file) #Открытие файла
width, height = image.size

draw = ImageDraw.Draw(image) #отрисовка картинки

font = ImageFont.truetype('arial.ttf', size=70) #Шрифт

text = draw.textbbox((0, 0), top_text, font) #Создание верхнего текста
draw.text(((width - text[2]) / 2, 10), top_text, font=font, fill="black") #Отрисовка верхнего текста

text = draw.textbbox((0, 0), bottom_text, font) #Создание нижнего текста
draw.text(((width - text[2]) / 2, height - text[3] - 10), bottom_text, font=font, fill="black") #Отрисовка нижнего текста

image.save("new_meme.jpg") #сохранение