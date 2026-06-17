---
title: desktop10:SupportedProtocols
description: Specifies the supported URL protocol schemes for the extension.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, desktop10:Extension, desktop10:AppExecutionAlias, desktop10:ExecutionAlias, desktop10:SupportedProtocols]
---

# desktop10:SupportedProtocols

Specifies the supported URL protocol schemes for the extension.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop10:Extension>`](element-desktop10-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop10:AppExecutionAlias>`**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop10:ExecutionAlias>`**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop10:SupportedProtocols>`**

## Syntax

```xml
<desktop10:SupportedProtocols>

  <!-- Child elements -->
  desktop10:SupportedProtocol{0,10000}

</desktop10:SupportedProtocols>
```

### Key

`{}` specific range of occurrences

## Attributes

None.

## Child elements

| Child element | Description |
|-|-|
| [desktop10:SupportedProtocol](element-desktop10-supportedprotocol.md) | Specifies a URL protocol scheme. |

## Parent elements

| Parent element | Description |
|-|-|
| [desktop:ExecutionAlias](element-desktop-executionalias.md) | The executable of a UWP app to be activated from a command prompt. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |
| **Minimum OS Version** | Windows 11 version 22H2 (Build 22621) |

## Remarks

The behavior of this element is comparable to setting supported protocols for unpackaged apps in the registry as described in [Application Registration](/windows/win32/shell/app-registration). The attributes and child elements from the desktop10 namespace are only supported on extension instances that specify CompatMode="classic" and are only supported on desktop SKUs.

## Examples

<!-- Author content goes here -->
