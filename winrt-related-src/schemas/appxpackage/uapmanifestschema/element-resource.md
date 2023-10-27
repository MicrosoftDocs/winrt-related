---
description: Declares a language, display scale, or DirectX feature level for resources that the package contains. The scale and DirectX feature level attributes are common for all resources in the package.
Search.Product: eADQiWindows 10XVcnh
title: Resource (Windows 10 package schema)
ms.assetid: 445e7de7-e778-4666-b099-3d7f6f0125c7
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 10/26/2017
---

# Resource (package schema for Windows 10)

Declares a language, display scale, or DirectX feature level for resources that the package contains. The scale and DirectX feature level attributes are common for all resources in the package.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Resources\>](element-resources.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<Resource\>**

## Syntax

```xml
<Resource
  Language = 'A valid BCP-47 language tag (such as "en", or "en-us").'
  uap:Scale = 'An optional number that can be one of the following values: "80", "100", "120", "125", "140", "150", "160", "175", "180", "200", "225", "250", "300", "350", "400", or "450".'
  uap:DXFeatureLevel = 'An optional string that can have one of the following values: "dx9", "dx10", "dx11", or "dx12".' />
```

See the [BCP-47 language tag](https://go.microsoft.com/fwlink/p/?linkid=227302) for more information.

### Key

`?`  optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Language** | The language for the resource contained in the package. The syntax of this attribute is defined by the IETF's [BCP47: Tags for Identifying Languages](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). | A valid BCP-47 language tag (such as `en`, or `en-us`). | No |  |
| **uap:Scale** | The [resolution scale](/uwp/api/Windows.Graphics.Display.ResolutionScale) of the resource. | An optional number that can be one of the following values: *80*, *100*, *120*, *125*, *140*, *150*, *160*, *175*, *180*, *200*, *225*, *250*, *300*, *350*, *400*, or *450*. | No |  |
| **uap:DXFeatureLevel** | The DirectX [feature level](/windows/win32/direct3d11/overviews-direct3d-11-devices-downlevel-intro#overview)  of the resource from the manifest's `Resources\Resource` field. | An optional string that can have one of the following values: *dx9*, *dx10*, *dx11*, or *dx12*. | No |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [Resources](element-resources.md) | Declares languages for the resources that the package contains. Every package must declare at least one language for resources. The scale and DirectX feature level attributes are common for all resources in the package. |

## Remarks

If you have string/image/file resources in your Visual Studio project that have language qualifiers in their names (see [Tailor your resources for language, scale, high contrast, and other qualifiers](/windows/uwp/app-resources/tailor-resources-lang-scale-contrast?branch=live)), then you can put the following in your app package manifest source file (`Package.appxmanifest`).

```xml
<Resources>
  <Resource Language="x-generate" />
</Resources>
```

When Visual Studio builds your package manifest file (`AppxManifest.xml`), it expands that single `Resource` element into a union of all the language qualifiers that it finds in your project. For example, if you have string, image, and/or file resources whose folder or file names include "en-US", "ja-JP", and "fr-FR", then your built `AppxManifest.xml` file will contain the following.

```xml
  <Resources>
    <Resource Language="EN-US" />
    <Resource Language="JA-JP" />
    <Resource Language="FR-FR" />
  </Resources>
```

The first entry in the list is the default language for the app, which you can set in Visual Studio. With your solution open in Visual Studio, open `Package.appxmanifest` and, on the Application tab, set **Default language**.

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
