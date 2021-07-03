import cv2

x = cv2.imread("img.jpeg")
i = x.shape[0]
j = x.shape[1]
print(i,j)

# encrypt image
key = int(input("Enter secret key: "))
msg = input("Enter message that you want to send: ")