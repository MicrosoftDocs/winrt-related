---
title: uap:InfoTip
description: Defines a string that provides additional info to the user about the file type (Windows 10).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Applications, Application, Extensions, uap:Extension, uap:FileTypeAssociation, uap:InfoTip]
---

# uap:InfoTip

Defines a string that provides additional info to the user about the file type.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:Extension>`](element-uap-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:FileTypeAssociation>`](element-uap-filetypeassociation.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap:InfoTip>`**  

## Syntax

```xml
<uap:InfoTip>
    <!-- TODO: Add value description -->
</uap:InfoTip>
```

## Value

A string with a value between 1 and 1024 characters in length.

## Attributes

None.

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap:FileTypeAssociation](element-uap-filetypeassociation.md) | Declares an app extensibility point of type **windows.fileTypeAssociation**. A file type association indicates that the app is registered to handle files of the specified types. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |

## Remarks

This string is localizable.

## Examples

<!-- Author content goes here -->
