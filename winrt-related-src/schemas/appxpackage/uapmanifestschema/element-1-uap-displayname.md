---
description: A friendly name that can be displayed to users (Windows 10, child of uap:Protocol).
Search.Product: eADQiWindows 10XVcnh
title: uap:DisplayName (Windows 10, child of uap:Protocol)
ms.assetid: c435a2d1-6f05-44b8-9dc2-34b661793314
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap:DisplayName (Windows 10, child of uap:Protocol)

A friendly name that can be displayed to users.

## Element hierarchy

> [\<Package\>](element-package.md)
> > [\<Applications\>](element-applications.md)
> > > [\<Application\>](element-application.md)
> > > > [\<Extensions\>](element-extensions.md)
> > > > > [\<uap:Extension\>](element-uap-extension.md)
> > > > > > [\<uap:FileTypeAssociation\>](element-uap-filetypeassociation.md)
> > > > > > [\<uap:Protocol\>](element-uap-protocol.md)
> > > > > > >**\<uap:DisplayName\>**

## Syntax

```xml
<uap:DisplayName>
  A string between 1 and 256 characters in length. This string is localizable.
</uap:DisplayName>
```

## Attributes and elements

### Attributes

None.

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [uap:FileTypeAssociation](element-uap-filetypeassociation.md) | Declares an app extensibility point of type **windows.fileTypeAssociation**. A file type association indicates that the app is registered to handle files of the specified types. |
| [uap:Protocol](element-uap-protocol.md) | Declares an app extensibility point of type **windows.protocol**. A URI association indicates that the app is registered to handle URIs with the specified scheme. |

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
