---
description: Describes an AutoPlay device action (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: uap:LaunchAction (in uap:AutoPlayDevice) (Windows 10)
ms.assetid: 9b7d9e7a-4f85-4525-9a6b-683b3b78c23d
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap:LaunchAction (uap:AutoPlayDevice) (Windows 10)

Describes an AutoPlay device action.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:Extension\>](element-uap-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:AutoPlayDevice\>](element-uap-autoplaydevice.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap:LaunchAction\>**

## Syntax

```xml
<uap:LaunchAction
  Verb = 'A string between 1 and 64 characters in length that consists of letters, periods, dashes, and spaces only.'
  ActionDisplayName = 'A string between 1 and 256 characters in length. This string is localizable.' 
  DeviceEvent = 'A string between 1 and 255 characters in length. Backward slashes ('\') are not allowed.'
  Verb = 'A string with a value between 1 and 64 characters in length that consists of letters, periods, dashes, and spaces only.'
/>
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **ActionDisplayName** | The name displayed to the user in the AutoPlay flyout for the handler. This string is localizable. | A string with a value between 1 and 256 characters in length. | Yes |  |
| **DeviceEvent** | The name of a device-related event that the extensibility point handles. For more info, see **Remarks**. | A string with a value between 1 and 255 characters in length. Backward slashes (`\`) are not allowed. | Yes |  |
| **Verb** | A unique identifier passed to the app when it's launched. The app uses this string to determine which AutoPlay handler triggered its launch. It's unique per app in the package and is case sensitive. | A string with a value between 1 and 64 characters in length that consists of letters, periods, dashes, and spaces only. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [uap:AutoPlayDevice](element-uap-autoplaydevice.md) | Declares an app extensibility point of type **windows.autoPlayDevice**. The app provides the specified AutoPlay device actions. |

## Related elements

The following elements have the same name as this one, but different content or attributes:

- **[uap:LaunchAction (type: CT_AutoPlayContent)](element-uap-launchaction.md)**
- **[uap:LaunchAction (global)](element-2-uap-launchaction.md)**

## Remarks

**ContentEvent** can be a custom event defined for the device. For WPD devices, **ContentEvent** can be one of the following well-known events:

- **WPD\\AudioSource**
- **WPD\\ImageSource**
- **WPD\\VideoSource**

## Examples

```xml
<uap:Extension Category="windows.autoPlayDevice">
  <uap:AutoPlayContent>
    <uap:LaunchAction Verb="import" ActionDisplayName="Import" ContentEvent="WPD\ImageSource"/>
  </uap:AutoPlayContent>
</uap:Extension>
```

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
