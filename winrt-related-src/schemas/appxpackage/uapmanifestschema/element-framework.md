---
description: Indicates whether the package is a framework package (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: Framework (Windows 10)
ms.assetid: 2a8e1c58-b079-4ef1-ae62-c27bb3f5a469
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# Framework (Windows 10)

Indicates whether the package is a framework package; that is, a package that can be used by other packages. Its value is **false** by default. You should not specify a value for it unless you are creating a framework.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Properties\>](element-properties.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<Framework\>**

## Syntax

```xml
<Framework>
  A boolean value.
</Framework>
```

## Attributes and elements

### Attributes

None.

### Child elements

None.

### Parent Elements

| Parent element | Description |
|-|-|
| [Properties](element-properties.md) | Defines additional metadata about the package including attributes that describe how the package appears to users. |

> [!NOTE]
> You may get an error if the manifest elements DisplayName or Description contain characters disallowed by the Windows firewall; namely `|` and `all`, due to which Windows fails to create the AppContainer profile for the package. Use this reference for [troubleshooting](/windows/win32/appxpkg/troubleshooting) if you get an error.

## Remarks

A package marked as a framework package cannot declare dependencies on other packages.

A framework package cannot define the [**Applications**](element-applications.md) or [**Capabilities**](element-capabilities.md) node.

## Requirements

|   | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |


 

 
