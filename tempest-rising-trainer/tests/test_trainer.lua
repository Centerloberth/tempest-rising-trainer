local trainer = require("src.trainer")

local function test_toggle()
    local result = trainer.toggle_feature("god_mode")
    assert(result == true, "Toggle god_mode should return true")
    print("PASS: toggle_feature works")
end

local function test_invalid_feature()
    local result = trainer.toggle_feature("nonexistent")
    assert(result == false, "Invalid feature should return false")
    print("PASS: invalid feature handled")
end

local function test_is_running()
    assert(trainer.is_running() == false, "Should not be running initially")
    print("PASS: initial state is stopped")
end

local function test_start_stop()
    local started = trainer.start()
    assert(started == false, "Start should fail without game process")
    print("PASS: start fails gracefully")
    
    trainer.stop()
    assert(trainer.is_running() == false, "Should be stopped after stop()")
    print("PASS: stop works correctly")
end

test_toggle()
test_invalid_feature()
test_is_running()
test_start_stop()

print("\nAll tests passed!")