---
title: desktop3:InvokeAction
description: Contains content and device information for invoking an AutoPlay action.
ms.date: 10/10/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop3:InvokeAction

Contains content and device information for invoking an AutoPlay action.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop3:Extension\>](element-desktop3-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop3:AutoPlayHandler\>](element-desktop3-autoplayhandler.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop3:InvokeAction\>**

## Syntax

```xml
<desktop3:InvokeAction
  ActionDisplayName = 'A string with a value between 1 and 256 characters in length.'
  ProviderDisplayName = 'A string with a value between 1 and 256 characters in length.'
  DefaultIcon = 'An optional string with a value between 1 and 256 characters in length that cannot contain these characters: <, >, :, %, ", |, ?, or *.' >

  <!-- Child elements -->
  ( desktop3:Content{0,1000},
    desktop3:Device{0,1000} )

</desktop3:InvokeAction>
```

### Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **ActionDisplayName** | A string that represents the action that users can take with a device that they connect to a PC (For example: "Import files", or "Play video"). | A string with a value between 1 and 256 characters in length. | Yes |  |
| **ProviderDisplayName** | A string that represents your app or service (For example: "Contoso video player"). | A string with a value between 1 and 256 characters in length. | Yes |  |
| **DefaultIcon** | A path to either an .ico file or a resource in a binary file for the default icon.  | An optional string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `:`, `%`, `"`, `|`, `?`, or `*`. | No |  |

### Child elements

| Child element | Description |
|-|-|
| [desktop3:Content](element-desktop3-content.md) | Defines the content information of an AutoPlayHandler. |  
| [desktop3:Device](element-desktop3-device.md) | Defines the device information of an AutoPlayHandler. |

### Parent elements

| Parent element | Description |
|-|-|
| [desktop3:AutoPlayHandler](element-desktop3-autoplayhandler.md) | Handler for AutoPlay, which can present your app as an option when a user connects a device to their PC. |

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/3` |
