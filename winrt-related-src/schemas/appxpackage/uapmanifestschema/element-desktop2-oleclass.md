---
ms.assetid: 6e4f6092-889f-4462-baf5-45ba7ca0359a
title: desktop2:OleClass
description: Enables OLE to get the OLE class registered for a given file extension.
ms.date: 04/05/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop2:OleClass

Enables OLE to get the OLE class registered for a given file extension.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:Extension\>](element-uap-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:FileTypeAssociation\>](element-uap-filetypeassociation.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop2:OleClass\>**

## Syntax

```xml
<desktop2:OleClass
  Clsid = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Clsid** | The ID of a COM class registered in the [\<ComServer\>](element-com-comserver.md) element.| A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [uap:FileTypeAssociation](element-uap-filetypeassociation.md) | Declares an app extensibility point of type **windows.fileTypeAssociation**. A file type association indicates that the app is registered to handle files of the specified types. |

## Remarks

A `<desktop2:OleClass>` element can only exist under a `<FileTypeAssociation>` element that is defined with an `<Application>` element that has: EntryPoint="windows.FullTrustApplication".

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/2` |
| **Minimum OS Version** | Windows 10 version 1703 (Build 15063) |
