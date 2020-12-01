from PIL import Image


img = Image.open("test__.png")
color = img.convert("L")
color.save('bw_test__.png')
color.show()
