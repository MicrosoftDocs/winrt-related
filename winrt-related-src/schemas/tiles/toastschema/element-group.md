---
description: Semantically identifies that the content in the group must either be displayed as a whole, or not displayed if it cannot fit. Groups also allow creating multiple columns.
Search.Product: eADQiWindows 10XVcnh
title: group
keywords: windows 10, uwp, schema, toast notifications


ms.topic: reference
ms.date: 03/01/2022
---

# group

Semantically identifies that the content in the group must either be displayed as a whole, or not displayed if it cannot fit. Groups also allow creating multiple columns.

## Element hierarchy


<dl>
<dt><a href="element-toast.md">&lt;toast&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-visual.md">&lt;visual&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-binding.md">&lt;binding&gt;</a></dt>
<dd><b>&lt;group&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<group>

  <!-- Child elements -->
  subgroup* 
</group>
```

### Key

`*`   optional (zero or one)

## Attributes and Elements


### Attributes

None.

### Child Elements

| Child Element | Description |
|---------------|-------------|
| [subgroup](element-subgroup.md) | Specifies vertical columns that can contain text and images. |


### Parent Elements

| Parent Element | Description |
|----------------|-------------|
| [binding](element-binding.md) | Specifies the toast template.  |


## See also

* [Toast content](/windows/apps/design/shell/tiles-and-notifications/adaptive-interactive-toasts)
* [Notifications Visualizer](/windows/apps/design/shell/tiles-and-notifications/notifications-visualizer)




 

 
