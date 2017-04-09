import qrcode

img = qrcode.make("http://kujirahand.com/")

img.save("crcode-test.png")
