---
title: uap5:VideoRendererEffect
description: Enables activation of video renderer effects in apps.
ms.date: 10/10/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap5:VideoRendererEffect

Enables activation of video renderer effects in apps.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap5:Extension\>](element-uap5-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<uap5:VideoRendererEffect\>**

## Syntax

```xml
<uap5:VideoRendererEffect
    DisplayName = 'A string with a value between 1 and 256 characters in length. This string is localizable.'
    Description = 'A string with a value between 1 and 2048 characters in length.' 
    wincap3:ActivatableClassId = 'A string with a value between 1 and 255 characters in length.'
    wincap3:Path = 'A string with a value between 1 and 256 characters in length that cannot contain these characters: <, >, ", |, ?, or *.'
    wincap3:ProcessorArchitecture = 'A string value that can be one of the following: "x86", "x64", "arm", "arm64", or "neutral".' />

    <!-- Child elements -->
    uap5:VideoRendererExtensionProfiles{0,1000}
    uap5:InputTypes{0,1000}

</uap5:VideoRendererEffect>
```

### Key

`?`   optional (zero or one)
`{}` specific range of occurrences

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **DisplayName** | The video renderer display name. | A string with a value between 1 and 256 characters in length. This string is localizable. | No |  |
| **Description** | A description of the video renderer effect. | A string with a value between 1 and 2048 characters in length. | No |  |
| **rescap3:ActivatableClassId** | The class ID associated with this media content. | A string with a value between 1 and 255 characters in length. | No |
| **rescap3:Path** | The path to the media content. | A string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `"`, `|`, `?`, or `*`. | No |
| **rescap3:ProcessorArchitecture** | The processor architecture used for the media content. | A string value that can be one of the following: *x86*, *x64*, *arm*, *arm64*, or *neutral*. | No |

### Child elements

| Child element | Description |
|-|-|
| [VideoRendererExtensionProfiles](element-uap5-VideoRendererExtensionProfiles.md) | Contains a list of video renderer profiles. |
| [InputTypes](element-uap5-InputTypes.md) | Contains a list of media input sub-types. |

### Parent elements

| Parent element | Description |
|-|-|
| [uap5:Extension](element-uap5-extension.md) | Declares an extensibility point for the app. |

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

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |
| **Minimum OS Version** | Windows 10 version 1709 (Build 16299) |
