import random
import datetime
import os
list_nama = []
phno = []
list_jmlhkmr= []
list_jmlhtamu=[]
checkin = []
checkout = []
list_room = []
price = []
rc = []
roomno = []
custid = []
day = []

i = 0

def home():
    os.system("cls")
    print("\t           ██╗  ██╗ ██████╗ ████████╗███████╗██╗")
    print("\t           ██║  ██║██╔═══██╗╚══██╔══╝██╔════╝██║  ")   
    print("\t           ███████║██║   ██║   ██║   █████╗  ██║   ")  
    print("\t           ██╔══██║██║   ██║   ██║   ██╔══╝  ██║    ") 
    print("\t           ██║  ██║╚██████╔╝   ██║   ███████╗███████╗")
    print("\t           ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚══════╝")
    print("\t                                                 ███╗   ███╗ █████╗ ██╗    ██╗ █████╗ ██████╗ ")
    print("\t                                                 ████╗ ████║██╔══██╗██║    ██║██╔══██╗██╔══██╗")
    print("\t                                                 ██╔████╔██║███████║██║ █╗ ██║███████║██████╔╝")
    print("\t                                                 ██║╚██╔╝██║██╔══██║██║███╗██║██╔══██║██╔══██╗")
    print("\t                                                 ██║ ╚═╝ ██║██║  ██║╚███╔███╔╝██║  ██║██║  ██║")
    print("\t                                                 ╚═╝     ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝\n")
    print("+=======================================================+")
    print("|                   HOTEL MENU                          |")
    print("|=======================================================|")
    print("| 1 | Booking                                           |")
    print("| 2 | Rooms Info                                        |")
    print("| 3 | Room Service(Menu Card)                           |")
    print("| 4 | Record                                            |")
    print("| 5 | Exit                                              |")
    print("|_______________________________________________________|")    
    try:
        ch=int(input("\nPilih Menu --> "))
    except:
        os.system("cls")
        home()
    if ch == 1:
        os.system("cls")
        booking()
    elif ch == 2:
        os.system("cls")
        rooms_Info()
    elif ch == 3:
        os.system("cls")
        restaurant()
    elif ch == 4:
        os.system("cls")
        record()
    else:
        print("Pilihan tidak ada...!!!")


def booking():
    harga=0
    rom=0
    global i
    os.system("cls")
    print("\t\t BOOKING ROOMS")
    print(" ")
    while True:
        nama = str(input("Name: "))
        p1 = str(input("Phone No.: "))
  
        if nama!=" " and p1!=" ":
            list_nama.append(nama)
            phno.append(p1)
            break		
        else:
            print("\tName, Phone no. tidak boleh kosong...!!!")
            
    print("Contoh format : 01/02/2022")
    while True: 
        cii=str(input("Check-In: "))
        if "/" in cii:
            checkin.append(cii)
            ci=cii
            cii=cii.split('/')
            cii[0]=int(cii[0])
            cii[1]=int(cii[1])
            cii[2]=int(cii[2])
            break
    while True:	
        coo=str(input("Check-Out: "))
        if "/" in coo:
            checkout.append(coo)
            co=coo
            coo=coo.split('/')
            coo[0]=int(coo[0])
            coo[1]=int(coo[1])
            coo[2]=int(coo[2])
            break
    
    d1 = datetime.datetime(cii[2],cii[1],cii[0])
    d2 = datetime.datetime(coo[2],coo[1],coo[0])
    d = (d2-d1).days
    day.append(d)
        
    os.system("cls")
    print("----SELECT ROOM TYPE----")
    print(" 1. Standard Non-AC")
    print(" 2. Standard AC")
    print(" 3. 3-Bed Non-AC")
    print(" 4. 3-Bed AC")
    print(("\t\tPress 0 for Room Prices"))
  
    ch=int(input("\nPilih Room --> "))
		
		
    if ch==0:
        print(" 1. Standard Non-AC -  Rp.350,000")
        print(" 2. Standard AC     -  Rp.400,000")
        print(" 3. 3-Bed Non-AC    -  Rp.4500,00")
        print(" 4. 3-Bed AC        -  Rp.500,000")
        ch=int(input("->"))
    if ch==1:
        rom="Standard Non-AC"
        list_room.append(rom)
        print("Room Type- Standard Non-AC")
        harga=350000
        price.append(harga)
        print("Price- 350,000")
    elif ch==2:
        rom='Standard AC'
        list_room.append(rom)
        print("Room Type- Standard AC")
        harga=400000
        price.append(harga)
        print("Price- 400,000")
    elif ch==3:
        rom='3-Bed Non-AC'
        list_room.append(rom)
        print("Room Type- 3-Bed Non-AC")
        harga=450000
        price.append(harga)
        print("Price- 450,000")
    elif ch==4:
        rom='3-Bed AC'
        list_room.append(rom)
        print("Room Type- 3-Bed AC")
        harga=500000
        price.append(harga)
        print("Price- 500,000")
    else:
        print(" Wrong choice..!!")
    
    jmlhkmr=int(input("Berapa kamar : "))
    tamu=input("Jumlah Tamu : ")
    
    list_jmlhkmr.append(jmlhkmr)
    list_jmlhtamu.append(tamu)
    
    rn = random.randrange(400)
    cid = random.randrange(900)
			
    while rn in roomno or cid in custid:
        rn = random.randrange(600)
        cid = random.randrange(1000)
			
    rc.append(0)
    total=harga*jmlhkmr
    os.system("cls")		
    print("\t\t\t DATA PESANAN \n")
    print("Nama Pemesan  :",nama)
    print("No HP         :",p1)
    print("Room Type     : ",rom)
    print("Jumlah kamar  :",jmlhkmr)
    print(f"Harga kamar   : {harga}")
    print("Lama menginap :",d,"Hari")
    tnya=input("Lanjutkan Pembayaran (Y/N) ? ")
    if tnya=="n":
        list_nama.pop()
        phno.pop()
        checkin.pop()
        checkout.pop()
        day.pop()
        booking()
    
    print(f"\nTotal Pembayran {total:,}")
    uang=int(input("Uang bayar : "))
    kmbli=uang-total
    os.system("cls")
    print("\t\t\t======STRUK BOOKING======= \n")
    
    print("Data Pemesan")
    print('='*40)
    print("Nama Tamu :",nama)
    print("No HP        :",p1)
    print("\nDetail Pesanan")
    print('='*40)
    print("|Checkin         |Checkout ")
    print(f" {ci}\t {co}")
    print("\nLama menginap   :",d,"Hari")
    print("Tamu per kamar  :",tamu)
    print("Nomor kamar     :",rn)
    print("Costumer ID     :",cid)
    print(f"\n-----------------------------------------------------------------------")
    print(f"|   Pesanan    |    Room type      |Jumlah |Harga perkamar |   Total   |")
    print(f"|--------------------------------------------------------------------- |")
    print(f"|  Hotel Room  |  {rom}  |   {jmlhkmr}   |   {harga:,}     | {total:,}   |")
    print(f"|--------------------------------------------------------------------- |")
    print(f"|                                               total harga : {harga:,}  |")
    print(f"|                                               Uang Anda   : {uang:,}  |")
    print(f"|                                               kembalian   : {kmbli:,}  |")
    print("-----------------------------------------------------------------------")
    
    
    
    roomno.append(rn)
    custid.append(cid)
    i=i+1
    n=int(input("0-BACK ---> "))
    if n==0:
        os.system("cls")
        home()

# ROOMS INFO
def rooms_Info():
    print("		 ------ HOTEL ROOMS INFO ------")
    print("")
    print("STANDARD NON-AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed, Television, Telephone,")
    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
    print("an attached washroom with hot/cold water.\n")
    print("STANDARD NON-AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed, Television, Telephone,")
    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
    print("an attached washroom with hot/cold water + Window/Split AC.\n")
    print("3-Bed NON-AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1")
    print("Side table, Balcony with an Accent table with 2 Chair and an")
    print("attached washroom with hot/cold water.\n")
    print("3-Bed AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, ")
    print("1 Side table, Balcony with an Accent table with 2 Chair and an")
    print("attached washroom with hot/cold water + Window/Split AC.\n\n")
    print()
    n=int(input("0-BACK ---> "))
    if n==0:
        os.system("cls")
        home()

# RESTAURANT FUNCTION
def restaurant():
    ph=int(input("Customer Id: "))
    global i
    f=0
    r=0
    for n in range(0,i):
        if roomno[n]==ph:
            f=1
            print("-------------------------------------------------------------------------")
            print("|					          Menu Card                                 |")
            print("-------------------------------------------------------------------------")
            print("BEVARAGES							  Roti                              ")
            print("----------------------------------	  ----------------------------------")
            print(" 1 Regular Tea............. 10,000	  9  Dal Tadka..............  15,000")
            print(" 2 Masala Tea.............. 15,000     10 Plain Roti.............. 15,000")
            print(" 3 Coffee.................. 20,000     11 Butter Roti............. 15,000")
            print(" 4 Cold Drink.............. 20,000     12 Tandoori Roti........... 20,000")
            print(" 5 Bread Butter............ 30,000	  13 Butter Naan............. 20,000")
            print(" 6 Bread Jam............... 30,000	 ")
            print(" 7 Veg. Sandwich........... 50,000	 ")
            print(" 8 Veg. Toast Sandwich..... 50,000	 ")
			
            print("masukan 0 - untuk akhiri ")
            ch=1
            while(ch!=0):
                ch=int(input("Pilih Menu--> "))
                if ch==1 :
                    rs=20000
                    r=r+rs
                elif ch==2 or ch==4:
                    rs=25000
                    r=r+rs
                elif ch==5 or ch==6:
                    rs=30000
                    r=r+rs
                elif ch==7 or ch==8:
                    rs=50000
                    r=r+rs
                elif ch==11 or ch==9 or ch==12:
                    rs=70000
                    r=r+rs
                else:
                    print("Pilihan Salahh..!!")
                    print("Total Bill: ",r)
			
            r=r+rc.pop(n)
            rc.append(r)
            
    if f == 0:
            print("Customer Id Tidak ditemukan")
    n=int(input("0-BACK ---> "))
    if n==0:
        os.system("cls")
        home()
	
				
def record():
    if phno!=[]:
        print("|----------------------------------------------------------------------------------------------------------------------|")
        print("\t\t\t\t	 *** HOTEL RECORD ***    ")
        print("----------------------------------------------------------------------------------------------------------------------|")
        print("| Name   | Phone No.   | Check-In   | Check-Out	 | Room Type	 | Price	 |Day ")
        print("----------------------------------------------------------------------------------------------------------------------|")
		
        for n in range(0,i):
            print("|",list_nama[n]," |",phno[n],"|",checkin[n],"|",checkout[n],"|",list_room[n],"|",price[n],"|",day[n],"Day")
		
        print("----------------------------------------------------------------------------------------------------------------------|")
	
    else:
        print("No Records Found")
    n = int(input("0-BACK --->"))
    if n == 0:
        os.system("cls")
        home()


home()