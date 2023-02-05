from tkinter import filedialog as fd
from tkinter import messagebox
from winsound import Beep
from tkinter import ttk
from tkinter import *
from PIL import Image
import requests
import os


# Start/ Back End--------------------------
try:
    try:
        import PIL
        try:
            os.remove(os.getcwd()+"\\seven.txt")
        except:
            pass
    except:
        os.system("pip install pillow")
    #
    src = ''
    dst = ''
    class src_path:
            def src():
                    source = (fd.askdirectory(title="مبدا"))
                    global source_val   # access
                    source_val = source # value
                    if source is '':
                            pass
                    else:
                            frame_text1["text"]=str("انتخاب شده")
                            frame_text1["bg"]=("light green")
                            text1["text"]=str(source)
                            print(frame_text1["text"])
            def start0():
                    src_path.src()
                    cwd = os.getcwd()
                    file = open(str(cwd+"\\seven_1.txt"),"a")
                    file.writelines(source_val+"\n")
                    file.close()
                    src = source_val ### #
            def exit_msg():
                
                exit_box = messagebox.askyesno("مطمعن هستید","ایا خارج میشوید")
                if exit_box is True:
                    try:
                        cwd = str(os.getcwd())+"\\seven_1.txt"
                        os.remove(cwd)
                        root.quit()
                    except:
                        root.quit()
                else:
                    pass

    class dst_path:
            def dst():
                    destin = (fd.askdirectory(title="مقصد"))
                    global destin_val   # access
                    destin_val = destin # value
                    if destin is '':
                            pass
                    else:
                            frame_text2["text"]=str("انتخاب شده")
                            frame_text2["bg"]=("light green")
                            text2["text"]=str(destin)
                            print(frame_text2["text"])
            def start1():
                    dst_path.dst()
                    cwd = os.getcwd()
                    file = open(str(cwd+"\\seven_2.txt"),"a")
                    file.writelines(destin_val+"\n")  
                    file.close()
                    dst = destin_val ### #
    # Start Program Processing
    def start_process():
        try:
            read_file = open(os.getcwd()+"\\seven_1.txt","r") # Create File Handler
            readable = read_file.read().split("\n") # Read The File
            #
            read_file1 = open(os.getcwd()+"\\seven_2.txt","r") # Create File Handler
            readable1 = read_file1.read().split("\n") # Read The File
            
            src = readable[0] # Source Address
            dst = readable1[0] # Destin Address
            #print("SRC is :: %s"%(src))
            #print("DST is :: %s"%(dst))

            try:
                    txt_path = src.split("/") 
                    src_path = "//".join(txt_path)
                    list_files = os.listdir(src_path)
                    print(src_path)
                    count = 0
                    mif = str(format_list.get()) # my image format2
                    print("image format is :: %s"%(mif))
                    try:
                        for files in (list_files):
                            src_file = src + "//" + files 
                            dst_file = dst + "//" + files.split(".")[0] + str("."+mif) 
                            #print("dst is :: %s"%(dst)) # # #
                            try:
                                img = Image.open(src_file)
                                img.save(dst_file, str(mif), save_all=True)
                                print(f"Count of File:{count} Name:{files} . .")
                                count += 1
                            except:
                                pass
                    except:  
                            messagebox.showinfo("ناتواني","تصوير نتوانست فرمت را پشتيباني کند")
                    print("[+] Finished !")
                    delete_seven = os.getcwd()+"\\seven_1.txt" and os.getcwd()+"\\seven_2.txt"
                    os.remove(delete_seven)
                    print("File Event Deleted !")
            
            except Exception as e:
                    print(files)
        except:
            messagebox.showerror("عجله کردید","فرمت یا فایل مبدا/مقصد پیدا نشد")
except:
    delete_seven = os.getcwd()+"\\seven_1.txt" and os.getcwd()+"\\seven_2.txt"
    os.remove(delete_seven)


# Back End--------------------------   /End
# -
# -
# Start/ Front End-------------------------
# New Window
root = Tk()
# Window Title
root.title("برنامه")
# Window resize
root.geometry("500x400")
# Window resizable false
root.resizable(False,False)
# Label For Welcome Text
welcome_label = Label(root,text="خوش امديد",font=("tahoma",10))
welcome_label.grid(row=0,column=0)
# Line Break : Space between Label and Button
space_label = Label(root,text="\n")
space_label.grid(row=1,column=0)
# Button1 for source click
button1 = Button(root,text="فايل مبدا",width=10,bg="light blue",command=src_path.start0)
button1.grid(row=2,column=0,padx=20)
# Button2 for destin click
button2 = Button(root,text="فايل مقصد",width=10,bg="light blue",command=dst_path.start1)
button2.grid(row=2,column=2,padx=10)
# Quit Button
qquit = Button(root,text="خروج",width=30,bg="light blue",command=src_path.exit_msg)
qquit.grid(row=2,column=3,padx=20)
# Line Break
space_label = Label(root,text="\n")
space_label.grid(row=3,column=0)
# Label To Show Message For ComboBox Widget
Label(root,text="فرمت دلخواه را انتخاب کنيد",fg="green").grid(row=4,column=3)
# Format type Variable
format_var = StringVar()
# List Of Format in Combobox
format_list = ttk.Combobox(root,width=30,textvariable=format_var)
# Set Values To list
format_list['values'] = (
    "JPG","GIF","WEBP","PNG",
    "BLP","BMP","DDS","DIB",
    "EPS","ICNS","ICO","IM",
    "JPEG","MSP","PCX","PPM",
    "SGI","SPIDER","TGA","TIFF",
    "XBM","CUR","DCX","FITS",
    "FLI","FLC","FPX","FTEX",
    "GBR","GD","IMT","MIC",
    "MCIDAS","IPTC","NAA","MPO",
    "PCD","PIXAR","PSD","SUN","WAL",
    "WMF","EMF","XPM","PALM","PDF",
    "GRIB","HDF5","MPEG"
)
format_list.grid(row=5,column=3)
format_list.current()
# Label Frame 1 
label_frame1 = LabelFrame(root,text="مبدا",width="100",height="100")
label_frame1.grid(row=6,column=0)
# Label into Frame 1
frame_text1 = Label(label_frame1,text="انتخاب نشده")
frame_text1.grid(row=6,column=0)
# Label Frame 2
label_frame2 = LabelFrame(root,text="مقصد",width="100",height="100")
label_frame2.grid(row=7,column=0)
# Label into Frame 2
frame_text2 = Label(label_frame2,text="انتخاب نشده")
frame_text2.grid(row=7,column=0)
# # # #
# Line Break 
space_label = Label(root,text="\n")
space_label.grid(row=8,column=0)
# Process Button
action = Button(root,text="پردازش",width=30,bg="light blue",command=start_process)
action.grid(row=9,column=3)
# Output for label frame 1
text1 = Label(root,text="مسير فايل مبدا",width="30",bg="black",fg="white")
text1.grid(row=6,column=3)
# Output for label frame 2
text2 = Label(root,text="مسير فايل مقصد",width="30",bg="black",fg="white")
text2.grid(row=7,column=3)
# Create Menu Bar
def about_us():
    messagebox.showinfo("درباره", "اين برنامه توسط محمدحسين شفيعي نوشته شده است")
def tk_version():
        messagebox.showinfo("نسخه","نسخه فعلی 3.7 ")
def tk_quit():
    try:
        Beep(2000,200)
        root.quit()
    except:
        root.quit()
def tk_help():
    messagebox.showinfo("راهنمای برنامه",'''
    سلام برنامه به شما کمک خواهد کرد تا فرمت های مختلف تصاویر را دلخواه به فرمت های دیگر تبدیل کنید\n
    شما با دکمه فایل مبدا میتوانید تصاویری را که قصد دارید تغیر دهید را انتخاب کنید
    و از طریق دکمه فایل مقصد شما مسیری را انتخاب میکنید که قصد دارید انجا ذخیره شود
    پس از انتخاب فرمت دلخواه باید روی دکمه پردازش کلیک کنید تا برنامه عملیات را شروع کند موفق باشید
    ''')
menu_bar = Menu(root)
help_menu=Menu(menu_bar, tearoff=0)
help_menu.add_command(label="کمک",command=tk_help)
help_menu.add_command(label="درباره", command=about_us)
help_menu.add_command(label="نسخه",command=tk_version)
help_menu.add_command(label="خروج",command=tk_quit)
menu_bar.add_cascade(label="راهنما", menu=help_menu)
root.config(menu=menu_bar)
# Front End-------------------------   /End

# Window Loop
root.mainloop()
