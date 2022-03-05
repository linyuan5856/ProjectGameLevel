Time = CS.UnityEngine.Time

local player = {}

function player:Awake(behaviour)
    ---@type UnityEngine.GameObject
    self.Root = behaviour.gameObject
    print("Test Lua Behaivour Awake!---->    ")
end

function player:Start()
    print("Test Lua Behaivour start!")
end

function player:Update()

    if Input.GetKeyDown(KeyCode.W) then
        local go = player.Root
        local old = go.transform.localScale
        go.transform.localScale = Vector3(old.x, old.y, old.z) * 2
    end

    if Time.frameCount % 100 == 0 then
        -- print("Test Lua Behaivour Update!")
    end
end

return player


