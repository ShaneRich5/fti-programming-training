@ECHO off

IF %cd:~0,3% == C:\ (
    CALL C:/Miniconda3/Scripts/activate.bat C:/Miniconda3
) ELSE (
    CALL D:/Miniconda3/Scripts/activate.bat D:/Miniconda3
)

CALL conda env create -f pdt-env.yml
CALL activate pdt-env
CALL where python
PAUSE
