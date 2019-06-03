from tkinter import *
import os 

window = Tk()
window.title("Đồ án tốt nghiệp")
window.geometry('800x600')

lbl_school = Label(window, text="Đại Học Sư Phạm Kỹ Thuật")
lbl_school.grid(column=0, row=0)
lbl_school.configure(font=("Times New Roman", 12, "bold"),anchor='center')

lbl_name = Label(window, text="Tên đề tài")
lbl_name.grid(column=0, row=1)

lbl_gvhd = Label(window, text="GVHD")
lbl_gvhd.grid(column=0, row=2)
 
lbl_svth = Label(window, text="SVTH")
lbl_svth.grid(column=0, row=3)

lbl_svth = Label(window, text="Nhận diện")
lbl_svth.grid(column=0, row=4)

def clicked_image():
    os.system('python recognize.py --detector face_detection_model \
	--embedding-model openface_nn4.small2.v1.t7 \
	--recognizer output/recognizer.pickle \
	--le output/le.pickle \
	--image images/patrick_bateman.jpg')
 
btn_image = Button(window, text="Ảnh", command=clicked_image)
btn_image.grid(column=1, row=4)
 
def clicked_video():
    os.system('python recognize_video.py --detector face_detection_model \
	--embedding-model openface_nn4.small2.v1.t7 \
	--recognizer output/recognizer.pickle \
	--le output/le.pickle')
 
btn_video = Button(window, text="Video", command=clicked_video)
btn_video.grid(column=2, row=4)


window.mainloop()