---
description: Specifies a custom header that groups multiple notifications together within Action Center.
Search.Product: eADQiWindows 10XVcnh
title: header
keywords: windows 10, uwp, schema, toast notifications


ms.topic: reference
ms.date: 03/01/2022
---

# header

Specifies a custom header that groups multiple notifications together within Action Center.

## Element hierarchy

<dl>
<dt><a href="element-toast.md">&lt;toast&gt;</a></dt>
<dd><b>&lt;header&gt;</b></dd>
</dl>

## Syntax

``` syntax
<header id = string
    title = string
    arguments = string 
    activationType? = "foreground" | "protocol"
    activationOptions? = string
/>
```

### Key

`?`   optional (zero or one)

## Attributes and Elements


### Attributes

| Attribute | Description | Data type | Required | Default value |
|-----------|-------------|-----------|----------|---------------|
| id   | A developer-created identifier that uniquely identifies this header. If two notifications have the same header id, they will be displayed underneath the same header in Action Center. | string    | Yes      | None          |
| title      | A title for the header.  | string   | Yes      | None          |
| arguments | A developer-defined string of arguments that is returned to the app when the user clicks this header. Cannot be null. | string | Yes | None |
| activationType | The type of activation this header will use when clicked. | string | No | "foreground" |
| activationOptions | Additional options relating to activation of the toast header. | Additional options relating to activation of the toast header. | No | None |

### Child Elements

None

### Parent Elements

| Parent Element | Description |
|----------------|-------------|
| [toast](element-toast.md) | Base toast element, which contains at least a single [visual](element-visual.md) element. |


## See also

* [Toast content](/windows/apps/design/shell/tiles-and-notifications/adaptive-interactive-toasts)
* [Notifications Visualizer](/windows/apps/design/shell/tiles-and-notifications/notifications-visualizer)



 

 
