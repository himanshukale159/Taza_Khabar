import io
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk,Image

class NewsApp:

    def __init__(self):

        #fetch Data
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=07ce6431517e45c5b04b589c36e5bed6').json()
        
        # intial GUI load
        self.load_gui()

        # load first news
        self.load_news_item(0)
    
    def load_gui(self):
        self.root = Tk()
        self.root.geometry('350x600')
        self.root.resizable(0,0)
        self.root.title("Taza Khabar")
        self.root.iconbitmap("news-icon-24.ico")
        self.root.configure(background='black')

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
    
    def load_news_item(self,idx):
        
        self.clear()

        try:
            image_url = self.data['articles'][idx]['urlToImage']
            raw_data = urlopen(image_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo = ImageTk.PhotoImage(im)
        except:
            image_url = "https://previews.123rf.com/images/momoforsale/momoforsale2105/momoforsale210500063/169348832-no-image-available-sign-isolated-on-white-background-vector-illustration.jpg"
            raw_data = urlopen(image_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo = ImageTk.PhotoImage(im)
            
        
        label = Label(self.root,image=photo)
        label.pack()


        heading = Label(self.root,text=self.data['articles'][idx]['title'],bg='black',fg='white',wraplength=350,justify='center')
        heading.pack(pady=(10,20))
        heading.config(font=('verdana',15))


        detail = Label(self.root,text=self.data['articles'][idx]['description'],bg='black',fg='white',wraplength=350,justify='center')
        detail.pack(pady=(10,20))
        detail.config(font=('verdana',12))

        frame = Frame(self.root,bg='black')
        frame.pack(expand=True,fill=BOTH)

        if idx != 0:
            prev = Button(frame,text="Previous",width=16,height=3,command=lambda: self.load_news_item(idx-1))
            prev.pack(side=LEFT)

        read = Button(frame, text='Read More', width=16, height=3,command=lambda :self.open_link(self.data['articles'][idx]['url']))
        read.pack(side=LEFT)

        if idx != len(self.data['articles'])-1:
            next =Button(frame,text='Next',width=16,height=3,command=lambda: self.load_news_item(idx+1))
            next.pack(side=LEFT)
        
        self.root.mainloop()

    def open_link(self,url):
        webbrowser.open(url)


obj = NewsApp()