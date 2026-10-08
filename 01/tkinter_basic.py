
import tkinter
import PIL.Image
import PIL.ImageTk

root = tkinter.Tk()
root.title("이미지 다중 배치 및 변형 프로그램")
root.geometry("600x500")

canvas = tkinter.Canvas(root, width=600, height=500, bg="white")
canvas.pack(fill="both", expand=True)

canvas.create_text(300, 30, text="이미지 크기 조절 및 회전", font=("Arial", 14, "bold"))

root.mainloop()
