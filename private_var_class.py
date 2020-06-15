
class MyDataIncrement:
    __mycount = 0

    def count(self):
        self.__mycount += 1
        print("Count Value is:", self.__mycount)


counter = MyDataIncrement()
counter.count()
counter.count()

print("Secret Count:", counter._MyDataIncrement__mycount)
