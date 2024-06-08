# Automating some of the Oneblock Vanilla Skyblock

This is a few python scripts that I wrote to help automate the initial grid of starting a vanilla Oneblock Skyblock world.

### So far you can:

- setup your display so python can control your computer
- take a backup of your world
- load that backup and repeatedly walk off the edge of the world in the hope of spawning a zombie with a shovel

## How to use:

1. Install the required packages:

```bash
pip install -r requirements.txt
```

2. Run the setup script to initialize your screen:

```bash
python initialize_screen.py
```

3. Run the backup script to take a backup of your world:

```bash
python backup_world.py
```

4. Run the load script to load the backup and walk off the edge of the world:

```bash
python autostart.py
```

## Notes:

I will clean this up later so that it is easier to use. Currently it is a bit of a mess and you will need to edit the scripts to get them to work for you.
