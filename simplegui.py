#!/usr/bin python3
# -*- coding: utf-8 -*-
# before use, you need to do 'pip3 install pysimplegui'

import PySimpleGUI as sg

sg.theme('Default1')

layout = [  [sg.Text('raw1 raw1 raw1 ')],
            [sg.Text('raw2 INPUT SOME TEXTS'), sg.InputText()],
            [sg.Button('OK'), sg.Button('CANCEL')] ]

window = sg.Window('SAMPLE TEST SAMPLE TEST', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'CANCEL':
        break
    elif event == 'OK':
        print('YOUR INPUT： ', values[0])

window.close()

