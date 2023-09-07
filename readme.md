# UI Testing using process json objects

## Parameters
--folder ./test_samples/tests --templates ./test_samples/templates  --auto-open --server http://localhost --debug

## Chrome drivers
You need to make sure that you have a folder in the root of the project called "chrome".
In that folder you need two things.
1. copy of the chrome driver 
2. copy of the chrome binary

You can download both at:
https://googlechromelabs.github.io/chrome-for-testing/#stable
Make sure you download both as win64 for "Version: 116.0.5845.96 (r1160321)"

The ui_testing_process/chrome folder should now contain the chrome exe and supporting files along with the chromedriver exe.