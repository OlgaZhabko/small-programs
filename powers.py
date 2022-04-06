class Powers:
    '''this class generates powers of a whole number taking two arguments(a number and number of powers).
    The program tests it on numbers 3 (to the power of 10) and 5 (to the power of 7)'''
    def __init__(self, number, stop=5):
        self.start=0
        self.number=number
        self.stop=stop
    def __iter__(self):
        return self
    def __next__(self):
        self.start+=1
        if self.start==self.stop+1:
            raise StopIteration
        elif self.start==1:      
            return self.start, self.number
        else:
            self.number*=self.number
            return self.start, self.number
if __name__=='__main__':
    pow_of_3=Powers(3,10)
    for el in pow_of_3:
        print(*el)
    pow_of_5=Powers(5,7)
    for ind, el in list(pow_of_5):
        print(f'5 to the power of{ind:3} is {el}')