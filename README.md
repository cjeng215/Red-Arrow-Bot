# Red-Arrow-Bot

This is a Discord Bot that I made for my own personal server and learning purposes. 

Commands and Features: <br />
        !help                   -- displays list of commands <br />
        !clear_log              -- clears log file <br />
        !ping                   -- responds to channel with bot's latency to Discord <br />
        !giphy <subject>        -- responds to channel with gif relating to subject <br />
        !giphy_rand <subject>   -- responds to channel with a random gif relating to subject <br />
        !clear_messages         -- purges a text channel of all its messages <br />
        !play <subject>         -- calls bot into current voice channel and plays a youtube audio<br />
        !pause                  -- pauses bot's audio<br />
        !resume                 -- resumes's bot's audio<br />
        !stop                   -- stop's bot's audio and removes previous playing song<br />
        !leave                  -- disconnect bot from the voice channel it's called from<br />

- There is no queue system for the !play command<br />
- To play a next song, you should either !stop the current song(also removes current audio) or tell the bot to !leave and !play <subject><br />
- !giphy <subject> only returns a gif from the top result (number 1), which means multiple of the same command will return the same gif<br />
- !clear_log is only intended for debugging purposes when I was creating this bot<br />
