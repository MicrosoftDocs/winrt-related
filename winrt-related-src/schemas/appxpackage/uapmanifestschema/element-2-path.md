---
description: The path to the DLL (in ProxyStub).
Search.Product: eADQiWindows 10XVcnh
title: Path (in ProxyStub) (Windows 10)
ms.assetid: 4522dd59-287a-4c40-8054-168d06f61a08
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# Path (in ProxyStub) (Windows 10)

The path to the DLL.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extension\>](extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<InProcessServer\>](element-inprocessserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<ProxyStub\>](element-proxystub.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<Path\>**

## Syntax

```xml
<Path>
  A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.
</Path>
```

## Attributes and Elements

### Attributes

None.

### Child Elements

None.

### Parent Elements

| Parent element | Description |
|-|-|
| [InProcessServer](element-inprocessserver.md) | Declares a package extensibility point of type **windows.activatableClass.inProcessServer**. The app uses a dynamic link library (DLL) that exposes one or more activatable classes. |
| [ProxyStub](element-proxystub.md) | Declares a package extensibility point of type **windows.activatableClass.proxyStub**. A proxy can be composed of one or more interfaces. |

## Related elements

The following elements have the same name as this one, but different content or attributes:

- **[Path (*type: ST_Executable*)](element-1-path.md)**

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
