---
description: Specifies an input, either text box or selection menu, shown in a toast notification.
Search.Product: eADQiWindows 10XVcnh
title: input
keywords: windows 10, uwp, schema, toast notifications
ms.topic: reference
ms.date: 03/01/2022
---

# input

Specifies an input, either text box or selection menu, shown in a toast notification.

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
<input id = string
    type = "text" | "selection" 
    placeHolderContent? = string >
  <!-- Child elements -->
  selection{0,5}
</input>
```

### Key

`?`   optional (zero or one)
`{}`   specific range of occurrences

## Attributes and Elements


### Attributes

| Attribute | Description | Data type | Required | Default value |
|-----------|-------------|-----------|----------|---------------|
| id        | The ID associated with the input.  | string    | Yes      | None          |
| type      | The type of input. | string - This attribute can have one of the following values: "text", "selection"   | Yes      | None          |
| placeHolderContent | The placeholder displayed for text input. | string   | No      | None          |

### Child Elements

| Child Element | Description |
|---------------|-------------|
| [selection](element-selection.md) | Specifies the id and text of a selection item. |

### Parent Elements

| Parent Element | Description |
|----------------|-------------|
| [actions](element-actions.md) | Container element for declaring up to five inputs and up to five button actions for the toast notification. |

## See also

[Toast content](/windows/apps/design/shell/tiles-and-notifications/adaptive-interactive-toasts)
[Notifications Visualizer](/windows/apps/design/shell/tiles-and-notifications/notifications-visualizer)

## Requirements

|          | Value |
|----------|--------------|
| **Namespace** | `http://schemas.microsoft.com/notifications/2012/toast.xsd` |

 

 
