---
title: uap:SupportedFileTypes (in FileTypeAssociation)
description: Describes the uap:SupportedFileTypes element.
ms.date: 06/16/2026
ms.topic: reference
no-loc: [Package, Applications, Application, Extensions, uap:Extension, uap:FileTypeAssociation, uap:SupportedFileTypes]
---

# uap:SupportedFileTypes (in FileTypeAssociation)

Defines the file types associated with the app. They are unique per package and are case sensitive.

## Element hierarchy
**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:Extension>`](element-uap-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:FileTypeAssociation>`](element-uap-filetypeassociation.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap:SupportedFileTypes>`**  
## Syntax

```xml
<uap:SupportedFileTypes>

  <!-- Child elements -->
  uap:FileType{1,1000}
  uap:FileType{1,1000}

</uap:SupportedFileTypes>
```

### Key

`{}` specific range of occurrences

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [uap:FileType](element-uap-filetypeassociation-filetype.md) | A supported file type specified as its file type extension. |
| [uap10:FileType](element-uap10-filetype.md) | <!-- TODO: Add description --> |

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

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
