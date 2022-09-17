---
description: Specifies whether the executable runs as a single instance or can run as multiple instances (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: Instancing (Windows 10)
ms.assetid: 26533f27-2470-4083-91a0-4e4b03f8479a
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# Instancing (Windows 10)

Specifies whether the executable runs as a single instance or can run as multiple instances.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extension\>](element-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<OutOfProcessServer\>](element-outofprocessserver.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<Instancing\>**

## Syntax

```xml
<Instancing>
  "singleInstance" or "multipleInstances"
</Instancing>
```

## Attributes and elements

### Attributes

None.

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [OutOfProcessServer](element-outofprocessserver.md) | Declares a package extension point of type **windows.activatableClass.outOfProcessServer**. The app uses an executable (`.exe`) that exposes one or more activatable classes. |

## Requirements

| Item  | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
