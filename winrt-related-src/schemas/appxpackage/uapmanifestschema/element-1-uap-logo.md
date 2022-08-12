---
description: A path to a file that contains an image (Windows 10, child of uap:Protocol).
Search.Product: eADQiWindows 10XVcnh
title: uap:Logo (Windows 10, child of uap:Protocol)
ms.assetid: 22d15097-d9f7-4a9b-9466-d7e76fd7d5ad
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap:Logo (Windows 10, child of uap:Protocol)

A path to a file that contains an image.

## Element hierarchy

> [\<Package\>](element-package.md)
> > [\<Applications\>](element-applications.md)
> > > [\<Application\>](element-application.md)
> > > > [\<Extensions\>](element-extensions.md)
> > > > > [\<uap:Extension\>](element-uap-extension.md)
> > > > > > [\<uap:FileTypeAssociation\>](element-uap-filetypeassociation.md)
> > > > > > [\<uap:Protocol\>](element-uap-protocol.md)
> > > > > > > **\<uap:Logo\>**

## Syntax

```xml
<uap:Logo>
  A string between 1 and 256 characters in length that ends with ".jpg", ".png", or ".jpeg" that can't contain these characters: <, >, :, ", |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both.
</uap:Logo>
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
