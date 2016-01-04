# PyInstaller-Assistance-Tools--PAT
"...an easier way to compile your python application with PyInstaller..."

###why?###
This whole thing came from my struggles with creating an all-in-one-shot method to create a standalone/single application within PyInstaller...ok here goes...link to SO answer I wrote too:

###but there's other compilers in the wild, right?###
**Might I suggest using PyInstaller instead of py2exe** (since PyInstaller does a far better job in terms of bundling a single executable).  I'm on Windows about 90% of the time (no complaints here) with my python coding-- PyInstaller is a way better option than py2exe (for me at least --  I've used/test a great deal of Win compilers in the past with varied success).  Maybe other people suffering compiling issues could benefit from this method as well. 

###PyInstaller Prerequisites:###

 1. **Install PyInstaller** from: http://www.pyinstaller.org/
 2. After PyInstaller installation-- confirm both "pyi-makespec.exe" and "pyi-build.exe" are in the "C:\Python##\Scripts" directory on your machine
 3. **Download my PyInstaller-Assitance-Tools--PAT** (it's just 2 batch files and 1 executable with the executable's source python file too -- for the paranoid)...The file are listed above:
 * Create_Single_Executable_with_NO_CONSOLE.bat
 * Create_Single_Executable_with_CONSOLE.bat
 * pyi-fixspec.exe
 * pyi-fixpec.py (optional -- this is the source file for the executable)

Place the exectuable file called "pyi-fixspec.exe" inside the previous "Scripts" folder I mentioned above...this makes compiling much easier in the long run!

Ok, now onto the slight "coding" changes in your file...Here is what to do:

###let's get it working now...###

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

(2) Goto the directory containing the 2 batch files mentioned above and type in either:

   C:\MyComputer\Downloads\PAT> Create_Single_Executable_with_NO_CONSOLE.bat C:\Path\to\the\python\file.py
(ouput exe file results in a GUI app when double clicked)

or the other option...
   
   C:\MyComputer\Downloads\PAT> Create_Single_Executable_with_CONSOLE.bat C:\Path\to\the\python\file.py
(ouput exe file results in a WINDOWS CONSOLE app when double clicked -- expects commandline activity ONLY)

(3) Your new single-file-executable is done! Check this location:

    C:\Original\Directory\ApplicationDistribution64bit\NameOfPythonFile\dist

If you do edit/change the original python file that has just been previously compiled, please delete the folder/contents of **\NameOfPythonFile\** prior to next compile kickoff (you'll want to delete the historical/artifact files) 


(4) Coffee break -- if you wany to edit/add ICONS to the executable (and other items too), please look at the generated ".spec" file and PyInstaller documentation for configuration details.  You'll just need to kick off this again in the windows console:

    pyi-build.exe C:\path\to\the\file.spec

###future stuff###
* I'll add my "right-click-to-compile" option/application
* add a feature within python file to referrence icons (so you don't need to manually edit/touch the .spec file
* I'll be back to tinker with this later.


Enjoy!
-Doug Jr.

