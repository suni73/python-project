print('Welcome to Bank ')
option2=int(input("choose option 1.signin 2.signup:"))
f=open('account.txt','w')
f.write('User Name')
f.write('\t')
f.write('Balance')
f.write('\t\t')
f.write('Credit AMT')
f.write('\t')
f.write('Debit Amt')
f.write('\t')
f.close()


f=open('customer.txt','w')
f.write('First Name')
f.write('\t')
f.write('Last Name')
f.write('\t')
f.write('User Name')
f.write('\t')
f.write('Password ')
f.write('\t')
f.write('Email ID')
f.write('\t')
f.close()
        






      
if option2==2:
    
    
    
    fname = raw_input("Please enter your First name:")
    lname = raw_input("Please enter your Last name:")
    password =raw_input("Enter your password. ")
    email =raw_input("Enter Email id:")
    if(email.endswith('@gmail.com')):
        
         
        print 'valid email'
    else:
        
         
        print 'enter correct email again'
    
    
    uname = fname + password[0:3]
    print("your username is :",uname)
    print ("Your account created successfully")

    file = open("customer.txt","a")
    file.write("\n")
    file.write(fname)
    file.write('\t\t')
    file.write(lname)
    file.write('\t\t')
    file.write(uname)
    file.write('\t')
    file.write(password)
    file.write('\t\t')
    file.write(email)
    file.write('\t')
    file.write('\n')
    file.close()

##transaction part

if option2==1:
    
    
    restart=('Y')
    chances = 3
    balance = 10000
    credit=0
    debit=0
    uname1=raw_input("Enter username:")
    while chances >= 0:
        
        
    
       raw_input("Enter your name:")
       raw_input("Enter your password:")
       pin = int(input('Please Enter You 4 Digit Pin: '))
       if pin == (1234):

        print('You entered you pin Correctly\n')
        while restart not in ('n','NO','no','N'):
            
            print('Please Press 1 For Balance\n')
            print('Please Press 2 For Debit amt\n')
            print('Please Press 3 For credi amt\n')
            print('Please Press 4 To Return Card\n')
        
            
                
            #uname=raw_input("Enter username:")
            option = int(input('What Would you like to choose? press 1,2,3,or 4'))
            if option == 1:
                print('Your Balance is ',balance)
                f=open("account.txt",'a')
                f.write('\n')
                f.write(uname1)
                f.write('\t\t')
                f.write(str(balance))
                f.write('\t\t')
                f.write(str(credit))
                f.write('\t\t')
                f.write(str(debit))
                f.write('\t\t')
                f.close()
                
                restart = input('Would You you like to go back? press 1 or 2 ')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break






                   

            elif option == 2:
                option2 = ('y')
                debit = float(input('How Much Would you like to withdraw?  '))
                if debit>0:
                    balance = balance - debit
                    print ('\nYour Balance is now ',balance)

                    f=open("account.txt",'a')
                    f.write('\n')
                    f.write(uname1)
                    f.write('\t\t')
                    f.write(str(balance))
                    f.write('\t\t')
                    f.write(str(credit))
                    f.write('\t\t')
                    f.write(str(debit))
                    f.write('\t\t')
                    f.close()

                    
                    restart = input('Would You you like to go back? ')
                    if restart in ('n','NO','no','N'):
                        print('Thank You')
                        break

                elif debit<0:
                    print('Invalid Amount, Please Re-try\n')
                    restart = ('y')
                elif debit == 1:
                    debit = float(input('Please Enter Desired amount:'))    

            elif option == 3:
                credit= float(input('How Much Would You Like To Pay In? '))
                balance = balance + credit
                print ('\nYour Balance is now ',balance)
                f=open("account.txt",'a')
                f.write('\n')
                f.write(uname1)
                f.write('\t\t')
                f.write(str(balance))
                f.write('\t\t')
                f.write(str(credit))
                f.write('\t\t')
                f.write(str(debit))
                f.write('\t\t')
                f.close()





                restart = input('Would You you like to go back?press 1 or 2 ')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option == 4:
                print('Please wait whilst your card is Returned...\n')
                print('Thank you for use our service')
                break
            else:
                print('Please Enter a correct number. \n')
                restart = ('y')
       elif pin != ('1234'):
           
           
           print('Incorrect Password')
           
            
           chances = chances - 1
            
           if chances == 0:
               
               
                
               print('\nNo more tries')
               
                
               break
