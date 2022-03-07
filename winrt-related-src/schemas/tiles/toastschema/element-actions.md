---
description: Container element for declaring up to five inputs and up to five button actions for the toast notification.
Search.Product: eADQiWindows 10XVcnh
title: actions
keywords: windows 10, uwp, schema, toast notifications


ms.topic: reference
ms.date: 03/01/2022
---

# actions (Toast XML Schema)

Container element for declaring up to five inputs and up to five button actions for the toast notification.

## Element hierarchy

<dl>
<dt><a href="element-toast.md">&lt;toast&gt;</a></dt>
<dd><b>&lt;actions&gt;</b></dd>
</dl>

## Syntax

``` syntax
<actions>

  <!-- Child elements -->
  input{0,5}
  action{0,5}   
</actions>
```

### Key

`{}`   specific range of occurrences

## Attributes and Elements


### Attributes

None.

### Child Elements

| Child Element | Description |
|---------------|-------------|
| [input](element-input.md) | Specifies an input shown in a toast. |
| [action](element-action.md) | Specifies a button shown in a toast. |

### Parent Elements

| Parent Element | Description |
|----------------|-------------|
| [toast](element-toast.md) | Base toast element, which contains at least a single [visual](element-visual.md) element. |


## See also

* [Toast content](/windows/apps/design/shell/tiles-and-notifications/adaptive-interactive-toasts)
* [Notifications Visualizer](/windows/apps/design/shell/tiles-and-notifications/notifications-visualizer)




 

 
