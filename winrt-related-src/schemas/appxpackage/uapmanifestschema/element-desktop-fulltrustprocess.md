---
title: desktop:FullTrustProcess
description: Represents a desktop process that runs in full-trust.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, desktop:Extension, desktop:FullTrustProcess]
---

# desktop:FullTrustProcess

Represents a desktop process that runs in full-trust.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop:Extension>`](element-desktop-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop:FullTrustProcess>`**

## Syntax

```xml
<desktop:FullTrustProcess>

  <!-- Child elements -->
  desktop:ParameterGroup{0,1000}

</desktop:FullTrustProcess>
```

### Key

`{}` specific range of occurrences

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [desktop:ParameterGroup](element-desktop-parametergroup.md) | Represents a group of command-line parameters for a full-trust process. |

## Parent elements

| Parent element | Description |
|-|-|
| [desktop:Extension](element-desktop-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10` |
| **Minimum OS Version** | Windows 10 version 1607 (Build 14393) |

## Remarks

For more details, see [FullTrustProcessLauncher](/uwp/api/windows.applicationmodel.fulltrustprocesslauncher).

## Examples

<!-- Author content goes here -->
