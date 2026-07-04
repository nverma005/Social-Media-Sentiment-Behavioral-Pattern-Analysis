import os
import csv
import time
import threading
import tkinter as gui_dc
from tkinter import messagebox
from mastodon import Mastodon
from dotenv import load_dotenv

load_dotenv()

mastodon = Mastodon(
    client_id=os.getenv('MASTODON_CLIENT_ID'),
    client_secret=os.getenv('MASTODON_CLIENT_SECRET'),
    access_token=os.getenv('MASTODON_ACCESS_TOKEN'),
    api_base_url=os.getenv('MASTODON_URL'),
    version_check_mode='none'
)

class cls_data_collection:

    @staticmethod
    def fn_ftch_data():
        timln_data = mastodon.timeline_home(limit=100)
        fchd_data = []
        if timln_data:
            for pst_data in timln_data:
                post_datetime = pst_data["created_at"]
                post_id = int(pst_data["id"])
                post_text = pst_data["content"]
                user_name = pst_data["account"]["display_name"]
                fchd_data.append((post_datetime, post_id, post_text, user_name))
            return fchd_data
        else:
            messagebox.showinfo('Data Collection', 'Error while fetching data')

    @staticmethod
    def fn_dsply_data(lst_bx_posts_data):
        post_dsplay = cls_data_collection.fn_ftch_data()
        for pst_data in post_dsplay:
            lst_bx_posts_data.insert(gui_dc.END, f"Post Date: {pst_data[0]}\nPost ID: {pst_data[1]}\ntext: {pst_data[2]}\nUser Name: {pst_data[3]}\n\n" + '_____________________' + "\n\n\n")

    @staticmethod
    def appnd_data_csv(file_path, data):
        with open(file_path, 'a', newline='', encoding='utf-8') as apnd_csv_file:
            apnd_wrtr = csv.writer(apnd_csv_file)
            apnd_wrtr.writerows(data)

    @staticmethod
    def crte_fldr(fldr_name):
        fldr_path = os.path.join(os.getcwd(), fldr_name)
        if not os.path.exists(fldr_path):
            os.mkdir(fldr_path)

    @staticmethod
    def crt_csv_file(fldr_name):
        fldr_path = os.path.join(os.getcwd(), fldr_name)
        file_path = os.path.join(fldr_path, 'md_dataset.csv')
        if not os.path.exists(file_path):
            with open(file_path, 'w', newline='', encoding='utf-8') as wrt_csv_file:
                writer = csv.writer(wrt_csv_file)
                writer.writerow(['Post Date', 'Post ID', 'text', 'User Name'])

    @staticmethod
    def get_latest_post_id(file_path):
        latest_post_id = ''
        if os.path.exists(file_path):
            with open(file_path, 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    post_id = row[1]
                    if post_id > str(latest_post_id):
                        latest_post_id = str(post_id)
        return latest_post_id

    @staticmethod
    def ftch_and_apnd_data(fldr_name):
        fldr_path = os.path.join(os.getcwd(), fldr_name)
        file_path = os.path.join(fldr_path, 'md_dataset.csv')
        ltst_post_id = cls_data_collection.get_latest_post_id(file_path)
        new_data = []
        timeline = mastodon.timeline_home(limit=100)
        for stats in timeline:
            post_date = stats['created_at']
            post_id = str(stats['id'])
            post_text = stats['content']
            user_name = stats['account']['display_name']
            if post_id > str(ltst_post_id):
                new_data.append((post_date, post_id, post_text, user_name))
        if new_data:
            cls_data_collection.appnd_data_csv(file_path, new_data)

    @staticmethod
    def gnrt_data(fldr_name):
        while True:
            cls_data_collection.crte_fldr(fldr_name)
            cls_data_collection.crt_csv_file(fldr_name)
            cls_data_collection.ftch_and_apnd_data(fldr_name)
            print('Data generated')
            time.sleep(2 * 60)

    @staticmethod
    def fn_gui_data_collection():
        canvas_gui_dc = gui_dc.Tk()
        canvas_gui_dc.geometry('700x700')
        canvas_gui_dc.title('Step 1: Data Collection')
        lbl_title = gui_dc.Label(canvas_gui_dc, text='Data Collection')
        lbl_title.place(x=300, y=50)
        lst_bx_posts_data = gui_dc.Text(canvas_gui_dc)
        lst_bx_posts_data.place(x=100, y=180)
        lst_bx_posts_data.configure(height=10, width=50)
        btn_ftch = gui_dc.Button(canvas_gui_dc, text='Fetch and Display Data',
                                  command=lambda: cls_data_collection.fn_dsply_data(lst_bx_posts_data))
        btn_ftch.place(x=90, y=120)
        btn_ftch.configure(height=1, width=25)
        btn_gnrte_ds = gui_dc.Button(canvas_gui_dc, text='Generate Data Set',
                                      command=lambda: threading.Thread(
                                          target=cls_data_collection.gnrt_data,
                                          args=("Mastodon dataset",),
                                          daemon=True
                                      ).start())
        btn_gnrte_ds.place(x=310, y=120)
        btn_gnrte_ds.configure(height=1, width=20)
        canvas_gui_dc.mainloop()