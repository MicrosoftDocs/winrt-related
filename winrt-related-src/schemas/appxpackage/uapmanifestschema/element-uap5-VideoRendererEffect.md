---
title: uap5:VideoRendererEffect
description: Enables activation of video renderer effects in apps.
ms.date: 06/05/2026
ms.topic: reference
no-loc: [Package, Applications, Application, Extensions, uap5:Extension, uap5:VideoRendererEffect]
keywords: windows 10, uwp, schema, manifest, desktop, extension
---

# uap5:VideoRendererEffect

Enables activation of video renderer effects in apps.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<uap5:Extension>`](element-uap5-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<uap5:VideoRendererEffect>`**

## Syntax

```xml
<uap5:VideoRendererEffect
  DisplayName = 'An optional string between 1 and 256 characters in length. This string is localizable.'
  Description = 'An optional string between 1 and 2048 characters in length.'
  wincap3:ActivatableClassId = 'An optional string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, &#124;, ?, or *.'
  wincap3:Path = 'An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *, ending with the case-insensitive file extension ".dll".'
  wincap3:ProcessorArchitecture = 'An optional string that can have one of the following values: "x86", "x64", "arm", "arm64", or "neutral".' >

  <!-- Child elements -->
  uap5:VideoRendererExtensionProfiles?
  uap5:InputTypes?

</uap5:VideoRendererEffect>
```

### Key

`?` optional (zero or one)

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **DisplayName** | The video renderer display name. | An optional string between 1 and 256 characters in length. This string is localizable. | No |  |
| **Description** | A description of the video renderer effect. | An optional string between 1 and 2048 characters in length. | No |  |
| **wincap3:ActivatableClassId** | The class ID associated with this media content. | An optional string between 1 and 255 characters in length that cannot start or end with a period or contain these characters: <, >, :, ", /, \, &#124;, ?, or *. | No |  |
| **wincap3:Path** | The path to the media content. | An optional string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", &#124;, ?, or *, ending with the case-insensitive file extension ".dll". | No |  |
| **wincap3:ProcessorArchitecture** | The processor architecture used for the media content. | An optional string that can have one of the following values: *x86*, *x64*, *arm*, *arm64*, *neutral*. | No |  |

## Child elements

| Child element | Description |
|-|-|
| [uap5:VideoRendererExtensionProfiles](element-uap5-videorendererextensionprofiles.md) | Contains a list of video renderer profiles. |
| [uap5:InputTypes](element-uap5-inputtypes.md) | Contains a list of media input sub-types. |

## Parent elements

| Parent element | Description |
|-|-|
| [uap5:Extension](element-uap5-extension.md) | Declares an extensibility point for the app. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |
| **wincap3** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10/windowscapabilities/3` |
| **Minimum OS Version** | Windows 10 version 1709 (Build 16299) |

## Remarks

A video renderer effect can implement both [VideoRendererExtensionProfiles](element-uap5-VideoRendererExtensionProfiles.md) and [InputTypes](element-uap5-InputTypes.md). Note that when multiple schemes are implemented, video renderer extension profiles are prioritized first.

## Examples

```xml
<uap5:Extension
    Category="windows.videoRendererEffect">
    <uap5:VideoRendererEffect
        DisplayName="Grey1&2"
        Description="Grey Video1&2" 
        ActivatableClassId="GreyEffect12.Grey"
        Path="Grey12.dll">
        <uap5:VideoRendererExtensionProfiles>
            <uap5:VideoRendererExtensionProfile>grey</uap5:VideoRendererExtensionProfile>
        </uap5:VideoRendererExtensionProfiles>
        <uap5:InputTypes>
            <uap5:InputType
                SubType="{2533FA52-3122-4cc1-9A10-78EBC4977CEF}"/>
        </uap5:InputTypes>
    </uap5:VideoRendererEffect>
</uap5:Extension>
```
