---
description: The path to the executable (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: Path (in OutOfProcessServer) (Windows 10)
ms.assetid: f3fe9184-f270-4050-b444-ec37a596b993
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# Path (in OutOfProcessServer) (Windows 10)

The path to the executable.

## Element hierarchy

> [\<Package\>](element-package.md)
> > [\<Extensions\>](element-extensions.md)
> > > [\<Extension\>](element-extension.md)
> > > > [\<OutOfProcessServer\>](element-outofprocessserver.md)
> > > > > **\<Path\>**

## Syntax

```xml
<Path>
  A string between 1 and 256 characters in length that must end with ".exe" and cannot contain these characters: <, >, :, ", |, ?, or *. It specifies the default executable for the extension. If not specified, the executable defined for the app is used.  If specified, the EntryPoint property is also used. If that EntryPoint property isn't specified, the EntryPoint defined for the app is used.
</Path>
```

## Attributes and elements

### Attributes

None.

### Child elements

None.

### Parent elements

| Parent elements | Description |
|-|-|
| [OutOfProcessServer](element-outofprocessserver.md) | Declares a package extension point of type **windows.activatableClass.outOfProcessServer**. The app uses an executable (`.exe`) that exposes one or more activatable classes. |

## Related elements

The following elements have the same name as this one, but different content or attributes:

- **[Path (type: ST_FileName)](element-path.md)**

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
