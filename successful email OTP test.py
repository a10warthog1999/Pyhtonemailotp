import os
import math
import random
import smtplib
import sys
from tkinter import messagebox, simpledialog, Tk

root = Tk()
root.title('Triple OTP verfication')
root.geometry('300x100')


def otpgenerator():
    digits="0123456789"
    OTP=""
    for i in range(6):
        OTP+=digits[math.floor(random.random()*10)]
    msg = OTP
    return msg


def name():
    name = simpledialog.askstring('Email Id', 'Enter the email associated with the organization ')
    return name

def name1():
    name1= simpledialog.askstring('Email Id', 'Enter email id linked to Aadhar card/PAN card ')
    return name1

def name2():
    name2 = simpledialog.askstring('Email Id', 'Enter email id of the Nominee')
    return name2

def key():
    key = simpledialog.askstring('Secret Key', 'Enter the secret key: ')
    return key



def otpverification():
    newname=name()
    newkey=key()
    newmsg=otpgenerator()
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(newname,newkey)
    s.sendmail('&&&&&&&&&&&',newname,newmsg)
    a = simpledialog.askstring('OTP', 'Enter OTP')
    
    if a == newmsg:
        messagebox.showinfo('Verified','Successful Verification')
        res = messagebox.askquestion('Attention', 'Is your adhar email same as 1st email')
        if res == 'yes':
            messagebox.showinfo('Verification','Adhaar email verification')
            newmsg1=otpgenerator()
            s.login(newname,newkey)
            s.sendmail('&&&&&&&&&&&',newname,newmsg1)
            b = simpledialog.askstring('Adhar verification','Enter Your OTP from adhaar registrered email id>>: ')
        elif res == 'no':
            messagebox.showinfo("Adhaar email verification")
            newname1=name1()
            newkey1=key()
            newmsg1=otpgenerator()
            s.login(newname1,newkey1)
            s.sendmail('&&&&&&&&&&&',newname1,newmsg1)
            b = simpledialog.askstring('Adhar verification','Enter Your OTP from adhaar registrered email id>>: ')
        
        if b == newmsg1:
            messagebox.showinfo('Verified','Successful Verification')
            messagebox.showinfo('Verification','Nominee email verification')
            newname2=name2()
            newkey2=key()
            newmsg2=otpgenerator()
            s.login(newname2,newkey2)
            s.sendmail('&&&&&&&&&&&',newname2,newmsg2)
            c = simpledialog.askstring('Nominee','Enter Your OTP from nominee registrered email id>>: ')

            if c == newmsg2:
                messagebox.showinfo('Verified','You are successfully logged in')
                root.destroy();
                
            else:
                messagebox.showinfo("Not Verified")
                sys.exit()      
        else:
            messagebox.showinfo("Not Verified")
            sys.exit();
    else:
        messagebox.showinfo("Not Verified")
        sys.exit()



otpverification()

root.mainloop()



#shahzaib.b@somaiya.edu
#qjymnwxrfuykbubv


        
            
              
        
    
    
    
    
    
    
    
    
        
        
    
    

