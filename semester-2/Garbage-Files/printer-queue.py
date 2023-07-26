class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)
    def is_empty(self):
        return len(self.items) == 0
    
class Print(Queue):
    def __init__(self):
        Queue.__init__(self)
    def add_page(self,page):
        self.enqueue(page)
    def print_it(self):
        if self.is_empty():
            print("no pages to print")
        else:
            print("printer loading...")
            from time import sleep as s
            s(3) # time took by printer >_
            while not self.is_empty():
                page = str(self.dequeue())
                print("printing page " + page)
            print("All pages printed")
      
printer_ready = True          
a = Print()
a.add_page('page1.txt')
a.add_page('page2.txt')
a.add_page('page3.txt')
a.add_page('page4.txt')
if printer_ready:
    a.print_it()