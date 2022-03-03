---
description: Specifies a button shown in a toast.
Search.Product: eADQiWindows 10XVcnh
title: action
keywords: windows 10, uwp, schema, toast notifications
ms.topic: reference
ms.date: 03/01/2022
---

# action

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
    placement = TBD
    imageUri = TBD
    hint-inputid = TBD
    hint-buttonStyle = TBD
    hint-toolTip = TBD
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
| activationType | Decides the type of activation that will be used when the user interacts with a specific action. <ul>"foreground" - Default value. Your foreground app is launched.<li></li><li>"background" - Your corresponding background task is triggered, and you can execute code in the background without interrupting the user.</li><li>"protocol" - Launch a different app using protocol activation.</li></ul> | string | No | "foreground" |
| placement | TBD | string | No | None |
| imageUri | TBD | string | No | None |
| hint-inputId | TBD | string | No | None |
| hint-buttonStyle | TBD | string | No | None |
| hint-toolTip | TBD | string | No | None |

### Child Elements

None

### Parent Elements

| Parent Element | Description |
|----------------|-------------|
| [actions](element-actions.md) | Container element for declaring up to five inputs and up to five button actions for the toast notification. |

## See also

[Toast content](/windows/apps/design/shell/tiles-and-notifications/adaptive-interactive-toasts)
[Notifications Visualizer](windows/apps/design/shell/tiles-and-notifications/notifications-visualizer)


## Requirements

|          | Value |
|----------|--------------|
| **Namespace** | `http://schemas.microsoft.com/notifications/2012/toast.xsd` |

 

 
