images = int(input("how many images do you have?:"))
Res = input("What is the resloution of your images? e.g 1920 x 1080:").split()
Length = int(Res[0])
Height = int(Res[2])

Pixels = Length*Height
Bytes = images*(Pixels/8)

KiloBytes = Bytes/1024
counter = 0
while Bytes>1024:
    Bytes = Bytes/1024
    counter = counter+1

units = ["B", "KB", "MB","GB","TB"]
print(round(Bytes,2) , units[counter])
