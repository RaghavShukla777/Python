import mysql.connector as m
db=m.connect(host="localhost",user="root",passwd="Raghav@12",database="inventory")
cur=db.cursor()
print("+--------------------------------------------------------------------------+")
print("|                                                                          |")
print("|                  Welcome to Inventory Management System                  |")
print("|                                                                          |")
print("+--------------------------------------------------------------------------+")

while True:
    print("Choose an option:")
    print("1. Viewing inventory")
    print("2. Manipulating inventory")
    print("3. Exit")
    a=int(input("Enter :"))
    if a==1:
        while True:
             print("Choose your action:")
             print("1. Viewing the whole inventory.")
             print("2. Search a product")
             print("3. Table format")
             print("4. Go Back")
             b=int(input("Enter :"))
             if b==1:
                 cur.execute("Select * from electronics;")
                 for x in cur:
                     print(x)
             elif b==2:
                 while True:
                     print("Search by")
                     print("1. ID")
                     print("2. Brand Name ")
                     print("3. Item type")
                     print("4. Plant Location")
                     print("5. Go Back")
                     c=int(input("Enter:"))
                     if c==1:
                         p=input("Give Id:")
                         s="Select * from electronics where ID ='%s'" % (p,)
                         cur.execute(s)
                         for x in cur:
                             print(x)
                     elif c==2:
                         p=input("Give Brand Name:")
                         s="Select * from electronics where Brand ='%s'" % (p,)
                         cur.execute(s)
                         for x in cur:
                             print(x)
                         
                     elif c==3:
                         p=input("Give Item Type:")
                         s="Select * from electronics where MatDesc ='%s'" % (p,)
                         cur.execute(s)
                         for x in cur:
                             print(x)
                     elif c==4:
                         p=input("Give Plant Location:")
                         s="Select * from electronics where Plant ='%s'" % (p,)
                         cur.execute(s)
                         for x in cur:
                             print(x)

                     elif c==5:
                         break
                     else:
                         print("Invalid Input")
             elif b==3:
                 s="desc electronics"
                 cur.execute(s)
                 for x in cur:
                         print(x)
                 
             elif b==4:
                 break
             else :
                 print("Invalid entry")
                    
    elif a==2:         
        while True:        
             print("1. Adding or deleting a column.")
             print("2. Changing Table Values")
             print("3. Manipulate records")
             print("4. Go Back")
             b=int(input("Enter:"))
             if b==1:
                 while True:
                     print("1. Adding ")
                     print("2. Deleting")
                     print("3. Go Back")
                     c=int(input("Enter:"))
                     if c==1:
                            f=input("Column Name:")
                            g=input("Data Type:")
                            s="Alter table electronics add(%s   %s)"%(f,g)
                            cur.execute(s)
                            print("Table altered")
                            db.commit()
                         
                     elif c==2:
                            p=input("Give Column Name:")
                            s="Alter table electronics drop(%s)" % (p,)
                            cur.execute(s)
                            print("Column Removed")
                            cur.commit()
                     elif c==3:
                         break
                     else:
                         print("Invalid entry")
                 
             elif b==2:
                 while True:
                     print("Alter:") 
                     print("1. Stock ")
                     print("2. Plant")
                     print("3. Price")
                     print("4. Go Back")
                     c=int(input("Enter:"))
                     if c==1:
                         p=input("Give Item ID:")
                         q=int(input("Enter new stock value :"))
                         s="Update elecrtonics set stock =s where ID=%s;"%(q,p)
                         cur.execute(s)
                         print("Table altered")
                     elif c==2:
                         continue
                     elif c==3:
                         continue
                     elif c==4:
                         break
                     else:
                         print("Invalid input")
             elif b==3:
                 while True:
                     print("1. Entering Records")
                     print("2. Deleting Records")
                     print("3. Go Back")
                     c=int(input("Enter: "))
                     if c==1:
                           i=input("Enter ID: ")
                           mat=input("Enter Item Description: ")
                           p=input("Enter Plant: ")
                           st=int(input("Input stock amount : "))
                           sa=input("Enter sale availibility(Y/N): ")
                           pr=int(input("Enter price: "))
                           br=input("Enter brand: ")
                           query="Insert into electronics values('{0}','{1}','{2}',{3},'{4}',{5},'{6}')".format(i,mat,p,st,sa,pr,br)
                           cur.execute(query)
                           print(cur.rowcount()," Row entered")
                           db.commit()
                     elif c==2:
                           i=input("Enter ID: ")
                           q="delete from electronics where ID='%s'"%(i,)
                           cur.execute(q)
                           print(cur.rowcount()," Row deleted")
                           db.commit()
                     elif c==3:
                           break
                     else:
                           print("Invalid entry")
             elif b==4:
                 break
             else:
                 print("Invalid input")
    elif a==3:
        break
    else:
        print("Invalid entry")
print("Program ended")
db.close()