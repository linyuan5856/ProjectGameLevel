
local UIBase = import('UI/UIBase')
---@type UILogin
local UILogin = {}
extends(UILogin, UIBase)

-- create a ui instance
function UILogin.New(controller)
    local newUI = new(UILogin)
    newUI.Controller = controller
    return newUI
end

function UILogin:OnInit(controller)
    Log.Info('UILogin OnInit, do controls binding')
    Tools.SetButton(self.btnLogin,function()
        Log.Info("fuck login")
    end )
end

function UILogin:OnOpen()
    Log.Info('UILogin OnOpen, do your logic')
end

return UILogin
