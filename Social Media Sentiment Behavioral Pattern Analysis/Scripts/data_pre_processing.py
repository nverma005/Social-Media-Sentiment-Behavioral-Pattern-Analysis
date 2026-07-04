import os
import re
import nltk
import pandas as pd
from tkinter import *
import tkinter as tk_gui_dpp
from bs4 import BeautifulSoup
from langdetect import detect
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from tkinter import filedialog,messagebox
from nltk.sentiment.vader import SentimentIntensityAnalyzer



class cls_data_pre_prcs:

    # gui window
    @staticmethod
    def fn_gui_dpp():
        # Canvas
        canvas_gui_dpp = tk_gui_dpp.Tk()
        canvas_gui_dpp.geometry('800x800')
        canvas_gui_dpp.title('Step 2: Data Pre Processing')

        # Labels
        lbl_title = tk_gui_dpp.Label(canvas_gui_dpp, text='Data Pre Processing')
        lbl_title.place(x=300, y=50)

        lbl_slct = tk_gui_dpp.Label(canvas_gui_dpp, text="Select Dataset : ")
        lbl_slct.place(x=100, y=150)

        entry_file_path = tk_gui_dpp.Entry(canvas_gui_dpp, width='45')
        entry_file_path.place(x=220, y=150)
        # entry_file_path.configure(validate='key', validatecommand=lambda: cls_data_pre_prcs.fn_upload_dset(None))

        # Button Browse
        btn_Upload = tk_gui_dpp.Button(canvas_gui_dpp, text='Upload',
                                       command=lambda: cls_data_pre_prcs.fn_upload_dset(entry_file_path))
        btn_Upload.place(x=540, y=149)

        # Button Start
        btn_start = tk_gui_dpp.Button(canvas_gui_dpp, text='Start',
                                      command=lambda: cls_data_pre_prcs.fn_data_preprocess_btn(entry_file_path,btn_start,status_text))
        btn_start.place(x=290, y=230)
        btn_start.configure(height=1, width=20)

        status_text = tk_gui_dpp.Text(canvas_gui_dpp, height=18, width=60)
        status_text.place(x=100,y=300)

        print('gui pre processing done')  # test

        canvas_gui_dpp.mainloop()



    # upload data set button
    @staticmethod
    def fn_upload_dset(entry_file_path):
        upld_file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        entry_file_path.delete('0', tk_gui_dpp.END)
        entry_file_path.insert(tk_gui_dpp.END , upld_file_path)

        print('upload dset done')  # test


    # 1 Remove html tags
    @staticmethod
    def fn_rmv_html_tags(text):
        if isinstance(text, str):  # Check for NaN values
            b_soup = BeautifulSoup(text, "html.parser")
            return b_soup.get_text()
        return text


    # 2 remove special characters and numbers
    @staticmethod
    def fn_rmv_spcl_chrctr(text):
        if isinstance(text, str):
            return  ''.join(e for e in text if e.isalnum() or e.isspace())
        return str(text)




    # 3 convert to lower case
    @staticmethod
    def fn_cnvrt_lwrcase(text):
        return text.lower()

    # 4 tokenization
    @staticmethod
    def fn_tknyz_txt(text):
        return word_tokenize(text)


    # 5 remove stopwords
    @staticmethod
    def fn_rmv_stpwrd(tokens):
        stp_wrds = set(stopwords.words("english"))
        return  [token for token in tokens if token not in stp_wrds]


    # 6 remove unnecessary spaces
    @staticmethod
    def fn_rmv_extra_spacs(text):
        return " ".join(text.split())


    # 7 lemmatization
    @staticmethod
    def fn_lmtyz_txt(tokens):
        lmtyzr = WordNetLemmatizer()
        return  [lmtyzr.lemmatize(token) for token in tokens]


    # 8 negation handling
    @staticmethod
    def fn_handle_negations(tokens):
        negtn_words = set(
            ["not", "no", "never", "don't", "doesn't", "didn't", "can't", "couldn't", "won't", "wouldn't"])
        otpt = []
        negation = False
        for token in tokens:
            if token in negtn_words:
                negation = True
            elif negation:
                token = "NOT_" + token
                negation = False
            otpt.append(token)
        return otpt

    @staticmethod
    def rmv_spcfc_wrds(text):
        spcfc_wrds = ["now","my","as","new","world", "people", "so","Monday","may", "radio", "ari", "by","out","sunday","some", " it","than","also","sheila", "body",
                      "after", "their","into","live", "but","two","own", "on", "will", "at", "he", "are","food", "i", "one","so", "tune", "lasso", "it","we","day","what",
                      "an","when","posted", "the", "is", "this", "been","air","sea", "more","2023", "a","could","iwa", "from", "us", "nsfw","like", "who","july","most",
                      "httpssapmaradioidpublicsapmaradio", "your","all", "its","near","our", "my","being ","just", "you","week","she","not ","6","can", "about","had",
                      "in", "k","has","up","why","they", "has", "they", "day", "and","be", "to", "sapma", "says","how", "that","while", "feat", "his", "with", "over","say",
                      "monday","if", "were","have", "playing", "ground","special", "take","groundnews","4", "news","into","me","first","north","kennedy","this","say",
                      "house","no","bc","court", "was","gop","watch","her","bid","them","would","report","may","for","him","jr", "said","target","where", " breakingnews",
                      "people","make","not","officials","do","bbc"	,"before","former","get", "6","campaign","probe","being","back","block","before","there","jan","off",
                      "of","lead","press","than","high","tuesday","woman","know","bc","against","one", "they","him","or","years","year","act","video","dead","trial",
                      "taking","team","around","hes","set","other","officials","top","man","meeting","jan","itaworldsbk","media","against",	"photos","under","2020","plan",
                      "latest","cup","target","according","second","which","years","three","deal","black","last","alzheimers","troopsdieasalliesstalljetsusputsoilb4food",
                      "north",	"found","2024","down","year","since","0","ai","time","gop","woman","season","home" ,"womens","help","breakingnews","during","ground",
                      "times","west","groundnews","report","final","cbc","kelowna","games","across","castanet","south","topheadlines"		]

        wrds = text.split()
        fltrd_wrds = [word for word in wrds if word not in spcfc_wrds]
        return ' '.join(fltrd_wrds)

    # 9 Remove non english language
    @staticmethod
    def fn_rmv_non_english(data_frm):
        print("Starting remove_non_english method...")
        data_frm['language'] = data_frm['text'].apply(lambda x: detect(x) if isinstance(x, str) and x.strip() else '')
        print("Language column added...")
        data_frm = data_frm[data_frm['language'] == 'en']
        data_frm = data_frm.drop(columns=['language'])
        print("Non-English rows removed...")
        return data_frm


    # 10 Remove duplicate rows
    @staticmethod
    def fn_rmv_dplct_rws(data_frm):
        data_frm['tokens'] = data_frm['tokens'].apply(lambda x: ' '.join(x))  # Convert list of tokens to a string
        data_frm.drop_duplicates(inplace=True)
        data_frm['tokens'] = data_frm['tokens'].apply(word_tokenize)  # Convert the string back to a list of tokens
        return data_frm

    # 11 sentiment ( positive, negative, netural) using VADER
    @staticmethod
    def sentiment_analysis(text):
        analyzer = SentimentIntensityAnalyzer()
        sentiment_score = analyzer.polarity_scores(text)

        if sentiment_score['compound'] >= 0.05:
            return 'positive'
        elif sentiment_score['compound'] <= -0.05:
            return 'negative'
        else:
            return 'neutral'

    @staticmethod
    def perform_sentiment_analysis(data_frm):
        data_frm['Sentiment'] = data_frm['text'].apply(cls_data_pre_prcs.sentiment_analysis)
        return data_frm



    # call all preprocess steps
    @staticmethod
    def pre_prcs_data(input_dset, output_dset,status_text):
        status_text.delete(1.0,tk_gui_dpp.END)
        status_text.insert(tk_gui_dpp.END, 'Starting Data Pre-processing ... \n')

        data_frm = pd.read_csv(input_dset)

        # step 1 fn_rmv_html_tags
        data_frm['text'] = data_frm['text'].apply(cls_data_pre_prcs.fn_rmv_html_tags)
        status_text.insert(tk_gui_dpp.END, "Step 1: Removing HTML tags - Done.\n")

        # step 2 fn_rmv_spcl_chrctr
        data_frm['text'] = data_frm['text'].apply(cls_data_pre_prcs.fn_rmv_spcl_chrctr)
        status_text.insert(tk_gui_dpp.END, "Step 2: Removing special characters and numbers - Done.\n")

        # step 3 fn_cnvrt_lwrcase
        data_frm['text'] = data_frm['text'].apply(cls_data_pre_prcs.fn_cnvrt_lwrcase)
        status_text.insert(tk_gui_dpp.END, "Step 3: Converting text to lowercase - Done.\n")

        # step 4 fn_tknyz_txt
        data_frm['tokens'] = data_frm['text'].apply(cls_data_pre_prcs.fn_tknyz_txt)
        status_text.insert(tk_gui_dpp.END, "Step 4: Tokenization - Done.\n")

        # step 5 fn_rmv_stpwrd
        data_frm['tokens'] = data_frm['tokens'].apply(cls_data_pre_prcs.fn_rmv_stpwrd)
        status_text.insert(tk_gui_dpp.END, "Step 5: Stopword removal - Done.\n")

        # step 6 fn_rmv_extra_spacs
        data_frm['text'] = data_frm['text'].apply(cls_data_pre_prcs.fn_rmv_extra_spacs)
        status_text.insert(tk_gui_dpp.END, "Step 6: Removing unnecessary spaces - Done.\n")

        # step 7 fn_lmtyz_txt
        data_frm['tokens'] = data_frm['tokens'].apply(cls_data_pre_prcs.fn_lmtyz_txt)
        status_text.insert(tk_gui_dpp.END, "Step 7: Lemmatization - Done.\n")

        # step 8 fn_handle_negations
        data_frm['tokens'] = data_frm['tokens'].apply(cls_data_pre_prcs.fn_handle_negations)
        status_text.insert(tk_gui_dpp.END, "Step 8: Handle negations - Done.\n")

        # Step Remove specific words
        data_frm['text'] = data_frm['text'].apply(cls_data_pre_prcs.rmv_spcfc_wrds)
        status_text.insert(tk_gui_dpp.END, "Step : Remove specific words - Done.\n")

        # step 9 fn_rmv_non_english
        data_frm = cls_data_pre_prcs.fn_rmv_non_english(data_frm)
        status_text.insert(tk_gui_dpp.END, "Step 9: Remove non-English text - Done.\n")

        # step 10 fn_rmv_dplct_rws
        data_frm = cls_data_pre_prcs.fn_rmv_dplct_rws(data_frm)
        status_text.insert(tk_gui_dpp.END, "Step 10: Remove duplicates - Done.\n")

        # Step 11: Sentiment Analysis
        data_frm = cls_data_pre_prcs.perform_sentiment_analysis(data_frm)
        status_text.insert(tk_gui_dpp.END, "Step 11: Sentiment Analysis - Done.\n")

        # save preprocessed data to new file
        output_file = os.path.join(output_dset, 'pre_processed_data.csv')
        data_frm.to_csv(output_file,index=False)

        status_text.insert(tk_gui_dpp.END, f" Data Preprocessing completed. Preprocessed file saved at below mentione path:\n\n " +input_dset +"\n")
        messagebox.showinfo("Data Pre-processing", "Data preprocessing is complete.")

        return output_file

    # start button
    @staticmethod
    def fn_data_preprocess_btn(entry_file_path,btn_start,status_text):

        input_dset = entry_file_path.get()
        output_fldr = "Pre Processed Dataset"

        if not os.path.exists(output_fldr):
            os.makedirs(output_fldr)
        # Delete any existing preprocessed CSV file
        output_file = os.path.join(output_fldr,'preprocessed_dataset.csv')
        if os.path.exists(output_file):
            os.remove(output_file)

        cls_data_pre_prcs.pre_prcs_data(input_dset,output_fldr,status_text)
        btn_start.config(state=tk_gui_dpp.DISABLED)

        #messagebox.showinfo('Data Pre Processing','Pre processing done sucessfully')
        print('data preprocess button ')       # test

if __name__ == '__cls_data_pre_prcs__':

    cls_data_pre_prcs()