from numpy import *
from tkinter import *  #第一步是导入Tkinter包的所有内容：
import tkinter.messagebox as messagebox
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.helloLabel = Label(self, text='输入未知数个数 如3 \n起始与末尾都不要打空格!')  # 标签
        self.helloLabel.pack()
        self.expression = Entry(self)  # 单行文本框
        self.expression.pack()
        self.helloLabel = Label(self, text='输入系数矩阵A 请按行输入 \n每个数间以空格间断 如3 3 4!')  # 标签
        self.helloLabel.pack()
        self.expression1 = Entry(self)  # 单行文本框
        self.expression1.pack()
        self.helloLabel2 = Label(self, text='输入AX=B中B 请按列输入 \n每个数间以空格间断 如3 3 4!')  # 标签
        self.helloLabel2.pack()
        self.expression2 = Entry(self)  # 单行文本框
        self.expression2.pack()
        self.alertButton = Button(self, text='Evaluate it!', command=self.compute)  # 按钮
        self.alertButton.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()
        self.checkbutton = Checkbutton(self, )

    def compute(self):
        Numble  = self.expression.get() or '0'
        Numble = int(Numble)
        a = eye(Numble, Numble, dtype=float32)
        Numble1  = self.expression1.get() or '0'
        Numble1 = str.split(Numble1)
        Numble1 = list(map(float, Numble1))
        a = array([Numble1]).reshape(Numble, Numble)

        b = eye(Numble, 1, dtype=float32)
        Numble2  = self.expression2.get() or '0'
        Numble2 = str.split(Numble2)
        Numble2 = list(map(float, Numble2))
        b = array([Numble2]).reshape(Numble, 1)
        c = concatenate([a, b], axis=1)
        print('a',a)
        print('b',b)
        print('c',c)



        def guass(Numble, c):
            for _ in range(Numble):
                #    print(_)
                e = c[_:Numble, _]  # 划出第 - 列
                if abs(max(e)) > abs(min(e)):  # 找绝对值最大
                    f = where(e == max(e))
                elif max(e) == 0:
                    t = 1
                    break
                else:
                    f = where(e == min(e))
                g = ((f[0]).tolist()[0])
                Akk = e[g]
                if Akk == 0:  # 顺序主子式不为0
                    t = 1
                    break
                if g != 0:
                    c[[_, g + _], :] = c[[g + _, _], :]  # 交换二维numpy数组中的两行
                p1 = Numble - _ - 1
                p2 = Numble + 1
                for o in range(p1):
                    c1 = copy(c[_ + o + 1, _])
                    Mik = c1 / Akk
                    for q in range(p2):
                        c[_ + o + 1, q] = c[_ + o + 1, q] - Mik * c[_, q]
            print('改后[A,b]', c)
            return c

        # 分解为 L , U
        def tri(Numble, a):  # l xia  u shang
            l = eye(Numble, Numble, dtype=float32)
            u = zeros((Numble, Numble), dtype=float32)
            t = 1
            r = 0
            for m in range(Numble * Numble):
                ma = 0
                if t == 1:
                    for i in range(r, Numble):
                        ma = 0
                        for _ in range(r):
                            ma = ma + u[_, i] * l[r, _]
                        u[r, i] = a[r, i] - ma
                    t = t - 1
                if t != 1:
                    for i in range(r + 1, Numble):
                        ma = 0
                        for _ in range(r):
                            ma = l[i, _] * u[_, r] + ma
                        l[i, r] = (a[i, r] - ma) / u[r, r]
                    t = t + 1
                    r = r + 1
            return l, u

        # 求 Y
        def counter2(l, b, Numble):
            d = zeros(Numble, dtype=float32)
            for q3 in range(Numble):
                MA = 0
                if q3 == 0:
                    d[0] = b[0]
                else:
                    for q4 in range(q3):
                        MA = MA + d[q4] * l[q3, q4]
                    d[q3] = b[q3] - MA
            return d
            print(l, u)

        # 计算 x
        def counter(c, Numble):
            d = zeros(Numble, dtype=float32)
            for q3 in range(Numble):
                MA = 0
                if q3 == 0:
                    d[Numble - 1] = c[Numble - 1, Numble] / c[Numble - 1, Numble - 1]
                else:
                    for q4 in range(q3):
                        MA = MA + d[Numble - q3 + q4] * c[
                            Numble - q3 - 1, Numble - q3 + q4]  # MA    0.23376622961038956
                    d[Numble - q3 - 1] = (c[Numble - q3 - 1, Numble] - MA) / c[Numble - q3 - 1, Numble - q3 - 1]
            return d

            # 三角
        t = 0
        c1 = guass(Numble, c)
        d2 = counter(c1, Numble)
        l, u = tri(Numble, a)
        d = counter2(l, b, Numble)
        k = column_stack((u, d))
        d3 = counter(k, Numble)
        if t == 0:
            messagebox.showinfo('Result', '列主元消去法解为%s\n直接三角分解解为%s\n出nan表无唯一解' %(d2,d3) )
        else:
            messagebox.showinfo('error')

app = Application()
# 设置窗口标题:
app.master.title('计算 A @ X = B')
# 主消息循环:
app.mainloop()