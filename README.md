# Red-Arrow-Bot

This is a Discord Bot that I made for my own personal server and learning purposes. 

Commands and Features: 
        !help                   -- displays list of commands
        !clear_log              -- clears log file 
        !ping                   -- responds to channel with bot's latency to Discord 
        !giphy <subject>        -- responds to channel with gif relating to subject 
        !giphy_rand <subject>   -- responds to channel with a random gif relating to subject 
        !clear_messages         -- purges a text channel of all its messages
        !play <subject>         -- calls bot into current voice channel and plays a youtube audio
        !pause                  -- pauses bot's audio
        !resume                 -- resumes's bot's audio
        !stop                   -- stop's bot's audio and removes previous playing song
        !leave                  -- disconnect bot from the voice channel it's called from

> There is no queue system for the !play command
  > To play a next song, you should either !stop the current song(also removes current audio) or tell the bot to !leave and !play <subject>
> !giphy <subject> only returns a gif from the top result (number 1), which means multiple of the same command will return the same gif
> !clear_log is only intended for debugging purposes when I was creating this bot
