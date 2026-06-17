---
title: uap17:PackageExtensionHost
description: Declares an app extensibility point of type *windows.packageExtensionHost*. This element indicates which categories of extensions the package can host.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
no-loc: [Package, Applications, Application, Extensions, uap17:Extension, uap17:PackageExtensionHost]
---

# uap17:PackageExtensionHost

Declares an app extensibility point of type *windows.packageExtensionHost*. This element indicates which categories of extensions the package can host. Those category names are provided as child elements, of which at least one is required.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap17:Extension>`](element-uap17-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap17:PackageExtensionHost>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap17:Extension>`](element-uap17-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap17:PackageExtensionHost>`**  

## Syntax

```xml
<uap17:PackageExtensionHost>

  <!-- Child elements -->
  uap17:Name{1,unbounded}

</uap17:PackageExtensionHost>
```

### Key

`{}` specific range of occurrences

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [uap17:Name](element-uap17-name.md) | Specifies the name of an extension category that can be hosted by a [PackageExtensionHost](element-uap17-packageextensionhost.md). |

## Parent elements

| Parent element | Description |
|-|-|
| [uap17:Extension](element-uap17-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/17` |
| **Minimum OS Version** | <!-- TODO: Add minimum OS version --> |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
