#retail
#inventory
#oop
#class declaration
import time
import math
class SupplyChain:
    def __init__(self, name, stuff):
        self.name = name
        self.stuff = stuff
        
    def printname(self):
        print(self.name, self.stuff)

simcardpuzzle1='    ------------'
simcardpuzzle2='    |       [  ]|'
simcardpuzzle3='    ------------'     
sincard=simcardpuzzle1+simcardpuzzle2+simcardpuzzle3
#object        
supplychain1 = SupplyChain('supplychain1', 'postcard')
        
#function call
supplychain1.printname()

class PostCardLogistics(SupplyChain):
    pass
    
postcardsupplychain1 = PostCardLogistics('postcardsupplychain1', 'paper')

postcardsupplychain1.printname()


class Printer:
    def __init__(self, paper, art):
        self.paper = paper
        self.art = art
        
#    def printname(self):
        #print(self.paper, self.art)
        
class Art:
    def __init__(self, paper):
        self.paper = paper
      #  self.color = color
        
#    def drawArt:
#        return '''      ^   ^
  #                      ( +  +)
    #                    {    w}
      #                      [ ]   [ ]'''           
          
#dogArt = Art('A6')
#A6Printet = Printer('A6', 'pixel art')
#A6Printet = Printer('A6', dogArt.drawArt())

#A6Printer.printname()
  
        
#April 5 code      

#inventory

class BambooDesignedProductInventory(SupplyChain):
    pass
    
BambooDesignedProductInventory1 = BambooDesignedProductInventory1('BambooDesignedProductInventory', 'bamboo product 1 inventory')

BambooDesignedProductInventory1.printname()

#inheritance
#April 6 coding
#bamboo products
class BambooDesignedProduct(BambooDesignedProductInventory):
    pass
    
BambooDesignedProduct1 = BambooDesignedProduct('Bamboo Designed Product1', 'bamboo product 1 pending')

BambooDesignedProduct1.printname()


potentialbambooitems = ['bamboo postcard', 'bamboo beauty collection', 'bamboo furniture']

print(potentialbambooitems)


#pos computer
import numpy as np

mem = memoryview(bytes(8))

memarr = bytearray(8)

memarr[0] = 1
memarr[1] = 0
memarr[2] = 0
memarr[3] = 0
memarr[4] = 0
memarr[5] = 0
memarr[6] = 0
memarr[7] = 0

#print(memarr[7])

circuit = [0,1,2,3,4,5,6,7,8,9]

A = bool(str(memarr)[13])
#print(A)
B = bool(str(memarr)[16])

orGate = A or B

xorGate = A^B

andGate = A and B

circuit[0] = orGate

circuit.index(1, andGate)    
#__name__ equals '__main__' to make sure the program is directly run by Python interpreter not as a module

powersupply = input('Please enter 1 to print a bulb')
    if circuit[1]:
        bulb = '''   
            \  |  /
              (°)
              |=|
              [                               ]
              '''
bulb = bulb+str(memarr)[12:44]
if powersupply:
    print(bulb)
        
          
#retail pos
class POScomputer:
    def __init__(self, name, stuff):
        self.name = name
        self.stuff = stuff
        
    def printname(self):
        print(self.name, self.stuff)
        
    def printticket(self):
        print(self.name, self.stuff,  'Thank you')
    def poscomputer(self):
        circuit[1] = 1
        bulb = '''   
            \  |  /
              (°)
              |=|
              [                               ]
              '''
        print(bulb)
        
POScomputer1 = POScomputer('POScomputer', 'bamboo postcard')
        
POScomputer1.printticket()
#shopping cart

POScomputer1.poscomputer()

class ShoppingCart:
    def __init__(self, name, stuff):
        self.name = name
        self.stuff = stuff
        
    def printname(self):
        print(self.name, self.stuff)
        
    def printticket(self):
        print(self.name, self.stuff,  'Thank you')
        
ShoppingCart1 = ShoppingCart('ShoppingCart1', 'Empty cart')
        
ShoppingCart1.printname()

#RegEx in dynamic system
dynamicsystem = POScomputer1.printticket()+'dynamtic system'
print(re.search('^postcard', dynamicsystem))

from time import sleep, strftime, gmtime
#import cmd
#watch

def numtodigit(s):
    if s=='1':
        print('''   ---
           |    |
           |    |
           |    |
            ---''')
    if s=='2':
        print('''   -------------
                     |    |
                |    |
            |    |
            --------------''')
    if s=='3':
       print('''   -------------
                     |    |
                |    |
                     |    |
            --------------''')
    if s=='4':
        print('''    / |-----
           /    |    |
            |__|    |
                |    |
                 ---''')
    if s=='5':
        print('''           -------------
                     |    |
                |    |
                     |    |
            --------''')
    if s=='6':
        print('''   ---
           |    |____
           |    --      |
           |   | _|    |
            ----------''')
    if s=='7':
        print('''-----------
                |    |
              |    |
           |    |
            ---''')
    if s=='8':
        print('''   --------
           |    --    |
           |   |--|   |
           |    --    |
            ----------''')
    if s=='9':
        print('''   -----
           |  o  |
             |    |
           |    |
            ---''')
    if s==':':
        print('''   --
           |   |
             --
           |   |
            --''')
    if s==' ':
        print('''   
               
               
               
            ''')
            

        #mall in vendor machine
class Square:
    def __init__(self, name):
        self.name = name
     #   self.stuff = stuff
        
    def printname(self):
        print(self.name)
        
Square1 = Square('square1')
        
square1.printname()

class Storage(Square):
    pass
    
storage1 = Storage('stoage1')

storage1.printname()

        if(welcome='*'):
            for p in BambooDesignedProductInventory1
            p.printname()
            shoppingcartoptions= input('Press * to add product to shopping cart, press cancel to cancel to order, press checkout to check out')
            if shoppingcartoptions='*':
                print(p, 'added')
                #declare new shopping cart
                ShoppingCart2 = ShoppingCart('ShoppingCart2',' '+p.name)
            
            if shoppingcartoptions='cancel':
                __main__ = 'cancel'
               print('cancel')
            if shoppingcartoptions = 'checkout':
                for p in ShoppingCart2:
                    print(p.printticket())
                    print('Thank you for your shop, good bye')
                    #print time when retail finished
                    if p = ShoppingCart2[-1]
                        while True:
#    sleep(1)
#    print(gmtime()[11:])
#    print(gmtime())
    sleep(1)
    for s in strftime('%c')[11:]:
        #numtodigit(str(s))
        numtodigit(str(s))
        
   # cmd.clear()
#    print(strftime('%c'))

tuplecontract1 = [00000001]
tuplewallet1 = [0x00000001]

class TupleCryptoContract(tuplewalletname, crypto):
    def __init__(self, tuplewalletname, stuff):
        self.tuplewalletname = tuplewalletname
        self.tuplecoin = tuplecoin     
    def ustdtotuplecoin(self):
        print(self.tuplewalletname, self.tuplecoin, self.contentcreation)
    def tuplecointoustd(self):
        print(self.tuplewalletname, self.tuplecoin, self.contentcreation)
 #   def contentcreation(self):
        #print(self.tuplewalletname, self.tuplecoin, self.contentcreation)
    def printname(self):
        print(self.tuplewalletname, self.tuplecoin)
 #   def nftsystem:
 #       print('grahic card')
    #def nftalgorithm(nft):
#        print(cryptoornft)
   # def cpualgorithm:
#        print(math.sin()+'cpu technology')
#    def memorycardorsimcard:
      #  print(sincard)
    
class TupleNFTContract(tuplewalletname, nft, contentcreation, sinangle):
    def __init__(self, tuplewalletname, nft):
        self.tuplewalletname = tuplewalletname
        self.tuplecoin = tuplecoin     
    def ustdtonft(self):
        print(self.tuplewalletname, self.tuplecoin, self.contentcreation)
    def nfttoustd(self):
        print(self.tuplewalletname, self.tuplecoin, self.contentcreation)
    def contentcreation(self):
        print(self.tuplewalletname, self.tuplecoin, self.contentcreation)
    def printname(self):
        print(self.tuplewalletname, self.tuplecoin)
    def nftsystem:
        print('grahic card')
    def nftalgorithm(nft):
        print(cryptoornft)
    def cpualgorithm(sinangle):
        print(math.sin(sinangle)+'cpu technology')
    def memorycardorsimcard:
        print(sincard)
        
def tupletransaction(tuplecontractmame, tuplewallet):
    tupletransaction = tuplecontract * tuplewallet
    return transaction
    
letterfacenft = ['aaaaa']   
tuplecoin  = [0000000000000001]

#wallet coin oop
class TupleCryptoWallet(TupleCryptoContract):
    pass
    
class TupleNFTWallet(TupleNFTContract):
    pass

marketcapitaloftuplecoin = '*'
tuplemarketvalueassumption = marketcapitaloftuplecoin

alchecmy = '*'

if __name__ = __main__:
    entershop=False
    aichatbotvendormachine = False
    aichatbotvendormachineofflinecenterbutton = False
    welcome = 'welcome to vert, enjoy your shop. Enter * to start your shopping journey.'
    internalitemseo = "bamboo postcard"
    print(re.search('^bamboo', txt3))
    if entershop and time(60) and aichatbotvendormachineofflinecenterbutton:
        input(welcome)
    print(tuplecoin)
    print('tuplecoin scan')
    for analytics in tuplemarketvalueassumption:
        print(analytics)
     #object declation      
TupleWallet1 = TupleWallet(tuplewallet1, tuplecoin)
    #wallet function call
    TupleWallet1.printname()
TupleWallet2 = TupleWallet(tuplewallet1, letterfacenft)
    #wallet function call
    TupleWallet1.printname()

    TupleWallet2.printname()

        
#note function didn't pass value to 
#ai chatbot
#if __name__ == '__main__':
    