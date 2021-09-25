class Library:
    def __init__(self,list,name):
        self.list=list#
        self.name=name
        self.dic={}
    def displaybooks(self):
        for i in self.list:
            print(i)
    def lendbook(self,user,book):
        if book not in self.dic.keys():
            self.dic.update({book:user})
        else:
            print("Book is already present in list.")
    def addbook(self,book):
        self.list.append(book)
    def returnbook(self,book):
        
        self.dic.pop(book)
if __name__=='__main__':
    j=Library(["rich","honey","jungle book"],"jashan")
    while True:
       print("choose a function to peform:")
       i=int(input(""))
       if i==1:
           j.displaybooks()
       elif i==2:
           user=input("our id :")
           book=input("which book you want to lend:")
           j.lendbook(user,book)
       elif i==3:
           book=input("name of the book you want to add:")
           j.addbook(book)
       elif i==4:
           book=input("book you want to return:")
       else:
           print("Error")
       print("q to quit or c to continue")
       i2=""
       while i2!="q" and i2!="c":
           i2=input()
           if i2=="q":
               exit()
           elif i2=="c":
               continue
        