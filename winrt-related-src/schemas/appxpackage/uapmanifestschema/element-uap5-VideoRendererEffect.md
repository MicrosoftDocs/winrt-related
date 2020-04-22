---

title: uap5:VideoRendererEffect
description: Enables activation of video renderer effects in apps.

ms.date: 10/10/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap5:VideoRendererEffect

## Description
Enables activation of video renderer effects in apps.

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap5-extension.md">&lt;uap5:Extension&gt;</a></dt>
<dd><b>&lt;uap5:VideoRendererEffect&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<uap5:VideoRendererEffect DisplayName? = A string between 1 and 256 characters in length. This string is localizable.
                          Description? = A string between 1 and 2048 characters in length that cannot include characters such as tabs, carriage returns, and line feeds. >   
  <!-- Child elements -->
  ( uap5:VideoRendererExtensionProfiles{0,1000},
    uap5:InputTypes{0,1000} )
</uap5:VideoRendererEffect>
```

### Key
`?`   optional (zero or one)
`{}` specific range of occurrences

## Attributes and Elements
### Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| DisplayName | The video renderer display name. | A string between 1 and 256 characters in length. This string is localizable. | No |
| Description | A description of the video renderer effect. | A string between 1 and 2048 characters in length that cannot include characters such as tabs, carriage returns, and line feeds. | No |

### Child Elements 
| Child Element | Description |
|---------------|-------------|
| [VideoRendererExtensionProfiles](element-uap5-VideoRendererExtensionProfiles.md) | Contains a list of video renderer profiles. |
| [InputTypes](element-uap5-InputTypes.md) | Contains a list of media input sub-types. |

## Remarks
A video renderer effect can implement both [VideoRendererExtensionProfiles](element-uap5-VideoRendererExtensionProfiles.md) and [InputTypes](element-uap5-InputTypes.md). Note that when multiple schemes are implemented, video renderer extension profiles are prioritized first.

## Examples
```XML
<uap5:Extension Category="windows.videoRendererEffect">
    <uap5:VideoRendererEffect DisplayName="Grey1&2" Description="Grey Video1&2" 
                              ActivatableClassId="GreyEffect12.Grey" Path="Grey12.dll">
        <uap5:VideoRendererExtensionProfiles>
            <uap5:VideoRendererExtensionProfile>grey</uap5:VideoRendererExtensionProfile>
        </uap5:VideoRendererExtensionProfiles>
        <uap5:InputTypes>
            <uap5:InputType SubType="{2533FA52-3122-4cc1-9A10-78EBC4977CEF}"/>
        </uap5:InputTypes>
    </uap5:VideoRendererEffect>
</uap5:Extension>
```

## Requirements

|   |   |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |
