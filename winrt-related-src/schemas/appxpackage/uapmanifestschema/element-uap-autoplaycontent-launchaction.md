---
title: uap:LaunchAction (in AutoPlayContent)
description: Describes an AutoPlay content action (Windows 10).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Applications, Application, Extensions, uap:Extension, uap:AutoPlayContent, uap:LaunchAction]
---

# uap:LaunchAction (in AutoPlayContent)

Describes an AutoPlay content action.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:Extension>`](element-uap-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap:AutoPlayContent>`](element-uap-autoplaycontent.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap:LaunchAction>`**  

## Syntax

```xml
<uap:LaunchAction
  Verb = 'A required string with a value between 1 and 64 characters in length that consists of alphanumeric characters, periods (`.`), dashes (`-`), and spaces only.'
  ActionDisplayName = 'A required string between 1 and 256 characters in length. This string is localizable.'
  ContentEvent = 'A required string with a value between 1 and 255 characters in length. Backward slashes (`\`) are not allowed.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Verb** | A unique identifier that is passed to the app when it is launched. The app can use this string to determine which AutoPlay handler triggered its launch. It is unique per application in the package and is case sensitive. | A string with a value between 1 and 64 characters in length that consists of alphanumeric characters, periods (`.`), dashes (`-`), and spaces only. | Yes |  |
| **ActionDisplayName** | The name displayed to the user in the AutoPlay flyout for the handler. | A string between 1 and 256 characters in length. This string is localizable. | Yes |  |
| **ContentEvent** | The name of a content-related event that the extensibility point handles. For more info, see [Remarks](#remarks). | A string with a value between 1 and 255 characters in length. Backward slashes (`\`) are not allowed. | Yes |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [uap:AutoPlayContent](element-uap-autoplaycontent.md) | Declares an app extensibility point of type **windows.autoPlayContent**. The app provides the specified AutoPlay content actions. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **Minimum OS Version** | Windows 10 version 1511 (Build 10586) |

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
- [uap:LaunchAction (in type: CT_AutoPlayDevice)](element-uap-autoplaydevice-launchaction.md)
- [uap:LaunchAction (global)](element-uap-appointmentsproviderlaunchactions-launchaction.md)
- [Supporting AutoPlay](/previous-versions/windows/apps/hh452731(v=win.10))
