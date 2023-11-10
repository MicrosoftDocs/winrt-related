---
title: cloudFiles:CloudFilesContextMenus
description: Registration of a context menu for a cloud based placeholder file. (cloudFiles:CloudFilesContextMenus)
ms.date: 01/27/2023
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# cloudFiles:CloudFilesContextMenus

Registration of a context menu for a cloud based placeholder file.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<cloudFiles:Extension\>](element-cloudfiles-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<cloudFiles:CloudFiles\>](element-cloudfiles-cloudfiles.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<cloudFiles:CloudFilesContextMenu\>**

## Syntax

```xml
<cloudFiles:CloudFilesContextMenus>
    
  <!-- Child elements -->
  cloudFiles:Verb{0,10000} 
    
</cloudFiles:CloudFilesContextMenus>
```

### Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [cloudFiles:Verb](element-cloudfiles-verb.md) | Specifies the names of items in the File Explorer context menu for cloud based placeholder files. |

### Parent elements

| Parent element | Description |
|-|-|
| [cloudFiles:CloudFiles](element-cloudfiles-cloudfiles.md) | Registration for the handlers implemented in an application and context menu options for cloud based placeholder files. |

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/cloudfiles/windows10` |
| **Minimum OS Version** | Windows 10 (Build 19645) |
