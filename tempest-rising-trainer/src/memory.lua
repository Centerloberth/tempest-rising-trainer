local memory = {}
local ffi = require("ffi")

ffi.cdef[[
    void* GetModuleHandleA(const char* lpModuleName);
    uintptr_t GetProcAddress(void* hModule, const char* lpProcName);
    bool WriteProcessMemory(void* hProcess, void* lpBaseAddress, void* lpBuffer, size_t nSize, size_t* lpNumberOfBytesWritten);
    bool ReadProcessMemory(void* hProcess, void* lpBaseAddress, void* lpBuffer, size_t nSize, size_t* lpNumberOfBytesRead);
    void* OpenProcess(uint32_t dwDesiredAccess, bool bInheritHandle, uint32_t dwProcessId);
    bool CloseHandle(void* hObject);
    uint32_t GetCurrentProcessId();
]]

function memory.open_game_process()
    local pid = ffi.C.GetCurrentProcessId()
    local handle = ffi.C.OpenProcess(0x1F0FFF, false, pid)
    return handle
end

function memory.write_uint32(handle, address, value)
    local buf = ffi.new("uint32_t[1]", value)
    local written = ffi.new("size_t[1]")
    return ffi.C.WriteProcessMemory(handle, ffi.cast("void*", address), buf, 4, written)
end

function memory.read_uint32(handle, address)
    local buf = ffi.new("uint32_t[1]")
    local read = ffi.new("size_t[1]")
    ffi.C.ReadProcessMemory(handle, ffi.cast("void*", address), buf, 4, read)
    return buf[0]
end

function memory.close_handle(handle)
    if handle then
        ffi.C.CloseHandle(handle)
    end
end

return memory