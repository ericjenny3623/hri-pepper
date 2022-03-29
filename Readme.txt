export PYTHONPATH=${PYTHONPATH}:~/Downloads/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages/



from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "128.237.247.249", 9559)
tts.say("Hi")
tts.say("Hello")
tts.say("Hi")
