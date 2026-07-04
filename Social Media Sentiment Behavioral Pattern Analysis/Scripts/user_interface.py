import tkinter as tk_gui

import data_access_layer
from data_access_layer import cls_function_logic
#from Scripts.Sentiment_analysis_clcik import cls_sentiment_analysis


class cls_gui_frame:

    def fn_gui():
        # Canvas
        canvas_gui = tk_gui.Tk()
        canvas_gui.geometry('500x500')


        canvas_gui.title('Sentiment Analysis')
        canvas_gui.configure(bg="#cdd5d6")

        # Labels
        lbl_title = tk_gui.Label(canvas_gui, text='Sentiment Analysis')
        lbl_title.place(x=160, y=50)



        # STEP 1 : Data collection ****************************
        lbl_title = tk_gui.Label(canvas_gui, text='Step 1:')
        lbl_title.place(x=100, y=100)

        # Button  Data collection
        btn_data_collection = tk_gui.Button(canvas_gui, text='Data collection', command=cls_function_logic.fn_data_ftch)
        btn_data_collection.place(x=200, y=98)
        btn_data_collection.configure(height=1, width=25)

        # STEP 2 : Data pre-processing
        lbl_title_2 = tk_gui.Label(canvas_gui, text='Step 2:')
        lbl_title_2.place(x=100, y=160)

        # Button  Data pre-processing
        btn_data_pre_prcs = tk_gui.Button(canvas_gui, text='Data Pre-Processing', command=cls_function_logic.fn_data_pre_prcsng)
        btn_data_pre_prcs.place(x=200, y=158)
        btn_data_pre_prcs.configure(height=1, width=25)

        canvas_gui.mainloop()

if __name__ == '__main__':

    cls_gui_frame.fn_gui()

    ''' # **************************** Button Sentiment Analysis *************************************

        #  Sentiment Analysis
        lbl_title_3 = tk_gui.Label(canvas_gui, text='Step 3:')
        lbl_title_3.place(x=100, y=220)

        btn_sa = tk_gui.Button(canvas_gui, text='Sentiment Analysis',command=cls_function_logic.fn_sa)
        btn_sa.place(x=200, y=219)
        btn_sa.configure(height=1, width=25)'''

        




















