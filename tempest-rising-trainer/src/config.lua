local config = {}

config.game = {
    process_name = "TempestRising.exe",
    base_address = 0x00400000,
    update_interval = 0.1
}

config.features = {
    god_mode = {
        enabled = false,
        address = 0x00F12340,
        offset = 0x4C,
        value = 9999
    },
    unlimited_ammo = {
        enabled = false,
        address = 0x00F12344,
        offset = 0x50,
        value = 100
    },
    speed_hack = {
        enabled = false,
        address = 0x00F12348,
        offset = 0x54,
        value = 2.0
    }
}

return config