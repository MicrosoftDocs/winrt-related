---
description: Specifies vertical columns that can contain text and images.
Search.Product: eADQiWindows 10XVcnh
title: subroup
keywords: windows 10, uwp, schema, toast notifications


ms.topic: reference
ms.date: 03/01/2022
---

# subgroup

Specifies vertical columns that can contain text and images.

## Element hierarchy

<dl>
<dt><a href="element-toast.md">&lt;toast&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-visual.md">&lt;visual&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-binding.md">&lt;binding&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-group.md">&lt;group&gt;</a></dt>
<dd><b>&lt;subgroup&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<subgroup>
  <!-- Child elements -->
  text*
  image*   
</subgroup>
```

### Key

`*`   optional (zero or one)

## Attributes and Elements


### Attributes

None.

### Child Elements

| Child Element | Description |
|---------------|-------------|
| [text](element-text.md) | Specifies text used in the toast template. |
| [image](element-image.md) | Specifies an image used in the toast template. |

### Parent Elements

| Parent Element | Description |
|----------------|-------------|
| [group](element-group.md) | Semantically identifies that the content in the group must either be displayed as a whole, or not displayed if it cannot fit. Groups also allow creating multiple columns. |


## See also

* [Toast content](/windows/apps/design/shell/tiles-and-notifications/adaptive-interactive-toasts)
* [Notifications Visualizer](/windows/apps/design/shell/tiles-and-notifications/notifications-visualizer)



 

 
