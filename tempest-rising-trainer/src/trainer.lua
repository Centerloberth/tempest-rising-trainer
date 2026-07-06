local trainer = {}
local config = require("src.config")
local memory = require("src.memory")
local socket = require("socket")

local handle = nil
local running = false

function trainer.start()
    print("Tempest Rising Trainer v1.0")
    print("Connecting to game...")
    
    handle = memory.open_game_process()
    if not handle then
        print("Failed to open game process")
        return false
    end
    
    running = true
    print("Connected successfully")
    return true
end

function trainer.update()
    if not running then return end
    
    if config.features.god_mode.enabled then
        local addr = config.features.god_mode.address + config.features.god_mode.offset
        memory.write_uint32(handle, addr, config.features.god_mode.value)
    end
    
    if config.features.unlimited_ammo.enabled then
        local addr = config.features.unlimited_ammo.address + config.features.unlimited_ammo.offset
        memory.write_uint32(handle, addr, config.features.unlimited_ammo.value)
    end
    
    if config.features.speed_hack.enabled then
        local addr = config.features.speed_hack.address + config.features.speed_hack.offset
        local val = math.floor(config.features.speed_hack.value * 1000)
        memory.write_uint32(handle, addr, val)
    end
end

function trainer.toggle_feature(feature_name)
    if config.features[feature_name] then
        config.features[feature_name].enabled = not config.features[feature_name].enabled
        local status = config.features[feature_name].enabled and "enabled" or "disabled"
        print(feature_name .. " " .. status)
        return true
    end
    return false
end

function trainer.stop()
    running = false
    if handle then
        memory.close_handle(handle)
        handle = nil
    end
    print("Trainer stopped")
end

function trainer.is_running()
    return running
end

return trainer