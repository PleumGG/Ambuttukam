import customtkinter
app=customtkinter.CTk()
app.title('เครื่องคิดเลข')
app.geometry('500x500')

label = customtkinter.CTkLabel(app,text="หาพท.4เหลี่ยมจัตุราชา",fg_color='transparent',font=('Arai',40))
label.pack(pady=(20,0))
A = customtkinter.CTkLabel(app,text="หาได้รึป่าว",fg_color='transparent',font=('Arai',20))
A.pack(pady=(5,0))

answer_text=customtkinter.StringVar()
answer_label = customtkinter.CTkLabel(app,textvariable=answer_text,font=('Arai',40))
answer_label.pack(pady=(20,0))

#ปุ่มปัญญาอ่อน
def button_event():
    user_input1=entry.get()
    user_input2=entry1.get()
    
    
    answer=float(float(user_input1)*float(user_input2))
    result = str(answer)+"ตร.ม"
    answer_text.set(result)
    print(answer)

button = customtkinter.CTkButton(app,text='คำนวณ',command=button_event)
button.pack(pady=(15,0))

#กล่องรับค่า
entry = customtkinter.CTkEntry(app,placeholder_text="กว้าง")
entry.pack(pady=(15,0))
entry1= customtkinter.CTkEntry(app,placeholder_text="ยาว")
entry1.pack(pady=(15,0))
app.mainloop()