#PySimple examples (v 3.9)
#Tony Crewe
#Oct 2018 MacOs

import FreeSimpleGUI as sg
import os

#sg.ChangeLookAndFeel('BlueMono')
sg.SetOptions (background_color = 'LightBlue',
            element_background_color = 'LightBlue',
            text_element_background_color = 'LightBlue',
               font = ('Arial', 12, 'bold'),
               text_color = 'Blue',
               input_text_color ='Blue',
               button_color = ('Blue', 'White'))

#get pathname to current file

dirname, filename = os.path.split(os.path.abspath(__file__))
pathname = os.path.join(dirname , 'Names.txt' )

#Get data from file
names = [line.strip() for line in open(pathname)]
sorted_names = names[:]
sorted_names.sort()

tab1_layout =[[sg.Text('Linear Search demo', font =('Calibri', 14, 'bold'))],
        [sg.Listbox(values =[n for n in names], size = (15, 12),font = ('Calibri', 12), background_color ='White',key = '_display1_')],
         [sg.Text('_'*25,font = ('Calibri', 12))],
         [sg.Text('Enter name to search for:',font = ('Calibri', 14, 'bold'))],
         [sg.InputText(size = (15,1), key = '_linear_')],
          [sg.ReadButton('Linear Search', font = ('Calibri', 14, 'bold'), size = (11,1))]]

tab2_layout = [[sg.Text('Binary Search demo', font =('Calibri', 14, 'bold'))],
        [sg.Listbox(values =[n for n in sorted_names], size = (15, 12),font = ('Calibri', 12), background_color ='White',key = '_display2_')],
         [sg.Text('_'*25,font = ('Calibri', 12))],
         [sg.Text('Enter name to search for:',font = ('Calibri', 14, 'bold'))],
         [sg.InputText(size = (15,1), key = '_binary_')],
          [sg.ReadButton('Binary Search',font = ('Calibri', 14, 'bold'), size = (11,1))]]

layout = [
    [sg.TabGroup([[sg.Tab('Linear Search', tab1_layout),sg.Tab('Binary Search', tab2_layout)]])]]

window = sg.Window('Main Window').Layout(layout)

#Linear Search - no need for Ordered list
def linear_search():
    l = names[:]
    found = False
    for l in l:
        if l == value['_linear_']:             #Check each value
            found = True
            result = ['Linear search', l + ' found']
            window.FindElement('_display1_').Update(result)
            break
    if not found:
        result = [value['_linear_'], 'was not found']
        window.FindElement('_display1_').Update(result)

#Binary Search - only works for ordered lists
def binary_search():
    l = sorted_names
    lo = 0
    hi = len(l)-1
    found = False
    while lo <= hi:
        mid = (lo + hi) //2
        if l[mid] == value['_binary_']:
            found = True
            result = ['Binary search', l[mid] + ' found.']
            window.FindElement('_display2_').Update(result)
            break
        elif l[mid] < value['_binary_']:
            lo = mid + 1
        else:
            hi = mid - 1
    if not found:
        result = [value['_binary_'], 'was not found']
        window.FindElement('_display2_').Update(result)

while True:
    button, value = window.Read()
    if button is not None:
        if button == 'Linear Search':
            linear_search()
        if button == 'Binary Search':
            binary_search()
    else:
        break
