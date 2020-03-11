@echo off
set now_pth=%cd%
cd %~dp0
set path=%path%;%cd%\py_embed;%cd%\vcpm
cd %now_pth%
set vcpm_path=%~dp0
%~dp0\py_embed\python %vcpm_path%\vcpm\vcpm.py %1 %2 %3 %4 %5 %6 %7 %8 %9
@echo on