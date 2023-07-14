'''import all the necessary modules for running the software'''

from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox

# create a window and resize,add label and colour as per requirement
root = Tk()
root.geometry("1400x900")
root.title("Tour and Travel booking")
root.resizable(0,0)
root.config(bg="black")
tour_label=Label(root,text="Travel and Tour Booking",font=("Arial",30,"bold"),fg="#1874CD")
tour_label.place(x=1,y=0)

def home():
    '''Create a home function which imports home page itself'''
    root.destroy()
    import led

def payment():

    root_pay=Toplevel(root)
    root_pay.title("payment form")
    if frame_book is not None:
      frame_book.destroy()

     



def booking():
     '''Create a booking function which displays the form for filling details in order to book the respective tour'''
     global frame_book
     frame_book=Frame(root,width=700,height=320)
     frame_book.place(x=300,y=100)
     but_Next=Button(frame_book,text="Next",font=18,width=20,command=payment)
     but_Next.place(x=300,y=290)
     label_book1=Label(frame_book,text=" Tour Booking form",font=("Arial",24,"bold"))
     label_book1.place(x=0,y=0)

     months=StringVar()

     combobox1 =ttk.Combobox(frame_book,textvariable=months,values=("jan","feb","march","april","may","june","july","august","september","october","november","december"),width=5,state="readonly")
     combobox1.place(x=500,y=250)
     day=StringVar()
     num=[]
     for i in range(1,33):
            num.append(i)

     combobox1 =ttk.Combobox(frame_book,textvariable=day,values=num,width=2,state="readonly")
     combobox1.place(x=570,y=250)
     year= StringVar()
     spinbox = Spinbox(frame_book,textvariable=year,from_=2023,to_=2100,state="readonly",width=4)
     spinbox.place(x=625,y=250)

     months=StringVar()

     combobox1 =ttk.Combobox(frame_book,textvariable=months,values=("jan","feb","march","april","may","june","july","august","september","october","november","december"),width=5,state="readonly")
     combobox1.place(x=150,y=250)
     day=StringVar()
     num=[]
     for i in range(1,33):
            num.append(i)

     combobox1 =ttk.Combobox(frame_book,textvariable=day,values=num,width=2,state="readonly")
     combobox1.place(x=220,y=250)
     year= StringVar()
     spinbox = Spinbox(frame_book,textvariable=year,from_=2023,to_=2100,state="readonly",width=4)
     spinbox.place(x=275,y=250)


     label_book2=Label(frame_book,text="Name")
     label_book2.place(x=0,y=50)
     labela_book2=Label(frame_book,text="Contact No")
     labela_book2.place(x=350,y=50)
     labela_book3=Label(frame_book,text="Email")
     labela_book3.place(x=350,y=100)
     labela_book4=Label(frame_book,text="Password")
     labela_book4.place(x=350,y=150)
     label_book3=Label(frame_book,text="Surame")
     label_book3.place(x=0,y=100)
     label_book2_entry=Entry(frame_book,text="")
     label_book2_entry.place(x=100,y=50)
     label_book3_entry=Entry(frame_book,text="")
     label_book3_entry.place(x=100,y=100)
     labela_book2_entry=Entry(frame_book,text="")
     labela_book2_entry.place(x=450,y=50)
     labela_book3_entry=Entry(frame_book,text="")
     labela_book3_entry.place(x=450,y=100)
     labela_book3_entry=Entry(frame_book,text="",show="*")
     labela_book3_entry.place(x=450,y=150)
    #  visitors=Entry(frame_book,width=50)\
     label_book4=Label(frame_book,text="Number of Visitors")
     label_book4.place(x=0,y=150)
     no_of_visitors=StringVar()
     num=[]
     for i in range(1,31):
          num.append(i)
     combobox1=ttk.Combobox(frame_book,textvariable=no_of_visitors,values=num,state="readonly",width=10)
     combobox1.place(x=150,y=150)
     label_book5=Label(frame_book,text="Number of Tour Guides")
     label_book5.place(x=0,y=200)
     label_book5=Label(frame_book,text="Start Date")
     label_book5.place(x=0,y=250)
     label_book5=Label(frame_book,text="End Date")
     label_book5.place(x=370,y=250)
     label_book5=Label(frame_book,text="Amount")
     label_book5.place(x=350,y=200)
     labela_book3_entry=Entry(frame_book,text="",show="*")
     labela_book3_entry.place(x=450,y=200)
     no_of_visitors=StringVar()
     num=[]
     for i in range(1,6):
          num.append(i)
     combobox1=ttk.Combobox(frame_book,textvariable=no_of_visitors,values=num,state="readonly",width=10)
     combobox1.place(x=150,y=200)
frame1=Frame()

# frame_places=Frame(root,width=1400,height=1200)
# frame_places.place(x=0,y=35)

def everest1():
    global frame_places
    global frame_everest

    frame_everest=Frame(root,width=1400,height=1200)
    frame_everest.place(x=0,y=0)
    # label1=Label(frame_everest,text="this is the good adventerous places of Nepal")
    # label1.place(x=100,y=500)
    button_booking=Button(frame_everest,text="Book Your tour ",font=40,fg="green",command=booking)
    button_booking.configure(width=10,height=2)

    button_booking.place(x=320,y=760)
    image=Image.open("everest1.jpg")
    resized_image=image.resize((700,500))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_everest,image=converted)
    label.image=converted
    label.place(x=0,y=0)
    image=Image.open("everest1.jpg")
    resized_image=image.resize((700,500))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_everest,image=converted)
    label.image=converted
    label.place(x=700,y=0)
    
    laabel=Label(frame_everest,text="Everest base camp trek",font=("calibri",24,"bold"))
    laabel.place(x=30,y=510)
    laabela=Label(frame_everest,text="From kathmandu to solukhumbu",font=("Avenir",24,"bold"),fg="green")
    laabela.place(x=370,y=510)
    # frame_duration=Frame(frame_everest,width=190,height=95)
    # frame_duration.place(x=30,y=550)
    labeel1=Label(frame_everest,text="Duration\n9 days",font=("Avenir",18,"bold"),fg="grey")
    labeel1.place(x=30,y=560)
    labeel2=Label(frame_everest,text="Tour languages\nEnglish  Nepali",font=("Avenir",18,"bold"),fg="grey")
    labeel2.place(x=220,y=560)
    labeel3=Label(frame_everest,text="Age Group \n12-75",font=("Avenir",18,"bold"),fg="grey")
    labeel3.place(x=430,y=560)
    labeel4=Label(frame_everest,text="Services and Facilities\n\t\tIncluded:Food, Acommodation,Travel expense\n\t\tNot included Personal expense\t medical expense",font=("Avenir",18,"bold"),fg="grey")
    labeel4.place(x=800,y=560)
    labeel5=Label(frame_everest,text="Group size\n1-30",font=("Avenir",18,"bold"),fg="grey")
    labeel5.place(x=590,y=560)
    labeel6=Label(frame_everest,text="District\nSolukhumbu",font=("Avenir",18,"bold"),fg="grey")
    labeel6.place(x=750,y=560)

    laabel7=Label(frame_everest,text=" Tour Overview",font=("calibri",24,"bold"))
    laabel7.place(x=30,y=630)
    labeel8=Label(frame_everest,text="It is more than a trekking as one can see a beautiful scenery of highest mountain in the world.The  everest base- \ncamp's peak elevation is 5364 meters (17598 feet) So people suffering from acrophobia should not try this cause,\n they may suffer from altitude sickness. The one who is a regular traveller or who can think they can should try this.  ",font=("Avenir",17))
    labeel8.place(x=30,y=660)
    labeel9=Label(frame_everest,text="Day1: Kathmandu Airport-Lukla airport- trek to phakding \nDay2: phakding to namche bazaar                             \nDay3: Namche bazaar to tangboche                      \n Day:4 Trek to Dingbouche and trek to Louche\nDay5: Trek to Everest base camp                \n\t  Day6:Trek to kalapathar and back Namchebazaar      \n         Day7: Back to Lukla and back to Kathmandu",font=("Avenir",17))
    labeel9.place(x=900,y=660)
    
everest1()


def Ilam():
    global frame_Ilam

    frame_Ilam=Frame(root,width=1400,height=1200)
    frame_Ilam.place(x=0,y=35)
    # label1=Label(frame_Ilam,text="this is the good adventerous places of Nepal")
    # label1.place(x=100,y=500)
    button_booking=Button(frame_Ilam,text="Book ",font=40,bg="white",fg="green",command=booking)
    button_booking.configure(width=20,height=10)

    button_booking.place(x=320,y=760)
    image=Image.open("everest1.jpg")
    resized_image=image.resize((700,500))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_Ilam,image=converted)
    label.image=converted
    label.place(x=0,y=0)
    image=Image.open("everest1.jpg")
    resized_image=image.resize((700,500))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_Ilam,image=converted)
    label.image=converted
    label.place(x=700,y=0)
    
    laabel=Label(frame_Ilam,text="Ilam  trek",font=("calibri",24,"bold"))
    laabel.place(x=30,y=510)
    laabela=Label(frame_Ilam,text="From kathmandu to Ilam",font=("Avenir",24,"bold"),fg="green")
    laabela.place(x=370,y=510)
    # frame_duration=Frame(frame_Ilam,width=190,height=95)
    # frame_duration.place(x=30,y=550)
    labeel1=Label(frame_Ilam,text="Duration\n4 days",font=("Avenir",18,"bold"),fg="grey")
    labeel1.place(x=30,y=560)
    labeel2=Label(frame_Ilam,text="Tour languages\nEnglish  Nepali",font=("Avenir",18,"bold"),fg="grey")
    labeel2.place(x=220,y=560)
    labeel3=Label(frame_Ilam,text="Age Group \nAll age group",font=("Avenir",18,"bold"),fg="grey")
    labeel3.place(x=430,y=560)
    labeel4=Label(frame_Ilam,text="Services and Facilities\n\t\tIncluded:Food, Acommodation,Travel expense\n\t\tNot included Personal expense\t medical expense",font=("Avenir",18,"bold"),fg="grey")
    labeel4.place(x=800,y=560)
    labeel5=Label(frame_Ilam,text="Group size\n1-30",font=("Avenir",18,"bold"),fg="grey")
    labeel5.place(x=590,y=560)
    labeel6=Label(frame_Ilam,text="District\n Ilam",font=("Avenir",18,"bold"),fg="grey")
    labeel6.place(x=750,y=560)

    laabel7=Label(frame_Ilam,text=" Tour Overview",font=("calibri",24,"bold"))
    laabel7.place(x=30,y=630)
    labeel8=Label(frame_Ilam,text="Taking a break from your daily life is quite necessary to be mentally fresh,in such case Ilam might be your\n best places to chilling around.It is a district in eastern oart of Nepal connected with india separating \nthe mechi river.It is popular for unique green terrace fields It is about 700 km away from kathmandu.\n It takes about 12-13 hours to reach there.",font=("Avenir",17))
    labeel8.place(x=30,y=660)
    labeel9=Label(frame_Ilam,text="Day1: Kathmandu to Ilam Bazaar\nDay2:Ilam bazaar to Antu dada to maipokhari \nDay3: maipokhari to pashupatinagar to fikkal \nDay4: Fikkal to Ithari to kathmandu",font=("avenir",17))
    labeel9.place(x=990,y=700)
    
    button_booking=Button(frame_everest,text="Book ")
    button_booking.place(x=500,y=900)
Ilam()

def janakpur():
    global frame_janaki

    frame_janaki=Frame(root,width=1400,height=1200)
    frame_janaki.place(x=0,y=35)
    # label1=Label(frame_janaki,text="this is the good adventerous places of Nepal")
    # label1.place(x=100,y=500)
    button_booking=Button(frame_janaki,text="Book Your tour ",font=40,fg="green",command=booking)
    button_booking.configure(width=10,height=2)

    button_booking.place(x=320,y=760)
    image=Image.open("everest1.jpg")
    resized_image=image.resize((700,500))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_janaki,image=converted)
    label.image=converted
    label.place(x=0,y=0)
    image=Image.open("everest1.jpg")
    resized_image=image.resize((700,500))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_janaki,image=converted)
    label.image=converted
    label.place(x=700,y=0)
    
    laabel=Label(frame_janaki,text="Tour to Janakpur(Temple of janak)",font=("calibri",24,"bold"))
    laabel.place(x=30,y=510)
    laabela=Label(frame_janaki,text="From kathmandu to Dhanusha",font=("Avenir",24,"bold"),fg="green")
    laabela.place(x=470,y=510)
    # frame_duration=Frame(frame_janaki,width=190,height=95)
    # frame_duration.place(x=30,y=550)
    labeel1=Label(frame_janaki,text="Duration\n3 days",font=("Avenir",18,"bold"),fg="grey")
    labeel1.place(x=30,y=560)
    labeel2=Label(frame_janaki,text="Tour languages\nEnglish  Nepali",font=("Avenir",18,"bold"),fg="grey")
    labeel2.place(x=220,y=560)
    labeel3=Label(frame_janaki,text="Age Group \nAll age group",font=("Avenir",18,"bold"),fg="grey")
    labeel3.place(x=430,y=560)
    labeel4=Label(frame_janaki,text="Services and Facilities\n\t\tIncluded:Food, Acommodation,Travel expense\n\t\tNot included Personal expense\t medical expense",font=("Avenir",18,"bold"),fg="grey")
    labeel4.place(x=800,y=560)
    labeel5=Label(frame_janaki,text="Group size\n1-30",font=("Avenir",18,"bold"),fg="grey")
    labeel5.place(x=590,y=560)
    labeel6=Label(frame_janaki,text="District\nSolukhumbu",font=("Avenir",18,"bold"),fg="grey")
    labeel6.place(x=750,y=560)

    laabel7=Label(frame_janaki,text=" Tour Overview",font=("calibri",24,"bold"))
    laabel7.place(x=30,y=630)
    labeel8=Label(frame_janaki,text=" Janakpur dham is a tour of historical sites at janakpur ,birthplace of sita. All the hindu people\n worshipped this place as a great ceremony in chhath. Jankpur is popular with different historical and \nrelifious events. It is one of the most holy places of hindus.  You can get a chance to explore\n maithili culture and traditions by visiting there.",font=("Avenir",17))
    labeel8.place(x=30,y=660)
    labeel9=Label(frame_janaki,text="Day1: Kathmandu to Shree Ram Janaki Mandir (225 km) 7/8 hours. Overnight Stay. \nDay2:     Puja and full day sightseeing. Overnight Stay                      \nDay3: Drive back to Kathmandu by vehicles-7/8 hours.     ",font=("Avenir",17))
    labeel9.place(x=850,y=660)
    
janakpur() 

def koshi():
    global frame_koshi

    frame_koshi=Frame(root,width=1400,height=1200)
    frame_koshi.place(x=0,y=35)
    # label1=Label(frame_koshi,text="this is the good adventerous places of Nepal")
    # label1.place(x=100,y=500)
    button_booking=Button(frame_koshi,text="Book Your tour ",font=40,fg="green",command=booking)
    button_booking.configure(width=15,height=3)

    button_booking.place(x=320,y=790)
    image=Image.open("everest1.jpg")
    resized_image=image.resize((700,500))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_koshi,image=converted)
    label.image=converted
    label.place(x=0,y=0)
    image=Image.open("everest1.jpg")
    resized_image=image.resize((700,500))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_koshi,image=converted)
    label.image=converted
    label.place(x=700,y=0)
    
    laabel=Label(frame_koshi,text="Tour to Koshitappu wildlife reserve",font=("calibri",24,"bold"))
    laabel.place(x=30,y=510)
    laabela=Label(frame_koshi,text="From kathmandu to Koshitappu(Morang)",font=("Avenir",24,"bold"),fg="green")
    laabela.place(x=470,y=510)
    # frame_duration=Frame(frame_koshi,width=190,height=95)
    # frame_duration.place(x=30,y=550)
    labeel1=Label(frame_koshi,text="Duration\n4 days",font=("Avenir",18,"bold"),fg="grey")
    labeel1.place(x=30,y=560)
    labeel2=Label(frame_koshi,text="Tour languages\nEnglish  Nepali",font=("Avenir",18,"bold"),fg="grey")
    labeel2.place(x=220,y=560)
    labeel3=Label(frame_koshi,text="Age Group \nAll age group",font=("Avenir",18,"bold"),fg="grey")
    labeel3.place(x=430,y=560)
    labeel4=Label(frame_koshi,text="Services and Facilities\n\t\tIncluded:Food, Acommodation,Travel expense\n\t\tNot included Personal expense\t medical expense",font=("Avenir",18,"bold"),fg="grey")
    labeel4.place(x=800,y=560)
    labeel5=Label(frame_koshi,text="Group size\n1-30",font=("Avenir",18,"bold"),fg="grey")
    labeel5.place(x=590,y=560)
    labeel6=Label(frame_koshi,text="District\nMorang",font=("Avenir",18,"bold"),fg="grey")
    labeel6.place(x=750,y=560)

    laabel7=Label(frame_koshi,text=" Tour Overview",font=("calibri",24,"bold"))
    laabel7.place(x=30,y=630)
    labeel8=Label(frame_koshi,text="It is a wildlife reserve established in 1976 AD . It covers an area of 176 sq km.\n It was declared a Ramsar site, a wetland of international significance. Government of Nepal has declared \nthe buffer zone ( 173.5 sq. km ) surrounding the reserve in 2004.The reserve has important \nhabitat for a variety of wildlife. The last surviving population of Wild buffalo is found here.\n The estimated population of wild buffalo is around 159 individuals is dwindling.",font=("Avenir",17))
    labeel8.place(x=30,y=660)
    labeel9=Label(frame_koshi,text="Day1: Kathmandu to Biratnagar(by plane) and visit biratnagar \nDay2: Drive to Koshitappu reserve camp                        \nDay3:Explore koshitappu wildlife reserve and places near there. \n Day4:Jungle safari and enjoy the beautu of forest\n Day5: Fly back to Kathmandu via Biratnagar     ",font=("Avenir",17))
    labeel9.place(x=850,y=660)
   
koshi() 

def pashupatinath():
    global frame_janaki

    frame_janaki=Frame(root,width=1400,height=1200)
    frame_janaki.place(x=0,y=35)
    # label1=Label(frame_janaki,text="this is the good adventerous places of Nepal")
    # label1.place(x=100,y=500)
    button_booking=Button(frame_janaki,text="Book Your tour ",font=40,fg="green",command=booking)
    button_booking.configure(width=10,height=2)

    button_booking.place(x=320,y=760)
    image=Image.open("everest1.jpg")
    resized_image=image.resize((700,500))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_janaki,image=converted)
    label.image=converted
    label.place(x=0,y=0)
    image=Image.open("everest1.jpg")
    resized_image=image.resize((700,500))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_janaki,image=converted)
    label.image=converted
    label.place(x=700,y=0)
    
    laabel=Label(frame_janaki,text="Tour to pashupatinath(Temple of janak)",font=("calibri",24,"bold"))
    laabel.place(x=30,y=510)
    laabela=Label(frame_janaki,text="From kathmandu to Dhanusha",font=("Avenir",24,"bold"),fg="green")
    laabela.place(x=470,y=510)
    # frame_duration=Frame(frame_janaki,width=190,height=95)
    # frame_duration.place(x=30,y=550)
    labeel1=Label(frame_janaki,text="Duration\n3 days",font=("Avenir",18,"bold"),fg="grey")
    labeel1.place(x=30,y=560)
    labeel2=Label(frame_janaki,text="Tour languages\nEnglish  Nepali",font=("Avenir",18,"bold"),fg="grey")
    labeel2.place(x=220,y=560)
    labeel3=Label(frame_janaki,text="Age Group \nAll age group",font=("Avenir",18,"bold"),fg="grey")
    labeel3.place(x=430,y=560)
    labeel4=Label(frame_janaki,text="Services and Facilities\n\t\tIncluded:Food, Acommodation,Travel expense\n\t\tNot included Personal expense\t medical expense",font=("Avenir",18,"bold"),fg="grey")
    labeel4.place(x=800,y=560)
    labeel5=Label(frame_janaki,text="Group size\n1-30",font=("Avenir",18,"bold"),fg="grey")
    labeel5.place(x=590,y=560)
    labeel6=Label(frame_janaki,text="District\nSolukhumbu",font=("Avenir",18,"bold"),fg="grey")
    labeel6.place(x=750,y=560)

    laabel7=Label(frame_janaki,text=" Tour Overview",font=("calibri",24,"bold"))
    laabel7.place(x=30,y=630)
    labeel8=Label(frame_janaki,text=" pashupatinath dham is a tour of historical sites at pashupatinath ,birthplace of sita. All the hindu people\n worshipped this place as a great ceremony in chhath. Jankpur is popular with different historical and \nrelifious events. It is one of the most holy places of hindus.  You can get a chance to explore\n maithili culture and traditions by visiting there.",font=("Avenir",17))
    labeel8.place(x=30,y=660)
    labeel9=Label(frame_janaki,text="Day1: Kathmandu to Shree Ram Janaki Mandir (225 km) 7/8 hours. Overnight Stay. \nDay2:     Puja and full day sightseeing. Overnight Stay                      \nDay3: Drive back to Kathmandu by vehicles-7/8 hours.     ",font=("Avenir",17))
    labeel9.place(x=850,y=660)
    
pashupatinath() 

def durbar():
    global frame_janaki

    frame_janaki=Frame(root,width=1400,height=1200)
    frame_janaki.place(x=0,y=35)
    # label1=Label(frame_janaki,text="this is the good adventerous places of Nepal")
    # label1.place(x=100,y=500)
    button_booking=Button(frame_janaki,text="Book Your tour ",font=40,fg="green",command=booking)
    button_booking.configure(width=10,height=2)

    button_booking.place(x=320,y=760)
    image=Image.open("everest1.jpg")
    resized_image=image.resize((700,500))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_janaki,image=converted)
    label.image=converted
    label.place(x=0,y=0)
    image=Image.open("everest1.jpg")
    resized_image=image.resize((700,500))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_janaki,image=converted)
    label.image=converted
    label.place(x=700,y=0)
    
    laabel=Label(frame_janaki,text="Tour to Janakpur(Temple of janak)",font=("calibri",24,"bold"))
    laabel.place(x=30,y=510)
    laabela=Label(frame_janaki,text="From kathmandu to Dhanusha",font=("Avenir",24,"bold"),fg="green")
    laabela.place(x=470,y=510)
    # frame_duration=Frame(frame_janaki,width=190,height=95)
    # frame_duration.place(x=30,y=550)
    labeel1=Label(frame_janaki,text="Duration\n3 days",font=("Avenir",18,"bold"),fg="grey")
    labeel1.place(x=30,y=560)
    labeel2=Label(frame_janaki,text="Tour languages\nEnglish  Nepali",font=("Avenir",18,"bold"),fg="grey")
    labeel2.place(x=220,y=560)
    labeel3=Label(frame_janaki,text="Age Group \nAll age group",font=("Avenir",18,"bold"),fg="grey")
    labeel3.place(x=430,y=560)
    labeel4=Label(frame_janaki,text="Services and Facilities\n\t\tIncluded:Food, Acommodation,Travel expense\n\t\tNot included Personal expense\t medical expense",font=("Avenir",18,"bold"),fg="grey")
    labeel4.place(x=800,y=560)
    labeel5=Label(frame_janaki,text="Group size\n1-30",font=("Avenir",18,"bold"),fg="grey")
    labeel5.place(x=590,y=560)
    labeel6=Label(frame_janaki,text="District\nSolukhumbu",font=("Avenir",18,"bold"),fg="grey")
    labeel6.place(x=750,y=560)

    laabel7=Label(frame_janaki,text=" Tour Overview",font=("calibri",24,"bold"))
    laabel7.place(x=30,y=630)
    labeel8=Label(frame_janaki,text=" Janakpur dham is a tour of historical sites at janakpur ,birthplace of sita. All the hindu people\n worshipped this place as a great ceremony in chhath. Jankpur is popular with different historical and \nrelifious events. It is one of the most holy places of hindus.  You can get a chance to explore\n maithili culture and traditions by visiting there.",font=("Avenir",17))
    labeel8.place(x=30,y=660)
    labeel9=Label(frame_janaki,text="Day1: Kathmandu to Shree Ram Janaki Mandir (225 km) 7/8 hours. Overnight Stay. \nDay2:     Puja and full day sightseeing. Overnight Stay                      \nDay3: Drive back to Kathmandu by vehicles-7/8 hours.     ",font=("Avenir",17))
    labeel9.place(x=850,y=660)
    
durbar() 

def muktinath():
    global frame_janaki

    frame_janaki=Frame(root,width=1400,height=1200)
    frame_janaki.place(x=0,y=35)
    # label1=Label(frame_janaki,text="this is the good adventerous places of Nepal")
    # label1.place(x=100,y=500)
    button_booking=Button(frame_janaki,text="Book Your tour ",font=40,fg="green",command=booking)
    button_booking.configure(width=10,height=2)

    button_booking.place(x=320,y=760)
    image=Image.open("everest1.jpg")
    resized_image=image.resize((700,500))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_janaki,image=converted)
    label.image=converted
    label.place(x=0,y=0)
    image=Image.open("everest1.jpg")
    resized_image=image.resize((700,500))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_janaki,image=converted)
    label.image=converted
    label.place(x=700,y=0)
    
    laabel=Label(frame_janaki,text="Tour to muktinath(Temple of janak)",font=("calibri",24,"bold"))
    laabel.place(x=30,y=510)
    laabela=Label(frame_janaki,text="From kathmandu to Dhanusha",font=("Avenir",24,"bold"),fg="green")
    laabela.place(x=470,y=510)
    # frame_duration=Frame(frame_janaki,width=190,height=95)
    # frame_duration.place(x=30,y=550)
    labeel1=Label(frame_janaki,text="Duration\n3 days",font=("Avenir",18,"bold"),fg="grey")
    labeel1.place(x=30,y=560)
    labeel2=Label(frame_janaki,text="Tour languages\nEnglish  Nepali",font=("Avenir",18,"bold"),fg="grey")
    labeel2.place(x=220,y=560)
    labeel3=Label(frame_janaki,text="Age Group \nAll age group",font=("Avenir",18,"bold"),fg="grey")
    labeel3.place(x=430,y=560)
    labeel4=Label(frame_janaki,text="Services and Facilities\n\t\tIncluded:Food, Acommodation,Travel expense\n\t\tNot included Personal expense\t medical expense",font=("Avenir",18,"bold"),fg="grey")
    labeel4.place(x=800,y=560)
    labeel5=Label(frame_janaki,text="Group size\n1-30",font=("Avenir",18,"bold"),fg="grey")
    labeel5.place(x=590,y=560)
    labeel6=Label(frame_janaki,text="District\nSolukhumbu",font=("Avenir",18,"bold"),fg="grey")
    labeel6.place(x=750,y=560)

    laabel7=Label(frame_janaki,text=" Tour Overview",font=("calibri",24,"bold"))
    laabel7.place(x=30,y=630)
    labeel8=Label(frame_janaki,text=" muktinath dham is a tour of historical sites at muktinath ,birthplace of sita. All the hindu people\n worshipped this place as a great ceremony in chhath. Jankpur is popular with different historical and \nrelifious events. It is one of the most holy places of hindus.  You can get a chance to explore\n maithili culture and traditions by visiting there.",font=("Avenir",17))
    labeel8.place(x=30,y=660)
    labeel9=Label(frame_janaki,text="Day1: Kathmandu to Shree Ram Janaki Mandir (225 km) 7/8 hours. Overnight Stay. \nDay2:     Puja and full day sightseeing. Overnight Stay                      \nDay3: Drive back to Kathmandu by vehicles-7/8 hours.     ",font=("Avenir",17))
    labeel9.place(x=850,y=660)
    
muktinath() 

def gorkha():
    global frame_janaki

    frame_janaki=Frame(root,width=1400,height=1200)
    frame_janaki.place(x=0,y=35)
    # label1=Label(frame_janaki,text="this is the good adventerous places of Nepal")
    # label1.place(x=100,y=500)
    button_booking=Button(frame_janaki,text="Book Your tour ",font=40,fg="green",command=booking)
    button_booking.configure(width=10,height=2)

    button_booking.place(x=320,y=760)
    image=Image.open("everest1.jpg")
    resized_image=image.resize((700,500))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_janaki,image=converted)
    label.image=converted
    label.place(x=0,y=0)
    image=Image.open("everest1.jpg")
    resized_image=image.resize((700,500))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_janaki,image=converted)
    label.image=converted
    label.place(x=700,y=0)
    
    laabel=Label(frame_janaki,text="Tour to gorkha(Temple of janak)",font=("calibri",24,"bold"))
    laabel.place(x=30,y=510)
    laabela=Label(frame_janaki,text="From kathmandu to Dhanusha",font=("Avenir",24,"bold"),fg="green")
    laabela.place(x=470,y=510)
    # frame_duration=Frame(frame_janaki,width=190,height=95)
    # frame_duration.place(x=30,y=550)
    labeel1=Label(frame_janaki,text="Duration\n3 days",font=("Avenir",18,"bold"),fg="grey")
    labeel1.place(x=30,y=560)
    labeel2=Label(frame_janaki,text="Tour languages\nEnglish  Nepali",font=("Avenir",18,"bold"),fg="grey")
    labeel2.place(x=220,y=560)
    labeel3=Label(frame_janaki,text="Age Group \nAll age group",font=("Avenir",18,"bold"),fg="grey")
    labeel3.place(x=430,y=560)
    labeel4=Label(frame_janaki,text="Services and Facilities\n\t\tIncluded:Food, Acommodation,Travel expense\n\t\tNot included Personal expense\t medical expense",font=("Avenir",18,"bold"),fg="grey")
    labeel4.place(x=800,y=560)
    labeel5=Label(frame_janaki,text="Group size\n1-30",font=("Avenir",18,"bold"),fg="grey")
    labeel5.place(x=590,y=560)
    labeel6=Label(frame_janaki,text="District\nSolukhumbu",font=("Avenir",18,"bold"),fg="grey")
    labeel6.place(x=750,y=560)

    laabel7=Label(frame_janaki,text=" Tour Overview",font=("calibri",24,"bold"))
    laabel7.place(x=30,y=630)
    labeel8=Label(frame_janaki,text=" gorkha dham is a tour of historical sites at gorkha ,birthplace of sita. All the hindu people\n worshipped this place as a great ceremony in chhath. Jankpur is popular with different historical and \nrelifious events. It is one of the most holy places of hindus.  You can get a chance to explore\n maithili culture and traditions by visiting there.",font=("Avenir",17))
    labeel8.place(x=30,y=660)
    labeel9=Label(frame_janaki,text="Day1: Kathmandu to Shree Ram Janaki Mandir (225 km) 7/8 hours. Overnight Stay. \nDay2:     Puja and full day sightseeing. Overnight Stay                      \nDay3: Drive back to Kathmandu by vehicles-7/8 hours.     ",font=("Avenir",17))
    labeel9.place(x=850,y=660)
    
gorkha() 

def dhorpatan():
    global frame_janaki

    frame_janaki=Frame(root,width=1400,height=1200)
    frame_janaki.place(x=0,y=35)
    # label1=Label(frame_janaki,text="this is the good adventerous places of Nepal")
    # label1.place(x=100,y=500)
    button_booking=Button(frame_janaki,text="Book Your tour ",font=40,fg="green",command=booking)
    button_booking.configure(width=10,height=2)

    button_booking.place(x=320,y=760)
    image=Image.open("everest1.jpg")
    resized_image=image.resize((700,500))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_janaki,image=converted)
    label.image=converted
    label.place(x=0,y=0)
    image=Image.open("everest1.jpg")
    resized_image=image.resize((700,500))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_janaki,image=converted)
    label.image=converted
    label.place(x=700,y=0)
    
    laabel=Label(frame_janaki,text="Tour to dhorpatan(Temple of janak)",font=("calibri",24,"bold"))
    laabel.place(x=30,y=510)
    laabela=Label(frame_janaki,text="From kathmandu to Dhanusha",font=("Avenir",24,"bold"),fg="green")
    laabela.place(x=470,y=510)
    # frame_duration=Frame(frame_janaki,width=190,height=95)
    # frame_duration.place(x=30,y=550)
    labeel1=Label(frame_janaki,text="Duration\n3 days",font=("Avenir",18,"bold"),fg="grey")
    labeel1.place(x=30,y=560)
    labeel2=Label(frame_janaki,text="Tour languages\nEnglish  Nepali",font=("Avenir",18,"bold"),fg="grey")
    labeel2.place(x=220,y=560)
    labeel3=Label(frame_janaki,text="Age Group \nAll age group",font=("Avenir",18,"bold"),fg="grey")
    labeel3.place(x=430,y=560)
    labeel4=Label(frame_janaki,text="Services and Facilities\n\t\tIncluded:Food, Acommodation,Travel expense\n\t\tNot included Personal expense\t medical expense",font=("Avenir",18,"bold"),fg="grey")
    labeel4.place(x=800,y=560)
    labeel5=Label(frame_janaki,text="Group size\n1-30",font=("Avenir",18,"bold"),fg="grey")
    labeel5.place(x=590,y=560)
    labeel6=Label(frame_janaki,text="District\nSolukhumbu",font=("Avenir",18,"bold"),fg="grey")
    labeel6.place(x=750,y=560)

    laabel7=Label(frame_janaki,text=" Tour Overview",font=("calibri",24,"bold"))
    laabel7.place(x=30,y=630)
    labeel8=Label(frame_janaki,text=" dhorpatan dham is a tour of historical sites at dhorpatan ,birthplace of sita. All the hindu people\n worshipped this place as a great ceremony in chhath. Jankpur is popular with different historical and \nrelifious events. It is one of the most holy places of hindus.  You can get a chance to explore\n maithili culture and traditions by visiting there.",font=("Avenir",17))
    labeel8.place(x=30,y=660)
    labeel9=Label(frame_janaki,text="Day1: Kathmandu to Shree Ram Janaki Mandir (225 km) 7/8 hours. Overnight Stay. \nDay2:     Puja and full day sightseeing. Overnight Stay                      \nDay3: Drive back to Kathmandu by vehicles-7/8 hours.     ",font=("Avenir",17))
    labeel9.place(x=850,y=660)
    
dhorpatan() 

def lumbini():
    global frame_janaki

    frame_janaki=Frame(root,width=1400,height=1200)
    frame_janaki.place(x=0,y=35)
    # label1=Label(frame_janaki,text="this is the good adventerous places of Nepal")
    # label1.place(x=100,y=500)
    button_booking=Button(frame_janaki,text="Book Your tour ",font=40,fg="green",command=booking)
    button_booking.configure(width=10,height=2)

    button_booking.place(x=320,y=760)
    image=Image.open("everest1.jpg")
    resized_image=image.resize((700,500))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_janaki,image=converted)
    label.image=converted
    label.place(x=0,y=0)
    image=Image.open("everest1.jpg")
    resized_image=image.resize((700,500))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_janaki,image=converted)
    label.image=converted
    label.place(x=700,y=0)
    
    laabel=Label(frame_janaki,text="Tour to lumbini(Temple of janak)",font=("calibri",24,"bold"))
    laabel.place(x=30,y=510)
    laabela=Label(frame_janaki,text="From kathmandu to Dhanusha",font=("Avenir",24,"bold"),fg="green")
    laabela.place(x=470,y=510)
    # frame_duration=Frame(frame_janaki,width=190,height=95)
    # frame_duration.place(x=30,y=550)
    labeel1=Label(frame_janaki,text="Duration\n3 days",font=("Avenir",18,"bold"),fg="grey")
    labeel1.place(x=30,y=560)
    labeel2=Label(frame_janaki,text="Tour languages\nEnglish  Nepali",font=("Avenir",18,"bold"),fg="grey")
    labeel2.place(x=220,y=560)
    labeel3=Label(frame_janaki,text="Age Group \nAll age group",font=("Avenir",18,"bold"),fg="grey")
    labeel3.place(x=430,y=560)
    labeel4=Label(frame_janaki,text="Services and Facilities\n\t\tIncluded:Food, Acommodation,Travel expense\n\t\tNot included Personal expense\t medical expense",font=("Avenir",18,"bold"),fg="grey")
    labeel4.place(x=800,y=560)
    labeel5=Label(frame_janaki,text="Group size\n1-30",font=("Avenir",18,"bold"),fg="grey")
    labeel5.place(x=590,y=560)
    labeel6=Label(frame_janaki,text="District\nSolukhumbu",font=("Avenir",18,"bold"),fg="grey")
    labeel6.place(x=750,y=560)

    laabel7=Label(frame_janaki,text=" Tour Overview",font=("calibri",24,"bold"))
    laabel7.place(x=30,y=630)
    labeel8=Label(frame_janaki,text=" lumbini dham is a tour of historical sites at lumbini ,birthplace of sita. All the hindu people\n worshipped this place as a great ceremony in chhath. Jankpur is popular with different historical and \nrelifious events. It is one of the most holy places of hindus.  You can get a chance to explore\n maithili culture and traditions by visiting there.",font=("Avenir",17))
    labeel8.place(x=30,y=660)
    labeel9=Label(frame_janaki,text="Day1: Kathmandu to Shree Ram Janaki Mandir (225 km) 7/8 hours. Overnight Stay. \nDay2:     Puja and full day sightseeing. Overnight Stay                      \nDay3: Drive back to Kathmandu by vehicles-7/8 hours.     ",font=("Avenir",17))
    labeel9.place(x=850,y=660)
    
lumbini() 

def kanjiroba():
    global frame_janaki

    frame_janaki=Frame(root,width=1400,height=1200)
    frame_janaki.place(x=0,y=35)
    # label1=Label(frame_janaki,text="this is the good adventerous places of Nepal")
    # label1.place(x=100,y=500)
    button_booking=Button(frame_janaki,text="Book Your tour ",font=40,fg="green",command=booking)
    button_booking.configure(width=10,height=2)

    button_booking.place(x=320,y=760)
    image=Image.open("everest1.jpg")
    resized_image=image.resize((700,500))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_janaki,image=converted)
    label.image=converted
    label.place(x=0,y=0)
    image=Image.open("everest1.jpg")
    resized_image=image.resize((700,500))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_janaki,image=converted)
    label.image=converted
    label.place(x=700,y=0)
    
    laabel=Label(frame_janaki,text="Tour to kanjiroba(Temple of janak)",font=("calibri",24,"bold"))
    laabel.place(x=30,y=510)
    laabela=Label(frame_janaki,text="From kathmandu to Dhanusha",font=("Avenir",24,"bold"),fg="green")
    laabela.place(x=470,y=510)
    # frame_duration=Frame(frame_janaki,width=190,height=95)
    # frame_duration.place(x=30,y=550)
    labeel1=Label(frame_janaki,text="Duration\n3 days",font=("Avenir",18,"bold"),fg="grey")
    labeel1.place(x=30,y=560)
    labeel2=Label(frame_janaki,text="Tour languages\nEnglish  Nepali",font=("Avenir",18,"bold"),fg="grey")
    labeel2.place(x=220,y=560)
    labeel3=Label(frame_janaki,text="Age Group \nAll age group",font=("Avenir",18,"bold"),fg="grey")
    labeel3.place(x=430,y=560)
    labeel4=Label(frame_janaki,text="Services and Facilities\n\t\tIncluded:Food, Acommodation,Travel expense\n\t\tNot included Personal expense\t medical expense",font=("Avenir",18,"bold"),fg="grey")
    labeel4.place(x=800,y=560)
    labeel5=Label(frame_janaki,text="Group size\n1-30",font=("Avenir",18,"bold"),fg="grey")
    labeel5.place(x=590,y=560)
    labeel6=Label(frame_janaki,text="District\nSolukhumbu",font=("Avenir",18,"bold"),fg="grey")
    labeel6.place(x=750,y=560)

    laabel7=Label(frame_janaki,text=" Tour Overview",font=("calibri",24,"bold"))
    laabel7.place(x=30,y=630)
    labeel8=Label(frame_janaki,text=" kanjiroba dham is a tour of historical sites at kanjiroba ,birthplace of sita. All the hindu people\n worshipped this place as a great ceremony in chhath. Jankpur is popular with different historical and \nrelifious events. It is one of the most holy places of hindus.  You can get a chance to explore\n maithili culture and traditions by visiting there.",font=("Avenir",17))
    labeel8.place(x=30,y=660)
    labeel9=Label(frame_janaki,text="Day1: Kathmandu to Shree Ram Janaki Mandir (225 km) 7/8 hours. Overnight Stay. \nDay2:     Puja and full day sightseeing. Overnight Stay                      \nDay3: Drive back to Kathmandu by vehicles-7/8 hours.     ",font=("Avenir",17))
    labeel9.place(x=850,y=660)
    
kanjiroba() 

def rara():
    global frame_janaki

    frame_janaki=Frame(root,width=1400,height=1200)
    frame_janaki.place(x=0,y=35)
    # label1=Label(frame_janaki,text="this is the good adventerous places of Nepal")
    # label1.place(x=100,y=500)
    button_booking=Button(frame_janaki,text="Book Your tour ",font=40,fg="green",command=booking)
    button_booking.configure(width=10,height=2)

    button_booking.place(x=320,y=760)
    image=Image.open("everest1.jpg")
    resized_image=image.resize((700,500))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_janaki,image=converted)
    label.image=converted
    label.place(x=0,y=0)
    image=Image.open("everest1.jpg")
    resized_image=image.resize((700,500))
    converted =ImageTk.PhotoImage(resized_image)
    label= Label(frame_janaki,image=converted)
    label.image=converted
    label.place(x=700,y=0)
    
    laabel=Label(frame_janaki,text="Tour to rara(Temple of janak)",font=("calibri",24,"bold"))
    laabel.place(x=30,y=510)
    laabela=Label(frame_janaki,text="From kathmandu to Dhanusha",font=("Avenir",24,"bold"),fg="green")
    laabela.place(x=470,y=510)
    # frame_duration=Frame(frame_janaki,width=190,height=95)
    # frame_duration.place(x=30,y=550)
    labeel1=Label(frame_janaki,text="Duration\n3 days",font=("Avenir",18,"bold"),fg="grey")
    labeel1.place(x=30,y=560)
    labeel2=Label(frame_janaki,text="Tour languages\nEnglish  Nepali",font=("Avenir",18,"bold"),fg="grey")
    labeel2.place(x=220,y=560)
    labeel3=Label(frame_janaki,text="Age Group \nAll age group",font=("Avenir",18,"bold"),fg="grey")
    labeel3.place(x=430,y=560)
    labeel4=Label(frame_janaki,text="Services and Facilities\n\t\tIncluded:Food, Acommodation,Travel expense\n\t\tNot included Personal expense\t medical expense",font=("Avenir",18,"bold"),fg="grey")
    labeel4.place(x=800,y=560)
    labeel5=Label(frame_janaki,text="Group size\n1-30",font=("Avenir",18,"bold"),fg="grey")
    labeel5.place(x=590,y=560)
    labeel6=Label(frame_janaki,text="District\nSolukhumbu",font=("Avenir",18,"bold"),fg="grey")
    labeel6.place(x=750,y=560)

    laabel7=Label(frame_janaki,text=" Tour Overview",font=("calibri",24,"bold"))
    laabel7.place(x=30,y=630)
    labeel8=Label(frame_janaki,text=" rara dham is a tour of historical sites at rara ,birthplace of sita. All the hindu people\n worshipped this place as a great ceremony in chhath. Jankpur is popular with different historical and \nrelifious events. It is one of the most holy places of hindus.  You can get a chance to explore\n maithili culture and traditions by visiting there.",font=("Avenir",17))
    labeel8.place(x=30,y=660)
    labeel9=Label(frame_janaki,text="Day1: Kathmandu to Shree Ram Janaki Mandir (225 km) 7/8 hours. Overnight Stay. \nDay2:     Puja and full day sightseeing. Overnight Stay                      \nDay3: Drive back to Kathmandu by vehicles-7/8 hours.     ",font=("Avenir",17))
    labeel9.place(x=850,y=660)
    
rara() 
     




# root = None  # Initiae frame1 variable
# clickcount=0
def frame_destination():
    
    # if frame_adventure is not None:
    #     frame_adventure.place_forget()
    # # if a2 is not NONE:
    # #     a2.place_forget()
    
        
    # if  frame1 is None:
        frame1 = Frame(root, width=1100, height=190, bg="grey")
        frame1.place(x=100, y=35)
        label_pr1=Label(frame1,text="Province1",font=("Arial",22,"bold"),fg="#81D8D0",bg="white")
        label_pr1.place(x=10, y=20)
        btn1=Button(frame1,text="Everest Base camp ",font=("Arial",15,"bold"),bg="white",command=everest1)
        btn1.place(x=10,y=65)
        
        btn2=Button(frame1,text="Ilam",font=("Arial",15,"bold"),bg="white",command=Ilam)
        btn2.place(x=10,y=110)
        # btn3=Button(frame1,text="Taplejung",font=("Arial",15,"bold"),bg="white")
        # btn3.place(x=10,y=160)

        label_pr2=Label(frame1,text="Province2",font=("Arial",22,"bold"),fg="#81D8D0")
        label_pr2.place(x=180,y=20)
        btn4=Button(frame1,text="Janaki Temple",font=("Arial",15,"bold"),bg="white",command=janakpur)
        btn4.place(x=180,y=65)
        btn5=Button(frame1,text="Koshitappu WR",font=("Arial",15,"bold"),bg="white",command=koshi)
        btn5.place(x=180,y=110)
        # btn6=Button(frame1,text="Birgunj border",font=("Arial",15,"bold"),bg="white")
        # btn6.place(x=180,y=160)


        label_pr3=Label(frame1,text="Province3",font=("Arial",22,"bold"),fg="#81D8D0")
        label_pr3.place(x=350,y=20)
        btn7=Button(frame1,text="Pashupatinath ",font=("Arial",15,"bold"),bg="white",command=pashupatinath)
        btn7.place(x=350,y=65)
        btn8=Button(frame1,text="Kathmandu DS",font=("Arial",15,"bold"),bg="white",command=durbar)
        btn8.place(x=350,y=110)
        # btn9=Button(frame1,text="Bhaktapur DS",font=("Arial",15,"bold"),bg="white")
        # btn9.place(x=350,y=160)


        label_pr4=Label(frame1,text="Province4",font=("Arial",22,"bold"),fg="#81D8D0")
        label_pr4.place(x=500,y=20)
        btn10=Button(frame1,text="Muktinath Temple",font=("Arial",15,"bold"),bg="white",command=muktinath)
        btn10.place(x=500,y=65)
        btn11=Button(frame1,text="GOrkha durbar",font=("Arial",15,"bold"),bg="white",command=gorkha)
        btn11.place(x=500,y=110)
        # btn12=Button(frame1,text="Pokhara city",font=("Arial",15,"bold"),bg="white")
        # btn12.place(x=500,y=160)



        label_pr5=Label(frame1,text="Province5",font=("Arial",22,"bold"),fg="#81D8D0")
        label_pr5.place(x=650,y=20)


        btn13=Button(frame1,text="Dhorpatan HR",font=("Arial",15,"bold"),bg="white",command=dhorpatan)
        btn13.place(x=650,y=65)
        btn14=Button(frame1,text="Lumbini",font=("Arial",15,"bold"),bg="white",command=lumbini)
        btn14.place(x=650,y=110)
        # btn15=Button(frame1,text="Bardiya NP",font=("Arial",15,"bold"),bg="white")
        # btn15.place(x=650,y=160)

        label_pr6=Label(frame1,text="Province6",font=("Arial",22,"bold"),fg="#81D8D0")
        label_pr6.place(x=800,y=20)


        btn16=Button(frame1,text="Kanjiroba himal ",font=("Arial",15,"bold"),bg="white",command=kanjiroba)
        btn16.place(x=800,y=65)
        btn17=Button(frame1,text="Rara lake",font=("Arial",15,"bold"),bg="white",command=rara)
        btn17.place(x=800,y=110)
        # btn18=Button(frame1,text="Sheyphoksundo ",font=("Arial",15,"bold"),bg="white")
        # btn18.place(x=800,y=160)

        label_pr7=Label(frame1,text="Province7",font=("Arial",22,"bold"),fg="#81D8D0")
        label_pr7.place(x=930,y=20)

        btn19=Button(frame1,text="Baglung hanging bridge",font=("Arial",15,"bold"),bg="white")
        btn19.place(x=930,y=65)
        btn20=Button(frame1,text="Khaptad NP",font=("Arial",15,"bold"),bg="white")
        btn20.place(x=930,y=110)
        # btn21=Button(frame1,text="Api mountain ",font=("Arial",15,"bold"),bg="white")
        # btn21.place(x=930,y=160)
        






destination = Button(root, text="Destination",font=("Arial",18,"bold"),fg="blue", command=frame_destination)
destination.place(x=560, y=5)

# click_count=0
# frame_adventure=None
def pokhara():
     frame_pokhara1=Frame(root,width=1000,height=1200)
     frame_pokhara1.place(x=0,y=35)
     image=Image.open("everest1.jpg")
     resized_image=image.resize((1000,600))
     converted =ImageTk.PhotoImage(resized_image)
     label= Label(frame_pokhara1,image=converted)
     label.image=converted
     label.place(x=0,y=0)
    
     image=Image.open("everest1.jpg")
     resized_image=image.resize((500,230))
     converted =ImageTk.PhotoImage(resized_image)
     label= Label(frame_pokhara1,image=converted)
     label.image=converted
     label.place(x=0,y=600)
     image=Image.open("everest1.jpg")
     resized_image=image.resize((500,230))
     converted =ImageTk.PhotoImage(resized_image)
     label= Label(frame_pokhara1,image=converted)
     label.image=converted
     label.place(x=500,y=600)
     frame_pokhara_overview=Frame(root,width=400,height=1200)
     frame_pokhara_overview.place(x=1000,y=35)

     

def create_adventure():
    
       if frame1  is not NONE:
        frame1.place_forget()
    #    if a2 is not NONE:
    #     a2.place_forget()
    
        global frame_adventure
    # if frame_adventure is None:
        frame_adventure = Frame(root, width=700)
        frame_adventure.place(x=400, y=40, height=130)

        paragliding = Label(frame_adventure, text="Paragliding", font=("arial", 20, "bold"), fg="#00FF00")
        paragliding.place(x=10, y=10)
        pokhara_but = Button(frame_adventure, text="Pokhara Sarangkot", font=18,command=pokhara)
        pokhara_but.place(x=12, y=50)
        mygdi_but = Button(frame_adventure, text="Myagdi", font=18)
        mygdi_but.place(x=12, y=80)

        hiking = Label(frame_adventure, text="Trekking", font=("arial", 20, "bold"), fg="#00FF00")
        hiking.place(x=160, y=10)
        mardi_but = Button(frame_adventure, text="Mardi Himal", font=18)
        mardi_but.place(x=162, y=50)
        nagarkot_but = Button(frame_adventure, text="Nagarkot", font=18)
        nagarkot_but.place(x=162, y=80)

        rafting = Label(frame_adventure, text="Rafting", font=("arial", 20, "bold"), fg="#00FF00")
        rafting.place(x=265, y=10)
        koshi_rafting_but = Button(frame_adventure, text="Koshi Rafting", font=18)
        koshi_rafting_but.place(x=262, y=50)
        karnali_rafting_but = Button(frame_adventure, text="Karnali Rafting", font=18)
        karnali_rafting_but.place(x=262, y=80)

        bunjee_jumping = Label(frame_adventure, text="Bunjee Jumping", font=("arial", 20, "bold"), fg="#00FF00")
        bunjee_jumping.place(x=360, y=10)
        myagdi_but = Button(frame_adventure, text="Myagdi Bunjee", font=18)
        myagdi_but.place(x=378, y=50)
        pyuthan_but = Button(frame_adventure, text="Pyuthan Bunjee", font=18)
        pyuthan_but.place(x=378, y=80)

        mountaineering = Label(frame_adventure, text="Mountaineering", font=("arial", 20, "bold"), fg="#00FF00")
        mountaineering.place(x=540, y=10)
        mount_everest_but = Button(frame_adventure, text="Mount Everest", font=18)
        mount_everest_but.place(x=542, y=50)
        annapurna_but = Button(frame_adventure, text="Annapurna", font=18)
        annapurna_but.place(x=542, y=80)
#     else:
#         frame_adventure.place_forget()
#         frame_adventure = None

# def button_click():
 
#     global clickcount
#     clickcount += 1
#     if clickcount == 1:
#         create_adventure()
#         clickcount = 0

# frame1 = Frame(root, width=1400, height=35, bg="#158aff", relief=SUNKEN)
# frame1.place(x=0, y=0)

adventure_type = Button(root, text="Adventure Type", font=("calibri", 20, "bold"), fg="blue", command=create_adventure)
adventure_type.place(x=730, y=5)
# clickcount=0
# a2=None
def create_help():
        if frame_adventure is not NONE:
              frame_adventure.place_forget()
        
        global a2
    # if a2 is None:
        
        a2=Frame(root,width=500)
        a2.place(x=800,y=40,height=130)
        text1=Text(a2,font=24)
        text1.place(x=0,y=0)
        qsn1=Label(a2,text="Where are you from?",font=("Arial",16,"bold"))
        qsn1.place(x=10,y=5)
        entry_qsn1=Entry(a2)
        entry_qsn1.place(x=10,y=20)
#     else:
#         a2.place_forget()
#         a2=NONE
# def but_help():

#     global clickcount
#     clickcount+=1
#     if clickcount==1:
#         create_help()
#         clickcount=0
frame_account=Frame()
def signup():
     root.destroy()
     import signup 

def login1():
     root1=Toplevel(root)
     
     
     root1.title("login")



# def login1():

#      frame_log=Frame(frame_account,width=400,height=300)
#      frame_log.place(x=1000,y=45)
# frame_account=Frame()
def accounts():
     global frame_account
     frame_account=Frame(root,width=90,height=70)
     frame_account.place(x=1300,y=45)
     signup_btn=Button(frame_account,text="Sign up",font=("arial",18,"bold"),command=signup)
     signup_btn.place(x=0,y=0)
     login_btn=Button(frame_account,text="login",font=("arial",18,"bold"),command=login1)
     login_btn.place(x=0,y=45)
frame_account.pack()
accounts()

# def login1():

#      frame_log=Frame(frame_account,width=400,height=300)
#      frame_log.place(x=1000,y=45)
# login1()

home=Button(root,text="Home",font=("calibri",20,"bold"),fg="blue",bg="#1581ff",command=home,bd=0).place(x=440,y=5)       

help=Button(root,text="Help and Feedback",font=("calibri",20,"bold"),fg="blue",bg="blue",command=create_help).place(x=930,y=5)


contacts=Button(root,text="Contacts",font=("calibri",20,"bold"),fg="blue")
contacts.place(x=1160,y=5)

accounts=Button(root,text="Accounts",font=("calibri",20,"bold"),fg="blue",command=accounts)
accounts.place(x=1300,y=5)



frame2=Frame(root,width=1400,height=650,bg="green")
frame2.place(x=0,y=35)

frame_topdestinations=Frame(root,width=1400,height=50,bg="white")
frame_topdestinations.place(x=0,y=580)
label_top=Label(frame_topdestinations,text="Top Destinations",font=("Arial",30,"bold"))
label_top.place(x=500,y=0)

frame_bottom=Frame(root,width=1400,height=250,bg='white')
frame_bottom.place(x=0,y=620)



photo=Image.open("img1.jpg")
resized_photo=photo.resize((1400,600))
converted =ImageTk.PhotoImage(resized_photo)
label= Label(frame2,image=converted)
label.place(x=0,y=0)

label2=Label(root,text="Enjoy your journey with full of ",font=("Arial",30,"bold"),fg="black",bg="blue")
label2.place(x=400,y=50)
label2=Label(root,text=" happiness and better services",font=("Arial",30,"bold"),fg="black",bg="blue")
label2.place(x=400,y=100)

entry1=Entry(frame2,width=80,bg="white",relief=SUNKEN)
entry1.place(x=300,y=300,height=50)

frame3=Frame(frame_bottom,width=300,height=250)
frame3.place(x=0,y=0)
photo=Image.open("patan.png")
resized_photo1=photo.resize((300,150))
converted1=ImageTk.PhotoImage(resized_photo1)
label=Label(frame3,image=converted1)
label.place(x=0,y=0)

frame4=Frame(frame_bottom,width=300,height=250)
frame4.place(x=350,y=0)
photo=Image.open("ktm.png")
resized_photo2=photo.resize((300,150))
converted2=ImageTk.PhotoImage(resized_photo2)
label=Label(frame4,image=converted2)
label.place(x=0,y=0)

frame5=Frame(frame_bottom,width=300,height=250)
frame5.place(x=700,y=0)
photo=Image.open("pashupatinath.png")
resized_photo3=photo.resize((300,150))
converted3=ImageTk.PhotoImage(resized_photo3)
label=Label(frame5,image=converted3)
label.place(x=0,y=0)

frame6=Frame(frame_bottom,width=300,height=250,bg="white",relief=SUNKEN)
frame6.place(x=1050,y=0)
photo=Image.open("pokhara.png")
resized_photo4=photo.resize((300,150))
converted4=ImageTk.PhotoImage(resized_photo4)
label=Label(frame6,image=converted4)
label.place(x=0,y=0)

# frame7=Frame(frame_bottom,width=200,height=250)
# frame7.place(x=1200,y=635)
# photo=Image.open("rafting.png")
# resized_photo5=photo.resize((200,150))
# converted5=ImageTk.PhotoImage(resized_photo5)
# label=Label(frame7,image=converted5)
# label.place(x=0,y=0)





   
   

root.mainloop()
