---
title: com5:InProcessHandler
description: Registers an in-process handler with one or many class registrations. (in com5:ComServer)
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
no-loc: [Package, Applications, Application, Extensions, com5:Extension, com5:ComServer, com5:InProcessHandler]
---

# com5:InProcessHandler

Registers an in-process handler with one or many class registrations. This schema introduces some minor changes in syntactic validation from the com4 schema.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com5:Extension>`](element-com4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com5:ComServer>`](element-com4-comserver.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com5:InProcessHandler>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com5:Extension>`](element-com4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<com5:ComServer>`](element-com4-comserver.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<com5:InProcessHandler>`**

## Syntax

```xml
<com5:InProcessHandler
  Path = 'An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.' >

  <!-- Child elements -->
  com5:Class{0,4000}
  com5:InProcessHandlerDll{0,4000}
  com5:ClassReference{0,4000}

</com5:InProcessHandler>
```

### Key

`{}` specific range of occurrences

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Path** |  The full path to the in-process handler DLL.  | An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |  |

## Child elements

| Child element | Description |
|-|-|
| [com5:Class](element-com5-inprocesshandler-class.md) | Defines an in-process handler class registration. |
| [com5:InProcessHandlerDll](element-com5-inprocesshandlerdll.md) | Specifies the path and processor architecture of an in-process handler DLL. |
| [com5:ClassReference](element-com5-inprocesshandler-classreference.md) | Specifies the class with which the registered in-process handler is associated and sets registration details. |

## Parent elements

| Parent element | Description |
|-|-|
| [com4:ComServer](element-com4-comserver.md) | Declares a package extension point of type windows.comServer. The comServer extension may include class registrations, including activation details for the servers that implement these classes, and ProgId and TreatAsClass registrations, which provide additional identifiers used to reference these classes at runtime. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/com/windows10/5` |
| **Minimum OS Version** | Windows 11 version 21H2 (Build 22000) |

## Remarks

In a change from [com4:InProcessHandler](element-com4-inprocesshandler.md), the **Path** attribute does not require that the supplied value end in ".dll".

## Examples

<!-- Author content goes here -->
