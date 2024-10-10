---
title: com4:Readable
description: Specifies that an application can only read files. (com4:Readable)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:Readable

Specifies that an application can only read files.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com4:Class\>](element-com4-class.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com4:Conversion\>](element-com4-conversion.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com4:Readable\>**

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com4:Class\>](element-com4-class.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com4:Conversion\>](element-com4-conversion.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com4:Readable\>**

## Syntax

```xml
<com4:Readable>

  <!-- Child elements -->
  Format

</com4:Readable>
```

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [Format](element-com4-format.md) | Specifies the file format an application can read (convert from). |

### Parent elements

| Parent element | Description |
|-|-|
| [com4:Conversion](element-com4-conversion.md) | Specifies the formats an application can read and write. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/4` |
| **Minimum OS Version** | Windows 10 (Build 20348) |
