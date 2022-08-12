---
description: Defines one or more extensibility points for the app (Windows 10) by detailing the element hierarchy and syntax.
Search.Product: eADQiWindows 10XVcnh
title: Extensions (in Application) (Windows 10)
ms.assetid: 267051e3-b09c-467c-b5bd-4575cc31cb36
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# Extensions (in Application) (Windows 10)

Defines one or more extensibility points for the app.

## Element hierarchy

> [\<Package\>](element-package.md)
> > [\<Applications\>](element-applications.md)
> > > [\<Application\>](element-application.md)
> > > > **\<Extensions\>**

## Syntax

```xml
<Extensions>

  <!-- Child elements -->
  Extension{1,10000},
  com:Extension{1, 10000},
  com2:Extension{1, 10000},
  desktop:Extension{1,10000},
  desktop2:Extension{1, 10000},
  desktop3:Extension{1, 10000},
  desktop4:Extension{1, 10000},
  desktop6:Extension{1, 10000},
  desktop7:Extension{1, 10000},
  desktop8:Extension{1,10000},
  desktop9:Extension{1, 10000},
  rescap2:Extension{1, 10000},
  rescap3:Extension{1, 10000},
  uap:Extension{1,10000},
  uap2:Extension{1, 10000},
  uap3:Extension{1, 10000},
  uap4:Extension{1, 10000},
  uap5:Extension{1, 10000},
  uap6:Extension{1, 10000},
  uap7:Extension{1, 10000},
  uap8:Extension{1, 10000},
  uap10:Extension{1, 10000}
  uap12:Extension{1, 10000},
  uap13:Extension{1, 10000}

</Extensions>
```

### Key

`{}`   specific range of occurrences

## Attributes and Elements

### Attributes

None.

### Child Elements

| Child Element | Description |
|---------------|-------------|
| [Extension (global)](element-1-extension.md) | Declares an extensibility point for the package. |
| [com:Extension](element-com-extension.md) | Declares an extensibility point for the package. |
| [com2:Extension](element-com2-extension.md) | Declares an extensibility point for the package. |
| [desktop:Extension](element-desktop-extension.md) | Declares an extensibility point for the package. |
| [desktop2:Extension](element-desktop2-extension.md) | Declares an extensibility point for the package. |
| [desktop3:Extension](element-desktop3-extension.md) | Declares an extensibility point for the package. |
| [desktop4:Extension](element-desktop4-extension.md) | Declares an extensibility point for the package. |
| [desktop6:Extension](element-desktop6-extension.md) | Declares an extensibility point for the package. |
| [desktop7:Extension](element-desktop7-extension.md) | Declares an extensibility point for the package. |
| [desktop8:Extension](element-desktop8-extension.md) | Declares an extensibility point for the package. |
| [desktop9:Extension](element-desktop9-extension.md) | Declares an extensibility point for the package. |
| [rescap2:Extension](element-rescap2-extension-manual.md) | Declares an extensibility point for the package. |
| [rescap3:Extension](element-rescap3-extension.md) | Declares an extensibility point for the package. |
| [uap:Extension](element-uap-extension.md) | Declares an extensibility point for the package. |
| [uap2:Extension](element-uap2-extension.md) | Declares an extensibility point for the package. |
| [uap3:Extension](element-uap3-extension-manual.md) | Declares an extensibility point for the package. |
| [uap4:Extension](element-uap4-extension.md) | Declares an extensibility point for the package. |
| [uap5:Extension](element-uap5-extension.md) | Declares an extensibility point for the package. |
| [uap6:Extension](element-uap6-extension.md) | Declares an extensibility point for the package. |
| [uap7:Extension](element-uap7-extension.md) | Declares an extensibility point for the package. |
| [uap8:Extension](element-uap8-extension.md) | Declares an extensibility point for the package. |
| [uap10:Extension](element-uap10-extension.md) | Declares an extensibility point for the package. |
| [uap12:Extension](element-uap12-extension.md) | Declares an extensibility point for the package. |
| [uap13:Extension](element-uap13-extension.md) | Declares an extensibility point for the package. |

### Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [Application](element-application.md) | Represents an app that comprises part of or all of the functionality delivered in the package. |

## Related elements

The following elements have the same name as this one, but different content or attributes:

- **[Extensions (type: CT_PackageExtensions)](element-extensions.md)**

## Remarks

Extensibility points are a mechanism by which an app can add functionality in a manner defined by the operating system. An example of an app extensibility point is the ability to create a file type association and enable your app to be the default handler for files with a specific file name extension.

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
