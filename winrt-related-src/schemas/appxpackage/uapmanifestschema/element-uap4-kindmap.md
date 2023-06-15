---
ms.assetid: f2108ae9-972c-4b45-8ea0-db791ed08089
title: uap4:KindMap
description: Specifies what Kind is and how it's used.
ms.date: 04/05/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap4:KindMap

Specifies what Kind is and how it's used.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap4:Extension\>](element-uap4-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:FileTypeAssociation\>](element-uap-filetypeassociation.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap4:KindMap\>**

## Syntax

```xml
<uap4:KindMap>

  <!-- Child elements -->
  uap4:Kind{1,100}

</uap4:KindMap>
```

### Key

`{}` specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [Kind](element-uap4-kind.md) | Specifies the Kind value. |

### Parent elements

| Parent element | Description |
|-|-|
| [uap:FileTypeAssociation](element-uap-filetypeassociation.md) | Declares an app extensibility point of type *windows.fileTypeAssociation*. A file type association indicates that the app is registered to handle files of the specified types. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/4` |
