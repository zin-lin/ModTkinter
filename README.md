# ModTkinter

An Extended Framework for Tkinter/python 

ModTkinter is a technology which is based mainly on base64 decoding. After the double layer buffering of each tcl/tk widget, ModTkinter widgets will be rerendered with graphics as pixels...

Images are not use as normal images but pixels so that you can set any color you like as in [R,G,B,A] format...

#### Requirements

     Windows OS


#### Installation
    

    pip install ModTkinter
    

#### Usage
###### Importing
```python
import ModTkinter
from ModTkinter import *
```
This will import All widgets and Functions from the packages

###### MainClass
```python
import ModTkinter
from ModTkinter import ModTk

    
root = ModTk()
"""
ModTk instead of Tk will fix resolution 
The best resolution in your Windows system will be obtain

"""
root.mainloop()
```

This will import the main class Tk(). This using the ctypes, will change `DPIAwareness` to fix the resolution to the highest resolution available on your machine...


###### Button new Functions

```python

import ModTkinter
from ModTkinter import Button, ModTk

root = Tk()
button = Button(root, text = "Button" )
button.init()
button.pack()


root.mainloop()

```
This will render the image layer automatically over the Tk button, then adjust the background and border itself.

```python
button.init([0, 106, 255, opacity])
```
There you can pass any color. Opacity will range from `0-255`
```python
button.init([0, 106, 255, 255], 40, 20, [10 , 10, 10, 230], animation= True)
```

`40` is the width of the outline of the button or else is will be overflowed like in `C#`.
`20` here is the height.
`[10 , 10, 10, 230]` is the active color.

setting `animation = True` is to allow some bindings like entering will change the color to active color, leaving will maintain the original color...

configuration will be perform with `button.init()` again.

Since `<Enter>` and `<Leave>` bindings are used for animations, you can-

```python
button.enterbind = Your_Def
#You dun even have to pass in event
```












