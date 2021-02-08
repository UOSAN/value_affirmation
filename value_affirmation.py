#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on Fri Feb  5 15:28:23 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

rating_keys = ['5', '6', '7', '8', '9']


def convert_key_to_rating(run_number, key):
    rating = None
    if key in rating_keys:
        rating = int(key)
        if run_number != '0':
            rating = rating - 4

    return rating


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'value_affirmation'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '', 'run_number': '1'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/pnovak2/src/smoking/value_affirmation/value_affirmation.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[2560, 1440], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "setup"
setupClock = core.Clock()
conditions_file = 'conditions.csv'
instruction_text = 'Calibrating scanner'
if expInfo['run_number'] == '0':
    conditions_file = 'conditions_practice.csv'
    instruction_text = 'Instructions on how to perform task'


# Initialize components for Routine "introduction"
introductionClock = core.Clock()
introduction_text = visual.TextStim(win=win, name='introduction_text',
    text=instruction_text,
    font='Helvetica',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
value_message_text = visual.TextStim(win=win, name='value_message_text',
    text='default text',
    font='Helvetica',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rating_text = visual.TextStim(win=win, name='rating_text',
    text='How helpful is this message to help you quit smoking?',
    font='Helvetica',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
value_rating = visual.Slider(win=win, name='value_rating',
    size=(1.0, 0.025), pos=(0, -0.3), units=None,
    labels=['not at all','extremely'], ticks=(1, 2, 3, 4, 5),
    granularity=0, style=['triangleMarker'],
    color='LightGray', font='HelveticaBold',
    flip=False, depth=-3)
value_keyboard = keyboard.Keyboard()

# Initialize components for Routine "iti"
itiClock = core.Clock()
intertrial_interval = visual.ImageStim(
    win=win,
    name='intertrial_interval', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "end"
endClock = core.Clock()
end_text = visual.TextStim(win=win, name='end_text',
    text='Placeholder end text',
    font='Helvetica',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "setup"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
setupComponents = []
for thisComponent in setupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
setupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "setup"-------
while continueRoutine:
    # get current time
    t = setupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=setupClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setup"-------
for thisComponent in setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "introduction"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
introductionComponents = [introduction_text, key_resp]
for thisComponent in introductionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introductionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduction"-------
while continueRoutine:
    # get current time
    t = introductionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introductionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *introduction_text* updates
    if introduction_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introduction_text.frameNStart = frameN  # exact frame index
        introduction_text.tStart = t  # local t and not account for scr refresh
        introduction_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introduction_text, 'tStartRefresh')  # time at next scr refresh
        introduction_text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['apostrophe'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introductionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction"-------
for thisComponent in introductionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "introduction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(conditions_file),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    value_message_text.setText(message)
    value_rating.reset()
    value_keyboard.keys = []
    value_keyboard.rt = []
    _value_keyboard_allKeys = []
    # keep track of which components have finished
    trialComponents = [value_message_text, rating_text, value_rating, value_keyboard]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *value_message_text* updates
        if value_message_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            value_message_text.frameNStart = frameN  # exact frame index
            value_message_text.tStart = t  # local t and not account for scr refresh
            value_message_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(value_message_text, 'tStartRefresh')  # time at next scr refresh
            value_message_text.setAutoDraw(True)
        if value_message_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > value_message_text.tStartRefresh + 6.0-frameTolerance:
                # keep track of stop time/frame for later
                value_message_text.tStop = t  # not accounting for scr refresh
                value_message_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(value_message_text, 'tStopRefresh')  # time at next scr refresh
                value_message_text.setAutoDraw(False)
        
        # *rating_text* updates
        if rating_text.status == NOT_STARTED and tThisFlip >= 6.0-frameTolerance:
            # keep track of start time/frame for later
            rating_text.frameNStart = frameN  # exact frame index
            rating_text.tStart = t  # local t and not account for scr refresh
            rating_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating_text, 'tStartRefresh')  # time at next scr refresh
            rating_text.setAutoDraw(True)
        if rating_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rating_text.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                rating_text.tStop = t  # not accounting for scr refresh
                rating_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rating_text, 'tStopRefresh')  # time at next scr refresh
                rating_text.setAutoDraw(False)
        # Update marker position and slider rating
        # when there are keypresses of the rating buttons
        r = convert_key_to_rating(expInfo['run_number'], value_keyboard.keys)
        value_rating.markerPos = r
        # confirm rating by setting to current markerPos
        value_rating.rating = r
        
        
        # *value_rating* updates
        if value_rating.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
            # keep track of start time/frame for later
            value_rating.frameNStart = frameN  # exact frame index
            value_rating.tStart = t  # local t and not account for scr refresh
            value_rating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(value_rating, 'tStartRefresh')  # time at next scr refresh
            value_rating.setAutoDraw(True)
        if value_rating.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > value_rating.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                value_rating.tStop = t  # not accounting for scr refresh
                value_rating.frameNStop = frameN  # exact frame index
                win.timeOnFlip(value_rating, 'tStopRefresh')  # time at next scr refresh
                value_rating.setAutoDraw(False)
        
        # *value_keyboard* updates
        waitOnFlip = False
        if value_keyboard.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
            # keep track of start time/frame for later
            value_keyboard.frameNStart = frameN  # exact frame index
            value_keyboard.tStart = t  # local t and not account for scr refresh
            value_keyboard.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(value_keyboard, 'tStartRefresh')  # time at next scr refresh
            value_keyboard.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(value_keyboard.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(value_keyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if value_keyboard.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > value_keyboard.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                value_keyboard.tStop = t  # not accounting for scr refresh
                value_keyboard.frameNStop = frameN  # exact frame index
                win.timeOnFlip(value_keyboard, 'tStopRefresh')  # time at next scr refresh
                value_keyboard.status = FINISHED
        if value_keyboard.status == STARTED and not waitOnFlip:
            theseKeys = value_keyboard.getKeys(keyList=['5', '6', '7', '8', '9'], waitRelease=False)
            _value_keyboard_allKeys.extend(theseKeys)
            if len(_value_keyboard_allKeys):
                value_keyboard.keys = _value_keyboard_allKeys[-1].name  # just the last key pressed
                value_keyboard.rt = _value_keyboard_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('value_message_text.started', value_message_text.tStartRefresh)
    trials.addData('value_message_text.stopped', value_message_text.tStopRefresh)
    trials.addData('rating_text.started', rating_text.tStartRefresh)
    trials.addData('rating_text.stopped', rating_text.tStopRefresh)
    trials.addData('value_rating.response', value_rating.getRating())
    trials.addData('value_rating.rt', value_rating.getRT())
    trials.addData('value_rating.started', value_rating.tStartRefresh)
    trials.addData('value_rating.stopped', value_rating.tStopRefresh)
    # check responses
    if value_keyboard.keys in ['', [], None]:  # No response was made
        value_keyboard.keys = None
    trials.addData('value_keyboard.keys',value_keyboard.keys)
    if value_keyboard.keys != None:  # we had a response
        trials.addData('value_keyboard.rt', value_keyboard.rt)
    trials.addData('value_keyboard.started', value_keyboard.tStartRefresh)
    trials.addData('value_keyboard.stopped', value_keyboard.tStopRefresh)
    
    # ------Prepare to start Routine "iti"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    itiComponents = [intertrial_interval]
    for thisComponent in itiComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    itiClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "iti"-------
    while continueRoutine:
        # get current time
        t = itiClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=itiClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *intertrial_interval* updates
        if intertrial_interval.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            intertrial_interval.frameNStart = frameN  # exact frame index
            intertrial_interval.tStart = t  # local t and not account for scr refresh
            intertrial_interval.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(intertrial_interval, 'tStartRefresh')  # time at next scr refresh
            intertrial_interval.setAutoDraw(True)
        if intertrial_interval.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > intertrial_interval.tStartRefresh + iti-frameTolerance:
                # keep track of stop time/frame for later
                intertrial_interval.tStop = t  # not accounting for scr refresh
                intertrial_interval.frameNStop = frameN  # exact frame index
                win.timeOnFlip(intertrial_interval, 'tStopRefresh')  # time at next scr refresh
                intertrial_interval.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in itiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "iti"-------
    for thisComponent in itiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('intertrial_interval.started', intertrial_interval.tStartRefresh)
    trials.addData('intertrial_interval.stopped', intertrial_interval.tStopRefresh)
    # the Routine "iti" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(4.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [end_text]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_text* updates
    if end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text.frameNStart = frameN  # exact frame index
        end_text.tStart = t  # local t and not account for scr refresh
        end_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
        end_text.setAutoDraw(True)
    if end_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_text.tStartRefresh + 4.0-frameTolerance:
            # keep track of stop time/frame for later
            end_text.tStop = t  # not accounting for scr refresh
            end_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_text, 'tStopRefresh')  # time at next scr refresh
            end_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('end_text.started', end_text.tStartRefresh)
thisExp.addData('end_text.stopped', end_text.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
