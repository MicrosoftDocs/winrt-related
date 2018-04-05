---
author: laurenhughes
title: desktop4:DesktopIconOverlayHandlers
description: Contains Windows Shell icon overlay handlers for cloud based placeholder files.  
ms.author: lahugh
ms.date: 04/10/2018
ms.topic: reference
ms.prod: windows
ms.technology: winrt-reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop4:DesktopIconOverlayHandlers

## Description
Contains Windows Shell icon overlay handlers for cloud based placeholder files. 


## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop3-extension.md">&lt;desktop3:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop3-cloudfiles.md">&lt;desktop3:CloudFiles&gt;</a></dt>
<dd><b>&lt;desktop4:DesktopIconOverlayHandlers&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>


## Syntax
```syntax
<desktop4:DesktopIconOverlayHandlers>
    
  <!-- Child elements -->
  desktop4:DesktopIconOverlayHandler{0,10000} 
    
</desktop4:DesktopIconOverlayHandlers>
```

### Key
`{}`   specific range of occurrences

## Child Elements

| Child Element | Description |
|---------------|-------------|
| [desktop4:DesktopIconOverlayHandler](element-desktop4-desktopiconoverlayhandler.md) | Registration for a Windows Shell icon overlay handler. |

## See Also
[How to Register Icon Overlay Handlers](https://msdn.microsoft.com/library/windows/desktop/hh127455.aspx)

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/desktop/windows10/4</p></td>
</tr>
</tbody>
</table>