
import mastodon.utility
from mastodon.utility import *
from mastodon import Mastodon, StreamListener
import tkinter as gui_dc
from tkinter import messagebox,Scrollbar
import csv
import os
import time
import threading

class cls_data_collection:

    global mastodon
    # Mastodon Authentication
    clnt_id = 'RO9_LFCNfSEG0vLXtmOkyACer96bRWndA6Cd8LFEu0k'
    clnt_scrt = 'o59V2Kod3Q49mL7c0L10_InsAyEVbszPesXPx-mHcM8'
    acs_tkn = 'r9UZM6ccbqbMccT6uPY6O_981PRcZSamUMosSlcPxwE'
    url_lnk = 'https://mastodon.social'
    mastodon = Mastodon(
        client_id=clnt_id,
        client_secret=clnt_scrt,
        access_token=acs_tkn,
        api_base_url=url_lnk,
        version_check_mode='none'
    )
    # fetch data
    @staticmethod
    def fn_ftch_data():
        timln_data = Mastodon.timeline_home(self=mastodon,limit=100)
        fchd_data =[]
        if timln_data != None:
            for pst_data in timln_data:

                post_datetime = pst_data["created_at"]
                post_id = int(pst_data["id"])
                post_text = pst_data["content"]
                user_name = pst_data["account"]["display_name"]
                fchd_data.append((post_datetime, post_id, post_text, user_name))
                #post_info = f"Datetime: {post_datetime}\nPost ID: {post_id}\nContent: {post_text}\nUser: {user_name}\n"
            return fchd_data
        else:
            messagebox.showinfo('Data Collection', 'Error while fetching data')
    # display data
    @staticmethod
    def fn_dsply_data(lst_bx_posts_data):
        post_dsplay = cls_data_collection.fn_ftch_data()
        for pst_data in post_dsplay:
            lst_bx_posts_data.insert(gui_dc.END, f"Post Date: {pst_data[0]}\nPost ID: {pst_data[1]}\ntext: {pst_data[2]}\nUser Name: {pst_data[3]}\n\n" + "\n\n\n" + '_____________________' + "\n\n\n")
    @staticmethod
    def appnd_data_csv(file_path, data):
        with open(file_path,'a',newline='',encoding='utf-8') as apnd_csv_file:
            apnd_wrtr = csv.writer(apnd_csv_file)
            apnd_wrtr.writerows(data)
    @staticmethod
    def crte_fldr(fldr_name):
        prjct_path = os.getcwd()
        fldr_path = os.path.join(prjct_path, fldr_name)

        if not os.path.exists(fldr_path):
            os.mkdir(fldr_path)
            print(f"Folder '{fldr_name}' created successfully.")
        else:
            print(f"Folder '{fldr_name}' already exists.")
    @staticmethod
    def crt_csv_file(fldr_name):
        fldr_path = os.path.join(os.getcwd(), fldr_name)
        file_path = os.path.join(fldr_path,'md_dataset.csv')
        if not os.path.exists(file_path):
            with open(file_path, 'w', newline='', encoding='utf-8') as wrt_csv_file:
                writer = csv.writer(wrt_csv_file)
                writer.writerow(['Post Date', 'Post ID', 'text', 'User Name'])
            print(f"CSV file '{file_path}' created successfully.")
        else:
            print(f"CSV file '{file_path}' already exists.")
    @staticmethod
    def get_latest_post_id(file_path):
        latest_post_id = ''
        if os.path.exists(file_path):
            with open(file_path, 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                for row in reader:
                    post_id = row[1]
                    if post_id > str(latest_post_id):
                        latest_post_id = str(post_id)
        return latest_post_id
    @staticmethod
    def ftch_and_apnd_data(fldr_name):
        fldr_path = os.path.join(os.getcwd(), fldr_name)
        file_path = os.path.join(fldr_path,'md_dataset.csv')

        ltst_post_id = cls_data_collection.get_latest_post_id(file_path)
        new_data = []

        timeline = mastodon.timeline_home(limit=100)
        for stats in timeline:
            post_date = stats['created_at']
            post_id = str(stats['id'])  # Convert post ID to int
            post_text = stats['content']
            user_name = stats['account']['display_name']

            #if post_id > int(ltst_post_id):
            if post_id > str(ltst_post_id):
                new_data.append((post_date, post_id, post_text, user_name))

        if new_data:

            cls_data_collection.appnd_data_csv(file_path, new_data)
            print(f"Data appended to '{file_path}'.")
    @staticmethod
    def gnrt_data(fldr_name):
        while True:
            cls_data_collection.crte_fldr(fldr_name)
            cls_data_collection.crt_csv_file(fldr_name)
            cls_data_collection.ftch_and_apnd_data(fldr_name)
            print('Data generated')
            time.sleep(2 * 60)
            #print('Data genrated')
    def fn_gui_data_collection():

        # Canvas
        canvas_gui_dc = gui_dc.Tk()
        canvas_gui_dc.geometry('700x700')
        canvas_gui_dc.title('Step 1: Data Collection')
        #Labels
        lbl_title = gui_dc.Label(canvas_gui_dc, text='Data Collection')
        lbl_title.place(x=300, y=50)
        lst_bx_posts_data = gui_dc.Text(canvas_gui_dc)
        lst_bx_posts_data.place(x=100, y=180)
        lst_bx_posts_data.configure(height=10, width=50)
        # Buttons
        btn_ftch = gui_dc.Button(canvas_gui_dc, text='Fetch and Display Data',command=lambda: cls_data_collection.fn_dsply_data(lst_bx_posts_data))
        btn_ftch.place(x=90, y=120)
        btn_ftch.configure(height=1, width=25)
        #btn_gnrte_ds = gui_dc.Button(canvas_gui_dc,text='Genrate Data Set',command=lambda: cls_data_collection.gnrt_data('Mastodon dataset'))
        btn_gnrte_ds = gui_dc.Button(canvas_gui_dc,text='Generate Data Set',command=lambda: cls_data_collection.gnrt_data("Mastodon dataset"))
        #btn_gnrte_ds = gui_dc.Button(canvas_gui_dc,text='Genrate Data Set',command=cls_data_collection.Genrate_data)
        btn_gnrte_ds.place(x=310,y=120)
        btn_gnrte_ds.configure(height=1,width=20)
        canvas_gui_dc.mainloop()

if __name__ == '__cls_data_collection__':

    cls_data_collection()






