local UIBase = import('UI/UIBase')
---@type UILogin
local UILogin = {}
extends(UILogin, UIBase)
local  primitiveType=CS.UnityEngine.PrimitiveType

-- create a ui instance
function UILogin.New(controller)
    local newUI = new(UILogin)
    newUI.Controller = controller
    return newUI
end

function UILogin:OnInit(controller)
    Log.Info('UILogin OnInit, do controls binding')
    Tools.SetButton(self.btnLogin, self.OnLoginBtnClick)
end

function UILogin:OnOpen()
    Log.Info('UILogin OnOpen, do your logic')
end

function UILogin:OnLoginBtnClick()
    Log.Info("fuck login")
    SceneLoader.Load("Scene/Scene101/Scene101", function(success)
        --@type GameObject
        local go = GameObject.CreatePrimitive(primitiveType.Cube)
        go.name="test Cube"
        LuaBehaviour.Create(go, "Behaviour/TestLuaBehaviour")
    end)
end

return UILogin
