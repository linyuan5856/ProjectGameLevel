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
    Tools.SetButton(self.btnLogin, self.OnLoginBtnClick)
end

function UILogin:OnOpen()
    Log.Info('UILogin OnOpen, do your logic')
end

function UILogin:OnLoginBtnClick()
    Log.Info("fuck login")
    SceneLoader.Load("Scene/Scene101/Scene101", function(success)

        AssetBundleLoader.Load("Prefab/Character/CharacterDwarf",function(isOk,ab)
            if isOk and ab then
                ---@type GameObject
                local asset = ab:LoadAsset("CharacterDwarf");
                local prefab = Object.Instantiate(asset)
                LuaBehaviour.Create(prefab , "Behaviour/TestLuaBehaviour")
            end
            UIModule.Instance:CloseWindow("UILogin")
        end,LoaderMode.Async)
    end)
end

return UILogin
