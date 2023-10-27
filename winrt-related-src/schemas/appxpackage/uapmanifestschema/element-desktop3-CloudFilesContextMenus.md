---
title: desktop3:CloudFilesContextMenus
description: Registration of a context menu for a cloud based placeholder file. 
ms.date: 10/10/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop3:CloudFilesContextMenus

Registration of a context menu for a cloud based placeholder file.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop3:Extension\>](element-desktop3-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop3:CloudFiles\>](element-desktop3-cloudfiles.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop3:CloudFilesContextMenu\>**

## Syntax

```xml
<desktop3:CloudFilesContextMenus>
    
  <!-- Child elements -->
  desktop3:Verb{0,10000} 
    
</desktop3:CloudFilesContextMenus>
```

### Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [desktop3:Verb](element-desktop3-verb.md) | Specifies the names of items in the File Explorer context menu for cloud based placeholder files. |

### Parent elements

| Parent element | Description |
|-|-|
| [desktop3:CloudFiles](element-desktop3-cloudfiles.md) | Registration for the handlers implemented in an application and context menu options for cloud based placeholder files. |

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/3` |
| **Minimum OS Version** | Windows 10 version 1709 (Build 16299) |
