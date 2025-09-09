<h1>
	<p align="center">valorant_handedness</p>
</h1>

## Problem
While playing CSGO and now CS2, I got used to changing my handedness mid round in order to better hold angles. In CS2 there's a keybind for this, however in Valorant the only way to change handedness is by manually going through the settings everytime you want to do it. I wanted to automate this process to be as fast as I could, while also not breaking the TOS and without getting banned. [Demo](https://github.com/mortinso/valorant_handedness/#final-thoughts)

## Limitations by Riot
- Riot Vanguard (Riots anti-cheat) would likely be able to detect a DLL injection
- Riots official policy prohibits MACROs, so the only solution was a script (which to be honest is not that different)
- Not being able to inject the game with our own code, the script had to rely on Valorants GUI
- Riot Vanguard blocks mouse clicks from being emulated

## Solution
Since Riot Vanguard is so restrictive (and I didn't wanna get banned) what I could do to optimize changing my in-game handedness was pretty limited, but this is the result:
- The user opens Valorant and runs the script `python valorant_handedness.py` (The script quits when Valorant isn't running)
- The user joins a match and sets the `esc` menu to the right section
- When the user wants to change handedness, they press the keybind and click the mouse (It might take a bit to get used to the timing)

> [!IMPORTANT]
> The setting should be flush with the bottom of the scroll bar
> <img width="920" height="205" alt="Setting position2" src="https://github.com/user-attachments/assets/dbd4afda-6486-42d0-9ff2-1eeee749c40e" />

### Requirements
- python
- Windows

### Keybinds
Keybinds can be changed but the default are:
- `H` - Change handedness
- `L` - Quit the program

### Stuff I tried but didn't work
- Using Windows Mouse Keys to bind left click to numpad5. Riot ignores Windows Mouse Keys.
- Listening for `mouse.is_pressed()` after the cursor is moved to the right position. Listening for mouse clicks for some reason causes Valorant to ignore the mouse click we're detecting.
- Having the script close if Valorant wasn't running, caused the script to be significantly slower.

### Issues and possible fixes
Since it's such a basic script, it has a lot of limitations.
- It assumes the handedness is initially set to right hand: Could be fixed by reading the screen but that would be slower than assuming
- If you mistime the click it gets out of sync
- All it can do is press keyboard keys and move the mouse, so navigating the menu or changing the setting autonomously aren't options
- It assumes the display is 1920x1080: Maybe a map of display sizes and their respective coordinates could be used to hard code more resolutions into the script.

## Final Thoughts
That's it! It takes about 0.5s to change the setting, which is not great, but not terrible given the limitations and definitely better than doing it by hand. The runtime does however affect how often it is actually useful though, as in certain situations someone could peek you while the setting is being changed.

https://github.com/user-attachments/assets/01637583-2874-4418-ae44-9c5e3a2b6a7e
> [!NOTE]
> The debug messages are only in the demo video, however you could add your own if you wanted.
