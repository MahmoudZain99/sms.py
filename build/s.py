from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import pymysql


class Student:

    # ________ connect + add data ________

    def add_student(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='zain')
        cur = con.cursor()
        cur.execute("insert into students values (%s,%s,%s,%s,%s,%s,%s)", (
            self.id_var.get(),
            self.name_var.get(),
            self.email_var.get(),
            self.phone_var.get(),
            self.Qualifications_var.get(),
            self.gender_var.get(),
            self.address_var.get()
        ))
        con.commit()
        self.fetch_all()
        self.clear()
        con.close()

    # ________ Fetch data from sql  ________

    def fetch_all(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='zain')
        cur = con.cursor()
        cur.execute('select * from students')
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("", END, value=row)

    # ________ Delete user ________

    def delete(self):

        con = pymysql.connect(host='localhost', user='root', password='', database='zain')
        cur = con.cursor()
        cur.execute('delete from students where id =%s', self.del_var.get())
        con.commit()
        self.fetch_all()
        con.close()

    # ________ Clear cells ________

    def clear(self):
        self.id_var.set('')
        self.name_var.set('')
        self.email_var.set('')
        self.phone_var.set('')
        self.Qualifications_var.set('')
        self.gender_var.set('')
        self.address_var.set('')
        self.fetch_all()

    # ________ Edit (row cursor focus) ________

    def get_cursor(self, ev):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents['values']
        self.id_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.phone_var.set(row[3])
        self.Qualifications_var.set(row[4])
        self.gender_var.set(row[5])
        self.address_var.set(row[6])

    # ________ Search ________

    def search(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='zain')
        cur = con.cursor()
        cur.execute("select * from students where " +
                    str(self.se_by.get()) + " LIKE '%" + self.se_var.get() + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("", END, value=row)

    # ________ PROGRAM WINDOW ________

    def __init__(self, root):
        self.root = root
        self.root.geometry('1500x790')
        self.root.title('School Management Program')
        self.root.configure(background='silver')
        self.root.resizable(False, False)
        title = Label(self.root,
                      text='[ Student registration system ]',
                      bg='#1AAECB',
                      font=('monospace', 14, 'bold'),
                      fg='White'
                      )
        title.pack(fill=X)

        # ________ Variables ________

        self.id_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.phone_var = StringVar()
        self.Qualifications_var = StringVar()
        self.gender_var = StringVar()
        self.address_var = StringVar()
        self.del_var = StringVar()
        self.se_by = StringVar()
        self.se_var = StringVar()

        # ________ DATA ENTRY FIELDS ________

        manage_frame = Frame(self.root, bg='white')
        manage_frame.place(x=1150, y=28, width=380, height=600)
        title = Label(manage_frame, text='Data Entry', font=('deco', 16), fg='white', bg='#2980B9')
        title.pack(fill=X)

        lbl_id = Label(manage_frame, bg='white', text='ID', justify='center', font=('deco', 14))
        lbl_id.place(x=80, y=30, width=200, height=30)
        id_entry = Entry(manage_frame, textvariable=self.id_var, bd='2', font=('Agency FB', 14))
        id_entry.place(x=15, y=60, width=320, height=30)

        lbl_name = Label(manage_frame, bg='white', text='Name', font=('deco', 14))
        lbl_name.place(x=80, y=90, width=200, height=30)
        name_entry = Entry(manage_frame, textvariable=self.name_var, bd='2', font=('Agency FB', 14))
        name_entry.place(x=15, y=120, width=320, height=30)

        lbl_email = Label(manage_frame, bg='white', text='Email', font=('deco', 14))
        lbl_email.place(x=80, y=150, width=200, height=30)
        email_entry = Entry(manage_frame, textvariable=self.email_var, bd='2', font=('Agency FB', 14))
        email_entry.place(x=15, y=180, width=320, height=30)

        lbl_phone = Label(manage_frame, bg='white', text='Phone', font=('deco', 14))
        lbl_phone.place(x=80, y=210, width=200, height=30)
        phone_entry = Entry(manage_frame, textvariable=self.phone_var, bd='2', font=('Agency FB', 14))
        phone_entry.place(x=15, y=240, width=320, height=30)

        lbl_qulif = Label(manage_frame, bg='white', text='Qualifications',
                          font=('deco', 14))
        lbl_qulif.place(x=80, y=270, width=200, height=30)
        qulif_entry = Entry(manage_frame, textvariable=self.Qualifications_var, bd='2', font=('Agency FB', 14))
        qulif_entry.place(x=15, y=300, width=320, height=30)

        lbl_gender = Label(manage_frame, bg='white', text='Gender',
                           font=('deco', 14))
        lbl_gender.place(x=80, y=330, width=200, height=30)
        combo_gender = ttk.Combobox(manage_frame, textvariable=self.gender_var)
        combo_gender['value'] = ('Male', 'Female')
        combo_gender.place(x=15, y=360, width=320, height=30)

        lbl_address = Label(manage_frame, bg='white', text='Address',
                            font=('deco', 14))
        lbl_address.place(x=80, y=390, width=200, height=30)
        address_entry = Entry(manage_frame, textvariable=self.address_var, bd='2', font=('Agency FB', 14))
        address_entry.place(x=15, y=420, width=320, height=30)

        lbl_delete = Label(manage_frame, fg='red', bg='white', text=' Delete (ID) ', font=('deco', 14))
        lbl_delete.place(x=80, y=450, width=200, height=30)
        delete_entry = Entry(manage_frame, textvariable=self.del_var, bd='2', font=('Agency FB', 14))
        delete_entry.place(x=15, y=480, width=320, height=30)

        # ________ BUTTONS ________

        btn_frame = Frame(self.root, bg='white')
        btn_frame.place(x=1150, y=560, width=380, height=367)
        title = Label(btn_frame, text='Control Panel', font=('deco', 16), fg='white', bg='#2980B9')
        title.pack(fill=X)

        add_btn = Button(btn_frame, text='Add', font=('deco', 14), bg='#85929E', command=self.add_student)
        add_btn.place(x=15, y=40, width=320, height=30)

        del_btn = Button(btn_frame, text='Delete', font=('deco', 14), bg='#85929E',
                         command=lambda: [self.delete(), self.msg_del()])
        del_btn.place(x=15, y=70, width=320, height=30)

        update_btn = Button(btn_frame, text='Edit', font=('deco', 14), bg='#85929E',
                            command=lambda: [self.update(), self.msg_edit()])
        update_btn.place(x=15, y=100, width=320, height=30)

        clear_btn = Button(btn_frame, text='Empty', font=('deco', 14), bg='#85929E', command=self.clear)
        clear_btn.place(x=15, y=130, width=320, height=30)

        about_btn = Button(btn_frame, text='Who are we', font=('deco', 14), bg='#85929E', command=self.about)
        about_btn.place(x=15, y=160, width=320, height=30)

        exit_btn = Button(btn_frame, text='Exit', font=('deco', 14), bg='#85929E', command=self.Exit_App)
        exit_btn.place(x=15, y=190, width=320, height=30)

        # ________ SEARCH MANAGE  ________

        search_frame = Frame(self.root, bg='white')
        search_frame.place(x=2, y=29, width=1147, height=50)

        lbl_search = Label(search_frame, text='Search by ', font=('deco', 14), bg='white')
        lbl_search.place(x=300, y=10)
        combo_search = ttk.Combobox(search_frame, textvariable=self.se_by, justify='right')
        combo_search['value'] = ('ID', 'Name', 'Email', 'Phone')
        combo_search.place(x=400, y=12, height='25')

        search_entry = Entry(search_frame, textvariable=self.se_var, justify='right', bd='2')
        search_entry.place(x='550', y='10', width='330', height='30')

        se_btn = Button(search_frame, text='Search', font=('deco', 14), bg='#3498DB', fg='white', command=self.search)
        se_btn.place(x='910', y='14', width='100', height='25')

        fe_btn = Button(search_frame, text='Refresh', bd=2, font=('deco', 6), bg='silver', fg='black',
                        command=self.fetch_all)
        fe_btn.place(x='20', y='14', width='70', height='25')

        # ________ DETAILS  ________

        details_frame = Frame(self.root, bg='#F2F4F4')
        details_frame.place(x='2', y='80', width='1146', height='709')

        # ________ SCROLL  ________

        scroll_x = Scrollbar(details_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(details_frame, orient=VERTICAL)

        # ________ TREE VIEW  ________

        self.student_table = ttk.Treeview(details_frame,
                                          columns=('id', 'name', 'phone', 'email', 'Qualifications', 'gender',
                                                   'address'),
                                          xscrollcommand=scroll_x.set,
                                          yscrollcommand=scroll_y.set

                                          )
        self.student_table.place(x='20', y='0', width='1127', height='691')
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=LEFT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.xview)

        self.student_table['show'] = 'headings'
        self.student_table.heading('id', text='ID')
        self.student_table.heading('gender', text='Gender')
        self.student_table.heading('Qualifications', text='Qualifications')
        self.student_table.heading('phone', text='phone')
        self.student_table.heading('email', text='email')
        self.student_table.heading('name', text='Name')
        self.student_table.heading('address', text='Address')

        self.student_table.column('address', width=60)
        self.student_table.column('gender', width=2)
        self.student_table.column('Qualifications', width=60)
        self.student_table.column('email', width=130)
        self.student_table.column('phone', width=60)
        self.student_table.column('name', width=100)
        self.student_table.column('id', width=20)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_all()

    # ________ Edit (update data) ________
    def update(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='zain')
        cur = con.cursor()
        cur.execute(
            "update students set address=%s,gender=%s,Qualifications=%s,email=%s,phone=%s,name=%s where id=%s ", (
                self.address_var.get(),
                self.gender_var.get(),
                self.Qualifications_var.get(),
                self.email_var.get(),
                self.phone_var.get(),
                self.name_var.get(),
                self.id_var.get()

            ))

        con.commit()
        self.fetch_all()
        self.clear()
        con.close()

    def about(self):
        messagebox.showinfo("HI", "This Program is Designed By Mahmoud Zain")

    def msg_del(self):
        messagebox.showwarning("Delete User", "User has been Deleted")

    def msg_edit(self):
        messagebox.showwarning("Edit User", "User Edited")

    def Exit_App(self):
        msg_box = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                         icon='warning')
        if msg_box == 'yes':
            root.destroy()


root = Tk()
ob = Student(root)
root.mainloop()
