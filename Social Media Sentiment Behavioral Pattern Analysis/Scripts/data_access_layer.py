
from data_collection import cls_data_collection
from data_pre_processing import cls_data_pre_prcs
#from Scripts.Sentiment_analysis_clcik import cls_sentiment_analysis
from tkinter import messagebox


class cls_function_logic:

    # Step 1 : Data Colection
    @staticmethod
    def fn_data_ftch():
        cls_data_collection.fn_gui_data_collection()

    # Step 2 : Data Pre-Processing
    @staticmethod
    def fn_data_pre_prcsng():
        cls_data_pre_prcs.fn_gui_dpp()

    # *********************** Sentiment Analaysis button ***********************

    '''def fn_sa():
        cls_sentiment_analysis.fn_gui_sa()'''






