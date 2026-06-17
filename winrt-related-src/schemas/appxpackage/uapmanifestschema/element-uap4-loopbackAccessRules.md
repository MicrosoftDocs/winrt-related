---
title: uap4:LoopbackAccessRules
description: Contains rules for a loopback filter that enables communication between an app and a service.
ms.date: 06/05/2026
ms.topic: reference
no-loc: [Package, Applications, Application, Extensions, uap4:Extension, uap4:LoopbackAccessRules]
keywords: windows 10, uwp, schema, manifest, desktop, extension
---

# uap4:LoopbackAccessRules

Contains rules for a loopback filter that enables communication between an app and a service.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap4:Extension>`](element-uap4-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap4:LoopbackAccessRules>`**

## Syntax

```xml
<uap4:LoopbackAccessRules>

  <!-- Child elements -->
  uap4:Rule{0,1000}

</uap4:LoopbackAccessRules>
```

### Key

`{}` specific range of occurrences

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [uap4:Rule](element-uap4-rule.md) | Defines rules for inbound and outbound loopback connections. |

## Parent elements

| Parent element | Description |
|-|-|
| [uap4:Extension](element-uap4-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/4` |
| **Minimum OS Version** | Windows 10 version 1703 (Build 15063) |

## Remarks

Loopback connections are supported only for TCP connections.

> [!NOTE]
> The UDP protocol is not supported.

## Examples

<!-- Author content goes here -->
