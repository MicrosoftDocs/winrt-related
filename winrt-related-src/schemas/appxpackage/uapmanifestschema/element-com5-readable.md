---
title: com5:Readable
description: Specifies that an application can only read files. (com5:Readable)
ms.date: 06/22/2023
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
no-loc: [Package, Applications, Application, Extensions, com4:Extension, com4:ComServer, com5:InProcessServer, com5:Class, com5:Conversion, com5:Readable, com5:InProcessHandler, com5:Class, com5:Conversion, com5:Readable, Extensions, com4:Extension, com4:ComServer, com5:InProcessServer, com5:Class, com5:Conversion, com5:Readable, com5:InProcessHandler, com5:Class, com5:Conversion, com5:Readable]
---

# com5:Readable



## Description

Specifies that an application can only read files.

## Element hierarchy

**[`<Package>`](element-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-1-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:Extension>`](element-com4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:ComServer>`](element-com4-comserver.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com5:InProcessServer>`](element-com5-inprocessserver.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com5:Class>`](element-com5-inprocessserver-class.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com5:Conversion>`](element-com5-conversion.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com5:Readable>`**  
&nbsp;&nbsp;&nbsp;└─ [`<com5:InProcessHandler>`](element-com5-inprocesshandler.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com5:Class>`](element-com5-inprocesshandler-class.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com5:Conversion>`](element-com5-conversion.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com5:Readable>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-1-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:Extension>`](element-com4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com4:ComServer>`](element-com4-comserver.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com5:InProcessServer>`](element-com5-inprocessserver.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com5:Class>`](element-com5-inprocessserver-class.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com5:Conversion>`](element-com5-conversion.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com5:Readable>`**  
&nbsp;&nbsp;&nbsp;└─ [`<com5:InProcessHandler>`](element-com5-inprocesshandler.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com5:Class>`](element-com5-inprocesshandler-class.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com5:Conversion>`](element-com5-conversion.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com5:Readable>`**  

## Syntax
```syntax
<com5:Readable>
<!-- Child elements -->
  Format
</com5:Readable>
```




## Child Elements

| Element | Description |
| -----------| -------------|
| [Format](element-com5-format.md) | Specifies the file format an application can read (convert from). |

## Parent elements

| Parent element | Description |
|-|-|
| [com5:Conversion](element-com5-conversion.md) | Specifies the formats an application can read and write. |

## Requirements
| Item | Value |
| ---------------| -------------------------------------------------------------|
| com5 | `http://schemas.microsoft.com/appx/manifest/com/windows10/5` |
| **Minimum OS Version** | Windows 11 version 21H2 (Build 22000) |
