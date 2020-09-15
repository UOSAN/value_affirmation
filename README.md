# Value affirmation task

## Introduction

The value affirmation task presents text stimuli, related to a participant's
values, to affect how people consider quitting smoking.
This task is used in the Rethink Smoking study.

- Conditions: Value that is important to the participant or not important
- Trial structure: Introduction text (4). Then text related to a value (4s),
then text "How helpful is this message to help you quit smoking?"
that requires a rating response (4s), then an intertrial interval (~3s),
repeated 64 times. 13s per trial.
- Duration: 64 trials = 832s total.

## How to run the task

The task is run using PsychoPy.

## Task description

The task consists of displaying text related to quitting smoking that involves
the participant's self-selected most important and least important values.
Introduction text is displayed for 4s. The introduction text is
```
Placeholder introduction text
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
Then there is a blank intertrial interval, jittered mean 3s.

The trials are repeated 64 times.

Then there is end text displayed for 4s. The end text is
```
Placeholder end text
```

## Developer documentation
Created using PsychoPy v2020.1.2
