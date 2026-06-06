@echo off
if "%ANTLR_JAR%"=="" set ANTLR_JAR=antlr-4.13.2-complete.jar
if not exist "%ANTLR_JAR%" (
    echo Configure ANTLR_JAR ou coloque antlr-4.13.2-complete.jar na raiz do projeto.
    exit /b 1
)
java -jar "%ANTLR_JAR%" -Dlanguage=Python3 -visitor -o src/generated grammar/Compilador.g4
