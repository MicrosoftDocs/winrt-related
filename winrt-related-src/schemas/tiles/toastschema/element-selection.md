---
description: Specifies the id and text of a selection item.
Search.Product: eADQiWindows 10XVcnh
title: selection
keywords: windows 10, uwp, schema, toast notifications
ms.topic: reference
ms.date: 03/01/2022
---

# selection

Specifies the id and text of a selection item.

## Element hierarchy

<dl>
<dt><a href="element-toast.md">&lt;toast&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-actions.md">&lt;actions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-input.md">&lt;input&gt;</a></dt>
<dd><b>&lt;selection&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<selection id = string
    content = string />
```



## Attributes and Elements


### Attributes

| Attribute | Description | Data type | Required | Default value |
|-----------|-------------|-----------|----------|---------------|
| id        | The id of the selection item. | string    | Yes      | None          |
| content      |  The content of the selection item. | string   | Yes      | None          |

### Child Elements

None

### Parent Elements

| Parent Element | Description |
|----------------|-------------|
| [input](element-input.md) | Specifies an input shown in a toast. |

## See also

[Toast content](/windows/apps/design/shell/tiles-and-notifications/adaptive-interactive-toasts)
[Notifications Visualizer](/windows/apps/design/shell/tiles-and-notifications/notifications-visualizer)

## Requirements

|          | Value |
|----------|--------------|
| **Namespace** | `http://schemas.microsoft.com/notifications/2012/toast.xsd` |

 

 
