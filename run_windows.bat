@echo off
REM Get the Anaconda installation directory from the USERPROFILE environment variable
SET "ANACONDA_PATH=%USERPROFILE%\anaconda3"

REM Activate the Anaconda environment
CALL "%ANACONDA_PATH%\Scripts\activate.bat" audio2sub

REM Run the Streamlit WebUI
streamlit run "%USERPROFILE%\audio2sub\app.py"

REM Keep the console open after execution
pause
