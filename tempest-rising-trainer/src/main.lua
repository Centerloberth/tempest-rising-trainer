local trainer = require("src.trainer")
local socket = require("socket")

local function main_loop()
    if not trainer.start() then
        return
    end
    
    print("Commands: god, ammo, speed, quit")
    
    while trainer.is_running() do
        socket.select(nil, nil, 0.1)
        
        trainer.update()
        
        local input = io.read()
        if input then
            input = input:lower()
            if input == "god" then
                trainer.toggle_feature("god_mode")
            elseif input == "ammo" then
                trainer.toggle_feature("unlimited_ammo")
            elseif input == "speed" then
                trainer.toggle_feature("speed_hack")
            elseif input == "quit" then
                trainer.stop()
            else
                print("Unknown command")
            end
        end
    end
end

main_loop()