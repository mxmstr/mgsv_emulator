Metal Gear Online 3 LAN server emulator
==========================

Based on unknown321's TPP server emulator, this server emulates just the basic functionality of Metal Gear Online 3 allowing you to join or host matches with other players on the same local network, completely offline.

You still need a legit copy of the latest Steam version of Metal Gear Solid V - The Phantom Pain to get this to work.

I made this emulator for enabling local split-screen multiplayer, and I don't plan to implement anything beyond the minimum necessary to accomplish just that. Here's how to set that up with Nucleus Co-op: https://www.youtube.com/watch?v=0mJo00FnXto

Update: The Nucleus Co-op script now uses a serverless version of the emulator which you can get here: https://github.com/mxmstr/NucleusGameFixes/releases/tag/MGSV

How to use
==========================
Download Docker Desktop for Windows and run it.

Download the latest server image in the Releases section, or build the Dockerfile yourself.

Open a command prompt window and run ```docker load -i mgo.tar```

Run the server with ```docker run -it --rm -p 80:80 --name mgo mgo```

Open mgsvmgo.exe in a hex editor, search for the string "https://mgstpp-game.konamionline.com/tppstm/gate" and replace it with http://127.0.0.1:80.

MGO should now connect to the local server.
