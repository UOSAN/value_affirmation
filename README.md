# Value affirmation task

## Introduction

The value affirmation task presents text stimuli, related to a participant's
values, to affect how people consider quitting smoking.
This task is used in the Rethink Smoking study.

- Conditions: The value that is important to the participant or and the value that is least important.
- Trial structure: Introduction text (4s). Then text related to a value (6s),
then text "How helpful is this message to help you quit smoking?"
that requires a rating response (4s), then an intertrial interval (~2s),
repeated 20 times. 12s per trial.
- Duration: 20 trials = 240s total.

## How to run the task

The task is run using PsychoPy. Fill in the participant identifier, the session number and the run number. Session 0 is a brief practice run, session 1 and 2 with runs 1, 2, 3 or 4 are in-scanner runs. The task will start automatically after that.

The task is intended to be run using [task_runner](https://github.com/UOSAN/task_runner).

## Task description

The task consists of displaying text related to quitting smoking that involves
the participant's self-selected most important and least important values.
Introduction text is displayed for 4s. The introduction text is
```
Calibrating scanner
```
Next text related to each value is presented for 6s.
Then the text "How helpful is this message to help you quit smoking?" is
displayed and a rating scale is also displayed (4s). The rating scale has five
possible responses on the scale, 1-5, with labels at the ends
```
1 = not at all
5 = extremely
```
The participant uses the 1, 2, 3, 4, or 5 buttons on the keyboard to respond.
Then there is a blank intertrial interval, jittered mean 2s.

The trials are repeated 20 times.

## Configuration

The task is configured by a CSV file that differs per participant, per session and per run: `VAFF_<participant_id>_Session<session>_Run<run>.csv`, i.e. `VAFF_ASH999_Session1_Run3.csv` for the third run of the first session for participant ASH999.
The CSV file must contain two columns: the message to be displayed (`message`)
and the duration in seconds of the inter-trial interval (`iti`).