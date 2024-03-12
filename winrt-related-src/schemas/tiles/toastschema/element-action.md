---
description: Specifies a button shown in a toast.
Search.Product: eADQiWindows 10XVcnh
title: action
keywords: windows 10, uwp, schema, toast notifications
ms.topic: reference
ms.date: 03/01/2022
---

# action (Toast XML Schema)

Specifies a button shown in a toast.

## Element hierarchy

<dl>
<dt><a href="element-toast.md">&lt;toast&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-actions.md">&lt;actions&gt;</a></dt>
<dd><b>&lt;input&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<action content = string
    arguments = string
    activationType? = "foreground" | "background" | "protocol"
    afterActivationBehavior? = "default" | "pendingUpdate"
    placement? = "contextMenu"
    imageUri? = string
    hint-inputid = string
    hint-buttonStyle = "Success" | "Critical"
    hint-toolTip = string
/>
```

### Key

`?`   optional (zero or one)

## Attributes and Elements


### Attributes

| Attribute | Description | Data type | Required | Default value |
|-----------|-------------|-----------|----------|---------------|
| content   | The content displayed on the button. | string    | Yes      | None          |
| arguments   | App-defined string of arguments that the app will later receive if the user clicks this button. | string    | Yes      | None          |
| type      | An argument string that can be passed to the associated app to provide specifics about the action that it should execute in response to the user action.  | string   | Yes      | None          |
| activationType | Decides the type of activation that will be used when the user interacts with a specific action. <ul><li>"foreground" - Default value. Your foreground app is launched.</li><li>"background" - Your corresponding background task is triggered, and you can execute code in the background without interrupting the user.</li><li>"protocol" - Launch a different app using protocol activation.</li></ul> | string | No | "foreground" |
| afterActivationBehavior | Specifies the behavior that the toast should use when the user takes action on the toast. <ul><li>"default" - Default value. The toast will be dismissed when the user takes action on the toast.</li><li>"pendingUpdate" - 	After the user clicks a button on your toast, the notification will remain present, in a "pending update" visual state. You should immediately update your toast from a background task so that the user does not see this "pending update" visual state for too long.</li> | string | No | "default" | 
| placement | When set to "contextMenu", the action becomes a context menu action added to the toast notification's context menu rather than a traditional toast button. | string | No | None |
| imageUri | The URI of the image source for a toast button icon. These icons are white transparent 16x16 pixel images at 100% scaling and should have no padding included in the image itself. If you choose to provide icons on a toast notification, you must provide icons for ALL of your buttons in the notification, as it transforms the style of your buttons into icon buttons. Use one of the following protocol handlers: <ul><li>http:// or https:// - A web-based image.</li><li>ms-appx:/// - An image included in the app package.</li><li>ms-appdata:///local/ - An image saved to local storage.</li><li>file:/// - A local image. (Supported only for desktop apps. This protocol cannot be used by UWP apps.)</li></ul>| string | No | None |
| hint-inputId | Set to the Id of an [input](element-input.md) to position button beside the input.  | string | No | None |
| hint-buttonStyle | The button style. **useButtonStyle** must be set to true in the [toast](element-toast.md) element. <ul><li>"Success" - The button is green</li><li>"Critical" - The button is red.</li></ul> Note that these values are case-sensitive. | string | No | None |
| hint-toolTip | The tooltip for a button, if the button has an empty content string. | string | No | None |

### Child Elements

None

### Parent Elements

| Parent Element | Description |
|----------------|-------------|
| [actions](element-actions.md) | Container element for declaring up to five inputs and up to five button actions for the toast notification. |

## See also

* [Toast content](/windows/apps/design/shell/tiles-and-notifications/adaptive-interactive-toasts)
* [Notifications Visualizer](/windows/apps/design/shell/tiles-and-notifications/notifications-visualizer)



 

 
