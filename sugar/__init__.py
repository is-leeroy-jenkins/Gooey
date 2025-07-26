'''
  ******************************************************************************************
      Assembly:                Gooey
      Filename:                init.py
      Author:                  Terry D. Eppler
      Created:                 05-31-2022

      Last Modified By:        Terry D. Eppler
      Last Modified On:        05-01-2025
  ******************************************************************************************
  <copyright file="init.py" company="Terry D. Eppler">

	     Boo is a df analysis tool integrating GenAI, Text Processing, and Machine-Learning
	     algorithms for federal analysts.
	     Copyright ©  2022  Terry Eppler

     Permission is hereby granted, free of charge, to any person obtaining a copy
     of this software and associated documentation files (the “Software”),
     to deal in the Software without restriction,
     including without limitation the rights to use,
     copy, modify, merge, publish, distribute, sublicense,
     and/or sell copies of the Software,
     and to permit persons to whom the Software is furnished to do so,
     subject to the following conditions:

     The above copyright notice and this permission notice shall be included in all
     copies or substantial portions of the Software.

     THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
     INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
     FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.
     IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
     DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
     ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
     DEALINGS IN THE SOFTWARE.

     You can contact me at:  terryeppler@gmail.com or eppler.terry@epa.gov

  </copyright>
  <summary>
    sugar.py
  </summary>
  ******************************************************************************************
  '''
from __future__ import annotations
import base64
from enum import Enum
import FreeSimpleGUI as sg
import fitz
from FreeSimpleGUI import Text, Frame, Sizegrip
from googlesearch import search
import random
import io
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasAgg
import matplotlib.figure
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import get_test_data
from matplotlib.ticker import NullFormatter
from mpl_toolkits.axes_grid1.axes_rgb import RGBAxes
import numpy as np
import os
from pandas import read_csv as CsvReader
from pandas import read_excel as ExcelReader
from pydantic import BaseModel
from PIL import Image, ImageTk, ImageSequence
from static import EXT, Client
from sys import exit, exc_info
from minion import App
import traceback
import urllib.request
import webbrowser
from typing import Dict, List, Tuple, Any, Text, Optional