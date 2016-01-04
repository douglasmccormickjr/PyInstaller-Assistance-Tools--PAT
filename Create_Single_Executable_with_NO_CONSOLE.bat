@echo off
echo %~n1
echo %~dp1
set filename=%~n1
set filepath=%~dp1
set distname=ApplicationDistribution64bit\
set filedist=%filepath%%distname%
set filefina=%filedist%%filename%\
echo %filename%
echo %filepath%
echo %filedist%
echo %distname%
echo %filefina%

IF EXIST "%filedist%" goto KeepGoing
IF Not EXIST "%filedist%" goto CreateDirectory

:CreateDirectory
echo ++++ Creating NEW application distribution folder...
mkdir "%filedist%"
goto KeepGoing

:KeepGoing
cd "%filedist%"
echo ++++ Creating NEW application sub/version folder...
mkdir "%filename%"
cd "%filename%"
echo ++++ Creating .spec file now...
"pyi-makespec.exe" --onefile --noconsole "%1"
echo ++++ Creating FIXED spec file...
REM ping 192.0.2.2 -n 1 -w 10000 > nul
"pyi-fixspec.exe" %filefina%%filename%.spec "%1"
echo ++++ Creating final build file...
pyi-build.exe %filefina%%filename%.spec
echo ++++ Opening distribution output window
explorer /n, %filefina%
echo ++++ exiting now...
exit /b 0
