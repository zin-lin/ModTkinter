# ModTkinter

An Extended Framework for `Tkinter/python`

ModTkinter is a technology which is based mainly on base64 decoding. After the double layer buffering of each `tcl/tk` widget, ModTkinter widgets will be rerendered with graphics as pixels...

Images are not use as normal images but pixels so that you can set any color you like as in `[R,G,B,A]` format...
`Would take no longer than 2 secs to load on a slow machine for nearly two hundred widgets on screen since
pixel data is formatted as an array...`

#### Requirements

     Windows OS
     1920*1080 (for better performances)
     Windows Xp or 10 (for better performances)


#### Installation
    
```python
>>>pip install ModTkinter
```

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
The best resolution in your Windows system will be obtained

"""
root.mainloop()
```

This will import the main class Tk(). This using the ctypes, will change `DPIAwareness` to fix the resolution to the highest resolution available on your machine...

##### AssistiveTouch

There are many examples. The most obvious one is the one on `Iphone`.

```python

import ModTkinter
from ModTkinter import AssistiveTouch, ModTk

root = Tk()
At = AssistiveTouch(master= root, text = "AT" )
root.mainloop()



```
`master` declaration is for the sake of the base app
with this one line of code you can access it.

In order to set the command, access through `At.camn['command']`
`camn` is the button part so you can do all the `tk.Button` configurations to it...


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

`40` is the width of the outline of the button or else is will be overflowed by the text like in `C#` and `Web`.
`20` here is the height.
`[10 , 10, 10, 230]` is the active color.

setting `animation = True` is to allow some bindings like entering will change the color to active color, leaving will maintain the original color...

configuration will be perform with `button.init()` again.

Since `<Enter>` and `<Leave>` bindings are used for animations, you can-

```python
button.enterbind = Your_Def_Enter
button.leavebind = Your_Def_Leave
#You dun even have to pass in event
#these will also be performed when leave and enter the button 
```

Others functionalities are as a normal button's.









