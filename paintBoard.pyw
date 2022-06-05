
import sys
from tkinter import messagebox, Menu, colorchooser
from tkinter.ttk import *
import tkinter as tk
import tkinter.simpledialog
from PIL import Image, ImageTk
from tkinter.filedialog import asksaveasfilename, askopenfilename
window = tk.Tk()
window.title('paint')
window.geometry('1000x700')
window.iconphoto(True, tk.PhotoImage(file='icon\\paint_icon.png'))
pencil, eraser, line, line_creat, save_path, r_creat, entry, text, img, name, open_path = None, None, None, None, None, None, None, None, None, None, None
line_c, bg_c, fill_c = (True, 'black'), (True, 'white'), (True, 'white')
last_pos, linepos, last_linepos, dele_list, text_pos = [
    0, 0], [0, 0], [0, 0], [[], [], []], [0, 0]
width_brushvalue, x_, y_, type_brush = 1, 750, 500, 'pencil'


class fuc_paint:
    def pencilcommand(self):
        global type_brush
        type_brush = 'pencil'

    def erasercommand(self):
        global type_brush
        type_brush = 'eraser'

    def linecommand(self):
        global type_brush
        type_brush = 'line'

    def rectanglecommand(self):
        global type_brush
        type_brush = 'rectangle'

    def textcommand(self):
        global type_brush
        type_brush = 'text'

    def weidth_appear(self):
        global width_brushvalue
        result = tkinter.simpledialog.askfloat(
            title=' ', prompt='width', initialvalue=width_brushvalue)
        if result == None:
            pass
        else:
            width_brushvalue = result

    def chooseColor(self):
        global line_c
        line_c = colorchooser.askcolor()

    def fillColor(self):
        global fill_c
        fill_c = colorchooser.askcolor()

    def one(self):
        global width_brushvalue
        width_brushvalue = 1

    def twenty_fifve(self):
        global width_brushvalue
        width_brushvalue = 25

    def fifty(self):
        global width_brushvalue
        width_brushvalue = 50

    def seventy_fifve(self):
        global width_brushvalue
        width_brushvalue = 75

    def dele(self):
        global dele_list
        if dele_list == []:
            pass
        else:
            try:
                for i in range(dele_list[1][len(dele_list[1])-1]):
                    number = len(dele_list[0])
                    cv.delete(dele_list[0][number-1])
                    cv.delete(dele_list[2][number-1])
                    dele_list[0] = dele_list[0][0:-1]
                    dele_list[2] = dele_list[2][0:-1]
                dele_list[1] = dele_list[1][0:-1]
            except IndexError:
                pass


class canvas_fuc:
    def resize(self):
        global x_, y_, cv
        x_y = tkinter.simpledialog.askstring(
            title=' ', prompt='resize', initialvalue=str(x_)+'x'+str(y_))
        if x_y == None:
            pass
        else:
            x_ = x_y.split('x')[0]
            y_ = x_y.split('x')[1]
        cv.configure(width=x_, height=y_)
        cv.coords(background_r, 0, 0, int(x_)+10, int(y_)+10)

    def bg_color(self):
        global bg_c, background_r, cv
        bg_c = colorchooser.askcolor()
        cv.itemconfig(background_r, fill=bg_c[1], outline=bg_c[1])


class start_fuc:
    def PNG(self):
        global fuc_start
        self.save_type = 'PNG'
        self.type_number = '.png'
        fuc_start.save_file()

    def JPEG(self):
        global fuc_start
        self.save_type = 'JPEG'
        self.type_number = '.jpeg'
        fuc_start.save_file()

    def GIF(self):
        global fuc_start
        self.save_type = 'GIF'
        self.type_number = '.gif'
        fuc_start.save_file()

    def save_file(self):
        global save_path, window, name, open_path
        from PIL import Image
        import os
        list = os.listdir('C:\\Program Files')
        cv.update()
        if 'gs' in list:
            save = asksaveasfilename(
                filetypes=[(self.save_type, self.type_number)])
            if save == '':
                pass
            else:
                cv.postscript(file=''.join([save, '.ps']), colormode='color')
                im = Image.open(''.join([save, '.ps']))
                im.save(''.join(
                    [save, self.type_number]), self.type_number.replace('.', ''))
                im.close()
                os.remove(''.join([save, '.ps']))
                name = os.path.split(save)
                open_path = name
                name = name[1].replace('.', '').replace(
                    'png', '').replace('jpeg', '').replace('gif', '')
                window.title(name)
        else:
            ret = messagebox.askquestion(title='warning', message="""Please install ghostscript, if not,
we can't save you image as PNG/JPEG/GIF
(Restart the program to enable).""")
            if ret == 'yes':
                os.popen('gs9561w64.exe')
                sys.exit()
            else:
                pass

    def openfile(self):
        import os
        global img, x_, y_, name, open_path, background_r
        openfilename = askopenfilename(
            filetypes=[('PNG', '.png'), ('JPG', '.jpeg'), ('GIF', '.gif')])
        if openfilename == '' or openfilename is None:
            pass
        else:
            openfilename = openfilename.replace('/', '\\')
            name = os.path.split(openfilename)
            open_path = name
            name = name[1].replace('.', '').replace(
                'png', '').replace('jpeg', '').replace('gif', '')
            img = ImageTk.PhotoImage(file=openfilename)
            sizeImage = Image.open(openfilename)
            cv.create_image(0, 0, anchor=tk.NW, image=img)
            x_ = sizeImage.width
            y_ = sizeImage.height
            cv.configure(width=x_-10, height=y_-10)
            cv.coords(background_r, 0, 0, int(x_)+10, int(y_)+10)
            window.title(name)

    def save_replace(self):
        import os
        global name, open_path
        if name != None:
            path = ''.join([open_path[0], '\\', name, '.ps'])
            cv.postscript(file=path, colormode='color')
            im = Image.open(path)
            end_type = open_path[1].replace(name, '')
            imgtypesave = ''.join[open_path[0], '\\', name+end_type]
            os.remove(imgtypesave)
            im.save(imgtypesave,
                    end_type.replace('.', ''))
            im.close()
            os.remove(path)

        else:
            fuc_start.PNG()


class mouse:
    def click(self, event):
        global last_pos, linepos, line_creat, line_c, width_brushvalue, r_creat, fill_c, bg_c, entry, text, dele_list, text_pos, width_brushvalue
        last_pos = [event.x, event.y]
        linepos = [event.x, event.y]
        if type_brush == 'text':
            cv.delete(text)
            if entry == None:
                entry = Entry(
                    window, background=bg_c[1], foreground=line_c[1], width=3)
                text = cv.create_window(event.x, event.y, window=entry)
                text_pos = [event.x, event.y]
                self.nu = 0
            else:
                if entry.get() == '':
                    pass
                else:
                    a = cv.create_text(text_pos[0], text_pos[1], text=entry.get(
                    ), fill=line_c[1])
                    dele_list[0].append(a)
                    dele_list[2].append(a)
                    self.nu = 1
                    entry = None
        else:
            if type_brush == 'line':
                line_creat = cv.create_line(
                    linepos[0], linepos[1], event.x, event.y, fill=line_c[1], width=width_brushvalue)
            elif type_brush == 'rectangle':
                r_creat = cv.create_rectangle(
                    linepos[0], linepos[1], event.x, event.y, outline=line_c[1], width=width_brushvalue, fill=fill_c[1])
                self.nu = 0
            self.nu = 0
            cv.bind("<B1-Motion>", mouse_fuc._paint)

    def _paint(self, event):
        global type_brush, width_brushvalue, last_pos, linepos, line_creat, r_creat
        if type_brush == 'pencil':
            if width_brushvalue == 1:
                a = cv.create_line(last_pos[0], last_pos[1], event.x,
                                   event.y, fill=line_c[1], width=width_brushvalue)
                dele_list[0].append(a)
                dele_list[2].append(a)
                self.nu += 1
            else:
                a = cv.create_line(last_pos[0], last_pos[1], event.x,
                                   event.y, fill=line_c[1], width=width_brushvalue)
                x1, y1 = (event.x - width_brushvalue /
                          2), (event.y - width_brushvalue / 2)
                x2, y2 = (event.x + width_brushvalue /
                          2), (event.y + width_brushvalue/2)
                b = cv.create_oval(
                    x1, y1, x2, y2, fill=line_c[1], outline=line_c[1])
                dele_list[0].append(a)
                dele_list[2].append(b)
                self.nu += 1
            last_pos = [event.x, event.y]

        elif type_brush == 'eraser':
            if width_brushvalue == 1:
                a = cv.create_line(last_pos[0], last_pos[1], event.x,
                                   event.y, fill='white', width=width_brushvalue)
                dele_list[0].append(a)
                dele_list[2].append(a)
                self.nu += 1
            else:
                a = cv.create_line(last_pos[0], last_pos[1], event.x,
                                   event.y, width=width_brushvalue, fill='white')
                x1, y1 = (event.x - width_brushvalue /
                          2), (event.y - width_brushvalue / 2)
                x2, y2 = (event.x + width_brushvalue /
                          2), (event.y + width_brushvalue/2)
                b = cv.create_oval(
                    x1, y1, x2, y2, fill='white', outline='white')
                dele_list[0].append(a)
                dele_list[2].append(b)
                self.nu += 1
            last_pos = [event.x, event.y]
        elif type_brush == 'line':
            cv.coords(line_creat, linepos[0], linepos[1], event.x, event.y)
            if line_creat in dele_list[0]:
                pass
            else:
                dele_list[0].append(line_creat)
                dele_list[2].append(line_creat)
            self.nu = 1
        elif type_brush == 'rectangle':
            cv.coords(r_creat, linepos[0], linepos[1], event.x, event.y)
            if r_creat in dele_list[0]:
                pass
            else:
                dele_list[0].append(r_creat)
                dele_list[2].append(r_creat)
            self.nu = 1

    def stop(self, event):
        if self.nu == 0:
            pass
        else:
            dele_list[1].append(self.nu)

    def pop(self, event):
        popmenu.post(event.x_root, event.y_root)


class keypress:
    def cheakkey(self, event):
        pass

    def savehotkey(self, event):
        global fuc_start
        fuc_start.PNG()

    def undohotkey(self, event):
        global paint_fuc
        paint_fuc.dele()

    def openhotkey(self, event):
        global fuc_start
        fuc_start.openfile()


keyfuc = keypress()
paint_fuc = fuc_paint()
fuc_canvas = canvas_fuc()
fuc_start = start_fuc()
mouse_fuc = mouse()
cv = tk.Canvas(window, width=x_, height=y_, bg='white')
background_r = cv.create_rectangle(
    0, 0, x_+10, y_+10, fill='white', outline='white')
menu = Menu(window)
filemenu = Menu(menu)
paintmenu = Menu(menu)
canvasmenu = Menu(menu)
brushmenu = Menu(menu)
typemenu = Menu(menu)
widthmenu = Menu(menu)
popmenu = Menu(menu)
window.config(menu=menu)
menu.add_cascade(label='File', menu=filemenu)
menu.add_cascade(label='Paint', menu=paintmenu)
menu.add_cascade(label='Canvas', menu=canvasmenu)
popmenu.add_command(label='undo', command=paint_fuc.dele)
filemenu.add_command(label='save', command=fuc_start.save_replace)
filemenu.add_cascade(label='saveAs', menu=typemenu)
filemenu.add_command(label='open', command=fuc_start.openfile)
typemenu.add_command(label='PNG', command=fuc_start.PNG)
typemenu.add_command(label='JPG', command=fuc_start.JPEG)
typemenu.add_command(label='GIF', command=fuc_start.GIF)
canvasmenu.add_command(label='resize', command=fuc_canvas.resize)
canvasmenu.add_command(label='bgcolor', command=fuc_canvas.bg_color)
paintmenu.add_cascade(label='Brush', menu=brushmenu)
brushmenu.add_command(label='pencil', command=paint_fuc.pencilcommand)
brushmenu.add_command(label='eraser', command=paint_fuc.erasercommand)
brushmenu.add_separator()
brushmenu.add_command(label='line', command=paint_fuc.linecommand)
brushmenu.add_command(label='rectangle', command=paint_fuc.rectanglecommand)
brushmenu.add_command(label='text', command=paint_fuc.textcommand)
paintmenu.add_cascade(label='width', menu=widthmenu)
img1 = ImageTk.PhotoImage(Image.open('icon\\1.png'))
widthmenu.add_command(command=paint_fuc.one, image=img1)
img2 = ImageTk.PhotoImage(Image.open('icon\\2.png'))
widthmenu.add_command(command=paint_fuc.twenty_fifve, image=img2)
img3 = ImageTk.PhotoImage(Image.open('icon\\3.png'))
widthmenu.add_command(command=paint_fuc.fifty, image=img3)
img4 = ImageTk.PhotoImage(Image.open('icon\\4.png'))
widthmenu.add_command(command=paint_fuc.seventy_fifve, image=img4)
paintmenu.add_command(label='fill color', command=paint_fuc.fillColor)
paintmenu.add_command(label='outline color', command=paint_fuc.chooseColor)
widthmenu.add_separator()
widthmenu.add_command(label=' other', command=paint_fuc.weidth_appear)
cv.pack(side='left', anchor='nw')


cv.bind('<Button-1>', mouse_fuc.click)
cv.bind('<Button-3>', mouse_fuc.pop)
cv.bind('<ButtonRelease-1>', mouse_fuc.stop)
window.bind('<Key>', keyfuc.cheakkey)
window.bind('<Control-s>', keyfuc.savehotkey)
window.bind('<Control-z>', keyfuc.undohotkey)
window.bind('<Control-o>', keyfuc.openhotkey)
window.mainloop()
