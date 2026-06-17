---
title: desktop3:Device
description: Defines the device information of an AutoPlayHandler.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, desktop3:Extension, desktop3:AutoPlayHandler, desktop3:InvokeAction, desktop3:Device]
---

# desktop3:Device

Defines the device information of an AutoPlayHandler.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop3:Extension>`](element-desktop3-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop3:AutoPlayHandler>`](element-desktop3-autoplayhandler.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop3:InvokeAction>`](element-desktop3-invokeaction.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop3:Device>`**

## Syntax

```xml
<desktop3:Device
  DeviceEvent = 'A required string with a value between 1 and 255 characters in length. Backward slashes (`\`) are not allowed.'
  HWEventHandler = 'A required GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
  InitCmdLine = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **DeviceEvent** | The name of a content event raised when a volume device such as a camera memory card, USB drive, or DVD is inserted into the PC. | A string with a value between 1 and 255 characters in length. Backward slashes (`\`) are not allowed. | Yes |  |
| **HWEventHandler** | The Class ID of the app that implements the [IHWEventHandler](/windows/win32/api/shobjidl/nn-shobjidl-ihweventhandler) interface. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |
| **InitCmdLine** | A string parameter that should be passed into the [Initialize](/windows/win32/api/shobjidl/nf-shobjidl-ihweventhandler-initialize) method of the [IHWEventHandler](/windows/win32/api/shobjidl/nn-shobjidl-ihweventhandler) interface. | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [desktop3:InvokeAction](element-desktop3-invokeaction.md) | Contains content and device information for invoking an AutoPlay action. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/3` |
| **Minimum OS Version** | Windows 10 version 1709 (Build 16299) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
