---

ms.assetid: a0d13555-3408-4d8e-8ac9-223f7b31059f
title: desktop2:EventMessageFiles
description: Contains event message files.

ms.date: 04/05/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop2:EventMessageFiles

Contains event message files.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop2:Extension\>](element-desktop2-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop2:DesktopEventLogging\>](element-desktop2-desktopeventlogging.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop2:EventMessageFiles\>**

## Syntax

```xml
<desktop2:EventMessageFiles>

  <!-- Child elements -->
  desktop2:File{1,1000}

</desktop2:EventMessageFiles>
```

### Key

`{}` specific range of occurrences

## Attributes and elements

### Attributes

None.

### Child elements

| Child element | Description |
|-|-|
| [File](element-desktop2-file.md) | Specifies the path to an event message file. |

### Parent elements

| Parent element | Description |
|-|-|
| [desktop2:DesktopEventLogging](element-desktop2-desktopeventlogging.md) | Enables Windows Desktop Bridge apps to register for Windows event logging. |

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/2` |
| Minimum OS Version | Windows 10 version 1703 (Build 15063) |
