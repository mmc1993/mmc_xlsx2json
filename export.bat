@echo off
set EXPORT_PATH=C:\Users\Administrator\Desktop\cfg\xlsx2json.py
set OUTPUT_PATH=C:\Users\Administrator\Desktop\cfg\export
set INPUT_PATH=C:\Users\Administrator\Desktop\cfg\xlsx
set CURRENT_PATH=%cd%
cd %INPUT_PATH%
for /r %%s in (,*) do (
    echo export %%s
    %EXPORT_PATH% %OUTPUT_PATH% "%%s"
)
cd %CURRENT_PATH%
pause