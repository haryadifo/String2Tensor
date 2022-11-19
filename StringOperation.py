class StringOperation:

    pesan = input("Masukkan Pesan Rahasia : ")
    remove_space_pesan = pesan.replace(" ", "")
    test = remove_space_pesan

    obj1 = ""
    obj2 = ""
    obj3 = ""

    matx1 = [0 for x in range(2)]
    matx2 = [0 for x in range(2)]
    matx3 = [0 for x in range(2)]
    tensor = [[]]

    def partition3D(self):
        pad = 3 - (len(self.test) % 3)
        for i in range(1, pad+1):
            self.test += "~"
        part = int(len(self.test)/3)
        for i in range(0, len(self.test)):
            if(i < part):
                self.obj1 += self.test[i:i+1]
            elif((i >= part) and (i < (part * 2))):
                self.obj2 += self.test[i:i+1]
            else:
                self.obj3 += self.test[i:i+1]
        print("obj 1 =", self.obj1)
        print("obj 2 =", self.obj2)
        print("obj 3 =", self.obj3)

    def partition2D(self, iter):
        test2 = self.obj1 if(iter == 1) else self.obj2 if(iter == 2) else self.obj3
        pad = 2 - (len(test2) % 2)
        for i in range(1, pad+1):
            test2 += "`"
        part = int(len(test2) / 2)
        if iter == 1:
            self.matx1[0] = test2[0:part]
            self.matx1[1] = test2[part:]
        elif iter == 2:
            self.matx2[0] = test2[0:part]
            self.matx2[1] = test2[part:]
        elif iter == 3:
            self.matx3[0] = test2[0:part]
            self.matx3[1] = test2[part:]

    def toTensor(self):
        row = 2
        column = 3
        self.tensor = [[0 for x in range(row)] for y in range(column)]
        for i in range(column):
            for j in range(row):
                if i == 0:
                    self.tensor[i][j] = self.matx1[j]
                elif i == 1:
                    self.tensor[i][j] = self.matx2[j]
                else:
                    self.tensor[i][j] = self.matx3[j]
        return self.tensor

    def TensorToBinary(self):
        word = self.tensor
        for i in range(3):
            for j in range(2):
                byte_arr = bytearray(word[i][j], "utf-8")
                word[i][j] = ""
                for byte in byte_arr:
                    word[i][j] += bin(byte)[2:]

#call the object
# test = StringOperation()
# test.partition3D()
# test.partition2D(2)
# test.partition2D(1)
# test.partition2D(3)
# print("Tensor = ", test.toTensor())
# test.TensorToBinary()
# print("Tensor to Binary = ", test.tensor)
# print(len(test.tensor),len(test.tensor[0]))
a = "aku"
print(a[2:3])
