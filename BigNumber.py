class BigNumber:
    
    def __init__(self,string_big=None):
        """ constructor for class BigNumber """
        self.string_big=str(string_big)
        #initialize list
        self.list_big=[]
        self.list_big=[str(x) for x in string_big]
        for i in self.list_big:
            if i==" ":
                self.list_big.remove(" ") ##remove spaces from input
            if i==",":
                self.list_big.remove(",") ##remove commas from input
            if i=="-":
                self.list_big.remove("-") ##all numbers positive
        while self.list_big[0]=="0":
            self.list_big.remove("0") ##remove preceding 0's from input

                    

    def __str__(self):
        """ tostring method for class BigNumber """
        string_list=[str(i) for i in self.list_big]
        for x in range(len(string_list))[::-3][1:]: ##add a comma every third digit from the right
                string_list.insert(x+1,",")
        y=""                                        ##initiating empty string
        return (y.join(string_list))                ##adding list to empty string to return desired format


    def compare(self,big2):
        if len(self.list_big)>len(big2.string_big):   ##Comparing lengths of list
            return ">"
        elif len(self.list_big)<len(big2.string_big):
            return "<"
        elif len(self.list_big)==len(big2.string_big):
            self.list_big=[int(x) for x in self.list_big]  ##Converting lists of strings to lists of integers
            list_big2=[int(x) for x in big2.string_big]
            a=0
            b=0
            for x in range(len(self.list_big)):           ##Scanning lists and comparing integers
                if self.list_big[x]>list_big2[x]:
                    return ">"
                elif self.list_big[x]<list_big2[x]:
                    return "<"
                elif self.list_big[x]==list_big2[x]:
                    x=x+1
                    continue
            return "=" 

    
    
    def add(self,big2):
        self.list_big=[int(x) for x in self.list_big]               ##converting to integers
        list_big2=[int(x) for x in big2.string_big]
        while True:
            if len(self.list_big)>len(list_big2):               ###matching length of list
                list_big2.insert(0,0)
                continue
            elif len(list_big2)>len(self.list_big):
                self.list_big.insert(0,0)
                continue
            elif len(list_big2)==len(self.list_big):
                self.list_big.reverse()
                list_big2.reverse()
                list_big3=[self.list_big[x]+list_big2[x] for x in range(len(self.list_big))]        ###adding integers
                list_big3.reverse()
                while any(x>9 for x in list_big3):              ###accounting for the carry
                    for x in range(len(list_big3)):
                        if list_big3[x]>9 and 0<x<len(list_big3):
                            list_big3[x]=int(10-list_big3[x])*-1
                            list_big3[x-1]=list_big3[x-1]+1
                            continue
                        elif list_big3[0]>9:
                            list_big3[0]=int(10-list_big3[0])*-1
                            list_big3.insert(0,1)
                        elif all(x<=9 for x in list_big3):
                            return BigNumber(list_big3)
            return BigNumber(list_big3)

    
    def subtract(self,big2):
        if BigNumber(self.list_big).compare(big2)==">":             ##subtraction if big1>big2
            self.list_big=[int(x) for x in self.list_big]
            list_big2=[int(x) for x in big2.string_big]
            while True:
                if len(self.list_big)>len(list_big2):
                    list_big2.insert(0,0)
                    continue
                elif len(self.list_big)==len(list_big2):
                    break
            self.list_big.reverse()
            list_big2.reverse()
            list_big3=[self.list_big[x]-list_big2[x] for x in range(len(self.list_big))]
            for x in range(len(list_big3)):
                if list_big3[x]<0:
                    list_big3[x]=list_big3[x]+10
                    list_big3[x+1]=list_big3[x+1]-1
                    continue
                else:
                    break
            list_big3.reverse()
            return BigNumber(list_big3)
        elif BigNumber(self.list_big).compare(big2)=="<":               ##subtration if big1<big2
            self.list_big=[int(x) for x in self.list_big]
            list_big2=[int(x) for x in big2.string_big]
            while True:
                if len(self.list_big)<len(list_big2):
                    self.list_big.insert(0,0)
                    continue
                elif len(self.list_big)==len(list_big2):
                    break
            self.list_big.reverse()
            list_big2.reverse()
            list_big3=[list_big2[x]-self.list_big[x] for x in range(len(self.list_big))]
            for x in range(len(list_big3)):
                if list_big3[x]<0:
                    list_big3[x]=list_big3[x]+10
                    list_big3[x+1]=list_big3[x+1]-1
                    continue
                else:
                    break
            list_big3.reverse()
            list_big3[0]=int(list_big3[0]*-1)
            return BigNumber(list_big3)

     
    def scale(self,factor):
        y=str(self)
        if 0<int(factor)<=9:
            c=int(factor)
            y=y.replace(",","")                 ###Change BigNumber to int then scale###
            y=int(y)
            b=y*c
            b=str(b)                            ###Convert back to BigNumber###
            return BigNumber(b)
        elif int(factor)==0:
            return "0"
        else:
            return "Scale factor must be inbetween 0 and 9."

    
    def multiply(self,big2):
        x=str(self)
        y=str(big2)
        x=x.replace(",","")                 ###Change both BigNumbers to int then multiply###
        y=y.replace(",","")
        x=int(x)
        y=int(y)
        w=x*y
        w=str(w)                            ###Convert answer to string then BigNumber##
        return BigNumber(w)
