---
title: desktop3:Content
description: Defines the content information of an AutoPlayHandler.
ms.date: 10/10/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop3:Content

Defines the content information of an AutoPlayHandler.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop3:Extension\>](element-desktop3-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop3:AutoPlayHandler\>](element-desktop3-AutoPlayHandler.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop3:InvokeAction\>](element-desktop3-invokeaction.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop3:Content\>**

## Syntax

```xml
<desktop3:Content
  ContentEvent = 'A string with a value between 1 and 255 characters in length. Backward slashes ("\") are not allowed.'
  Verb = 'A string with a value between 1 and 64 characters in length that consists of letters, numbers, periods, dashes, and spaces only.'
  DropTargetHandler = 'An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
  Parameters = 'An optional string with a value between 1 and 256 characters in length.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **ContentEvent** | The name of a content event raised when a volume device such as a camera memory card, USB drive, or DVD is inserted into the PC. | A string with a value between 1 and 255 characters in length. Backward slashes (`\`) are not allowed. | Yes |  |
| **Verb** | A literal value, specifying the action. Possible values can include (but aren't limited to): Show, play, import, and open. | A string with a value between 1 and 64 characters in length that consists of letters, numbers, periods (`.`), dashes (`-`), and spaces only. | Yes |  |
| **DropTargetHandler** | An GUID that identifies the class ID of the app that implements the [IDropTarget](/dotnet/api/microsoft.visualstudio.ole.interop.idroptarget) interface. | An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | No |  |
| **Parameters** | Parameters provided to start your app if the [IDropTarget](/dotnet/api/microsoft.visualstudio.ole.interop.idroptarget) interface is not implemented. | An optional string with a value between 1 and 256 characters in length. | No |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [desktop3:InvokeAction](element-desktop3-invokeaction.md) | Contains content and device information for invoking an AutoPlay action. |

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/3` |
| **Minimum OS Version** | Windows 10 version 1709 (Build 16299) |
