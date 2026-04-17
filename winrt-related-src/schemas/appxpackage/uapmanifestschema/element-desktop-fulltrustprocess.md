---
title: desktop:FullTrustProcess
description: Represents a desktop process that runs in full-trust.
ms.date: 05/10/2021
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
no-loc: [Package, Applications, Application, Extensions, Desktop:Extension, Desktop:FullTrustProcess]
---

# desktop:FullTrustProcess

Represents a desktop process that runs in full-trust.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-1-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Desktop:Extension>`](element-desktop-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<Desktop:FullTrustProcess>`**  

## Syntax

```xml
<desktop:FullTrustProcess >

  <!-- Child elements -->
  ParameterGroup{0,1000}

</desktop:FullTrustProcess>
```

### Key

`{}` specific range of occurrences

## Attributes and elements

### Attributes

None

### Child elements

| Child element | Description |
|-|-|
| [ParameterGroup](element-desktop-parametergroup.md) | Defines a group of command line parameters for the process. |

### Parent elements

| Parent element | Description |
|-|-|
| [desktop:Extension](element-desktop-extension.md) | Declares an extensibility point for the app. |

## Remarks

For more details, see [FullTrustProcessLauncher](/uwp/api/windows.applicationmodel.fulltrustprocesslauncher).

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10` |
| **Minimum OS Version** | Windows 10 version 1607 (Build 14393) |
