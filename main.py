from urllib.request import Request,urlopen
from bs4 import BeautifulSoup
import re
from pprint import pprint as pp
from tkinter import *
from tkinter import messagebox as msgbx
class Application(Frame):
	def __init__(self,master=None,res=None,links = None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()
		self.addContent(res)
		self.Links = links
	def createWidgets(self):
		self.QUIT = Button(self,text = "Quit", command = self.quit)
		self.QUIT.pack({"side":"bottom"})
	def addContent(self,res = None):
		self.Top = Label(self,text="Tech News Today")
		self.Top.pack()
		if res == None:
			msgbx.showwarning(self,"Something's Broken! Please Check and Retry")
		else:
			i=0
			erp = iter(s)
			self.scrollbar = Scrollbar(self)
			self.scrollbar.pack(side = RIGHT,fill = Y)
			self.ML = Listbox(self,width = 800,height = 600,yscrollcommand = self.scrollbar.set)
			while i<len(res):
				self.ML.insert(END,str(i+1)+" "+next(erp))
				i+=1
			self.ML.pack(side=LEFT,fill=BOTH)
			self.scrollbar.config(command = self.ML.yview)
			self.ML.bind("<<ListboxSelect>>",self.poll)

	def poll(self,*event):
		selected = self.ML.curselection()
		print(self.Links)

req = Request('https://www.gadgetsnow.com/tech-news',headers = {'User-Agent':'Mozilla/5.0'})
data = urlopen(req)
soup = BeautifulSoup(data,"html.parser")
l = soup.find_all("span",{"class":"w_tle"})
s = set()  # Title Set
ls = [] #Links Set
for name in l[:-4]:
	s.add(name.a.get_text())
	ls.append(name.a['href'])
root = Tk()
root.title("Tech News App")
app = Application(master=root,res=s,links = ls)
app.mainloop()
app.destroy()
