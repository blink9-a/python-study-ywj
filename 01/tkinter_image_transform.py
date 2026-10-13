import tkinter
import PIL.Image
import PIL.ImageTk

root = tkinter.Tk()
root.title("이미지 다중 배치 및 변형 프로그램")
root.geometry("600x500")

canvas = tkinter.Canvas(root, width=600, height=500, bg="white")
canvas.pack(fill="both", expand=True)

canvas.create_text(300, 30, text="이미지 크기 조절 및 회전 예시", font=("Arial", 14, "bold"))

pil_img1 = PIL.Image.open("image.png").convert("RGBA")
pil_img1 = pil_img1.resize((150, 150))
pil_img1 = pil_img1.rotate(45, expand=True, fillcolor=(0, 0, 0, 0))

tk_img1 = PIL.ImageTk.PhotoImage(pil_img1)
canvas.create_image(150, 250, image=tk_img1)

pil_img2 = PIL.Image.open("image.png")
pil_img2 = pil_img2.resize((200, 100))
pil_img2 = pil_img2.rotate(90, expand=True)

tk_img2 = PIL.ImageTk.PhotoImage(pil_img2)
canvas.create_image(450, 250, image=tk_img2)

root.mainloop()