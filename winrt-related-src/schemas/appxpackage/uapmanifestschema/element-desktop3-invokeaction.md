---
title: desktop3:InvokeAction
description: Contains content and device information for invoking an AutoPlay action.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, desktop3:Extension, desktop3:AutoPlayHandler, desktop3:InvokeAction]
---

# desktop3:InvokeAction

Contains content and device information for invoking an AutoPlay action.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop3:Extension>`](element-desktop3-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop3:AutoPlayHandler>`](element-desktop3-autoplayhandler.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop3:InvokeAction>`**

## Syntax

```xml
<desktop3:InvokeAction
  ActionDisplayName = 'A required string between 1 and 256 characters in length. This string is localizable.'
  ProviderDisplayName = 'A required string between 1 and 256 characters in length. This string is localizable.'
  DefaultIcon = 'An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.' >

  <!-- Child elements -->
  desktop3:Content{0,1000}
  desktop3:Device{0,1000}

</desktop3:InvokeAction>
```

### Key

`{}` specific range of occurrences

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **ActionDisplayName** | A string that represents the action that users can take with a device that they connect to a PC (For example: "Import files", or "Play video"). | A string between 1 and 256 characters in length. This string is localizable. | Yes |  |
| **ProviderDisplayName** | A string that represents your app or service (For example: "Contoso video player"). | A string between 1 and 256 characters in length. This string is localizable. | Yes |  |
| **DefaultIcon** | A path to either an .ico file or a resource in a binary file for the default icon. | An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *. | No |  |

## Child elements

| Child element | Description |
|-|-|
| [desktop3:Content](element-desktop3-content.md) | Defines the content information of an AutoPlayHandler. |
| [desktop3:Device](element-desktop3-device.md) | Defines the device information of an AutoPlayHandler. |

## Parent elements

| Parent element | Description |
|-|-|
| [desktop3:AutoPlayHandler](element-desktop3-autoplayhandler.md) | Handler for AutoPlay, which can present your app as an option when a user connects a device to their PC. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/3` |
| **Minimum OS Version** | Windows 10 version 1709 (Build 16299) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
