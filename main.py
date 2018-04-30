from googlesearch import search
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
		
links = list(search('Tech News',num=10,stop=1,pause=2))
req = Request(links[0],headers = {'User-Agent':'Mozilla/5.0'})
data = urlopen(req)
content = data.read()
soup = BeautifulSoup(content,"html.parser")
l = soup.find_all("a",href=re.compile("tech-news/"))
s = set()  # Title Set
ls = [] #Links Set
for link in l:
	p = link.get('title')
	q = link.get('href')
	if(p is not None and q is not None):
		s.add(p)
		ls.append(q)
root = Tk()
app = Application(master=root,res=s,links = ls)
app.mainloop()
app.destroy()

	
	
