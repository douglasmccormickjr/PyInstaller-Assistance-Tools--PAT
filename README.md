# PyInstaller-Assistance-Tools--PAT
an easier way to compile your python application with pyinstaller

This whole thing came from my struggles with creating an all-in-one-shot method to create a standalone/single application within PyInstaller...ok here goes...will fix later

**Might I suggest using pyinstaller instead of py2exe** (since pyinstaller does a far better job in terms of bundling a single executable).  I'm on Windows about 90% of the time (no complaints here) with my python coding-- PyInstaller is a way better option than py2exe (for me at least --  I've used/test a great deal of Win compilers in the past with varied success).  Maybe other people suffering compiling issues could benefit from this method as well. 

PyInstaller Prerequisite: 

 1. Install PyInstaller from: http://www.pyinstaller.org/
 2. After PyInstaller installation-- confirm both "pyi-makespec.exe" and "pyi-build.exe" are in the "C:\Python<whatever-number>\Scripts" directory on your machine
 3. Download my PyInstaller-Assitance-Tools (it's just 2 batch files and 1 executable with the executable's source python file too -- for the paranoid)...Place the exe file called "pyi-fixspec.exe" inside the previous "Scripts" folder I mentioned above...this makes compiling much easier in the long run!

Ok, now onto the slight "coding" changes in your file...Here is what to do:

  1. **I use a standard function that references the location of applications/scripts** that my python application needs to utilize to work while being executed/operated.  This function operates both when the app is a standalone python script or when it's fully compiled via pyinstaller.

Here's the piece of code I use:

    def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

and here's my app using it....

    source = resource_path("data\\some_archive.zip")

(please note that the data/files/folders I'm bundling for my app are below the main executable/script that I'll be compiling...the "_MEIPASS" part in the function lets pyinstaller know that it's working as a compiled application)

(2) 
