import FreeSimpleGUI as sg

label = sg.Text ("Select a File to compress")

input1 = sg.Input ()

choose_button1 = sg.FileBrowse ('choose')

label2 = sg.Text ("Select destination file")

input2 = sg.Input ()

choose_button2 = sg.FileBrowse ('choose')

compress_button = sg.Button ('Compress')

window = sg.Window ('File compress', layout=[[label, input1, choose_button1],
                                             [label2, input2, choose_button2],
                                             [compress_button]])

window.read ()
window.close ()
