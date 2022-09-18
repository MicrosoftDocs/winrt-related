---
description: Describes an AutoPlay content action (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: uap:LaunchAction (in uap:AutoPlayContent) (Windows 10)
ms.assetid: 5d2c732f-08dd-4e7e-93b1-6bb122e2179f
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# uap:LaunchAction (in uap:AutoPlayContent) (Windows 10)

Describes an AutoPlay content action.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:Extension\>](element-uap-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap:AutoPlayContent\>](element-uap-autoplaycontent.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap:LaunchAction\>**

## Syntax

```xml
<LaunchAction
  Verb = 'A string with a value between 1 and 64 characters in length that consists of alphanumeric characters, periods ("."), dashes ("-"), and spaces only.'
  ActionDisplayName = 'A string with a value between 1 and 256 characters in length. This string is localizable.'
  ContentEvent = 'A string with a value between 1 and 255 characters in length. Backward slashes ("\") are not allowed.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Verb** | A unique identifier that is passed to the app when it is launched. The app can use this string to determine which AutoPlay handler triggered its launch. It is unique per application in the package and is case sensitive. | A string with a value between 1 and 64 characters in length that consists of alphanumeric characters, periods (`.`), dashes (`-`), and spaces only. | Yes |  |
| **ActionDisplayName** | The name displayed to the user in the AutoPlay flyout for the handler. | A string with a value between 1 and 256 characters in length. This string is localizable. | Yes |  |
| **ContentEvent** | The name of a content-related event that the extensibility point handles. For more info, see [Remarks](#remarks). | A string with a value between 1 and 255 characters in length. Backward slashes (`\`) are not allowed. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [uap:AutoPlayContent](element-uap-autoplaycontent.md) | Declares an app extensibility point of type *windows.autoPlayContent*. The app provides the specified AutoPlay content actions. |

## Related elements

The following elements have the same name as this one, but different content or attributes:

- [uap:LaunchAction (in type: CT_AutoPlayDevice)](element-1-uap-launchaction.md)
- [uap:LaunchAction (global)](element-2-uap-launchaction.md)

## Remarks

**ContentEvent** can be a custom event defined by the volume or one of the following well-known events:

- **HandleCDBurningOnArrival**
- **HandleDVDBurningOnArrival**
- **MixedContentOnArrival**
- **PlayBluRayOnArrival**
- **PlayCDAudioOnArrival**
- **PlayDVDAudioOnArrival**
- **PlayDVDMovieOnArrival**
- **PlayEnhancedCDOnArrival**
- **PlayEnhancedDVDOnArrival**
- **PlayMusicFilesOnArrival**
- **PlaySuperVideoCDMovieOnArrival**
- **PlayVideoCDMovieOnArrival**
- **PlayVideoFilesOnArrival**
- **ShowPicturesOnArrival**
- **StorageOnArrival**
- **UnknownContentOnArrival**

## Examples

```xml
<uap:Extension
  Category="windows.autoPlayContent">
  <uap:AutoPlayContent>
    <uap:LaunchAction
      Verb="open"
      ActionDisplayName="Display"
      ContentEvent="ShowPicturesOnArrival"/>
  </uap:AutoPlayContent>
</uap:Extension>
```

## See also

[Supporting AutoPlay](/previous-versions/windows/apps/hh452731(v=win.10))

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
