
#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Using ALDialog Methods"""

import qi
import argparse
import sys
import os

from Tkinter import *
from ScrolledText import *



root = Tk()
root.title("Robot NAO")
content = Frame(root)
var = StringVar()

frame = ScrolledText(content, borderwidth=5, relief="sunken", width=30, height=10)
adresseIPLabel = Label(content, text="Adresse IP NAO")
IPtexteEntree = Entry(content, textvariable=var)

session = qi.Session()
ALDialog = None
topic_name = None

def quitter():
    try:
        global ALDialog
        global session
        global topic_name
        global root
        ALDialog.unsubscribe('my_dialog_example')
        # Deactivating the topic
        # Loading the topic given by the user (absolute path is required)
        ALDialog.deactivateTopic(topic_name)
        # now that the dialog engine is stopped and there are no more activated topics,
        # we can unload our topic and free the associated memory
        ALDialog.unloadTopic(topic_name)
        session.close()
        root.destroy()
        sys.exit()
    except RuntimeError:
        print ("\nCan't connect to Naoqi at IP {} (port {}).\nPlease check your script's arguments. Run with -h option for help.\n".format("192.168.43.232", 9559))
        root.destroy()
        sys.exit(1)


def report_callback_exception(self, exc, val, tb):
        showerror("Error", message=str(val))
        frame.insert(END,"\n"+"Impossible de se connecter avec cette IP \nEssayez d'appuyer sur le torse de nao pour obtenir son adresse IP")

def main():
    ip = var.get()
    frame.insert(END,"\n"+"Demarrage sur ip : "+ip)
    try:
        global session
        global ALDialog
        session.connect("tcp://{}:{}".format(str(ip), 9559))
        ALDialog = session.service("ALDialog")
    except RuntimeError:
        raise Exception("Impossible de se connecter")
        
    """
    This example uses ALDialog methods.
    It's a short dialog session with one topic.
    """
    # Getting the service ALDialog
    frame.insert(END,"\n"+"Chargement du dialogue")

    topic_path="/home/nao/dialog/interactive_dialog.top"
    # Loading the topic given by the user (absolute path is required)
    topf_path = topic_path.decode('utf-8')
    global topic_name
    topic_name = ALDialog.loadTopic(topf_path.encode('utf-8'))

    # Activating the loaded topic
    ALDialog.activateTopic(topic_name)

    # Starting the dialog engine - we need to type an arbitrary string as the identifier
    # We subscribe only ONCE, regardless of the number of topics we have activated
    ALDialog.subscribe('my_dialog_example')

content.grid(column=0, row=0, sticky=(N, S, E, W))
frame.grid(column=0, row=0, columnspan=1, rowspan=2, sticky=(N, S, E, W))
adresseIPLabel.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
IPtexteEntree.grid(column=3, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
boutonDemarrer = Button(content, text="Demarrer", command = lambda: main())
boutonArreter = Button(content, text="Arreter", command = lambda: quitter())
boutonDemarrer.grid(column=3, row=3)
boutonArreter.grid(column=4, row=3)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)

root.mainloop()
