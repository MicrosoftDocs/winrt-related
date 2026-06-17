---
title: Resource
description: Declares a language, display scale, or DirectX feature level for resources that the package contains. The scale and DirectX feature level attributes are common for all resources in the package.
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, Package, Resources, Resource]
---

# Resource

Declares a language, display scale, or DirectX feature level for resources that the package contains. The scale and DirectX feature level attributes are common for all resources in the package.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Resources>`](element-f-resources.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<Resource>`**  

## Syntax

```xml
<Package
  xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10">
  ...
  <Resource
    Language = 'An optional valid BCP 47 language tag.'
    uap:Scale = 'An optional value. <!-- TODO: Add description for t:ST_Scale_All -->'
    uap:DXFeatureLevel = 'An optional string that can have one of the following values: "dx9", "dx10", or "dx11".' />
</Package>
```

See the [BCP-47 language tag](https://go.microsoft.com/fwlink/p/?linkid=227302) for more information.

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Language** | The language for the resource contained in the package. The syntax of this attribute is defined by the IETF's [BCP47: Tags for Identifying Languages](https://www.rfc-editor.org/info/bcp47). | An optional valid BCP 47 language tag. | No |  |
| **uap:Scale** | The [resolution scale](/uwp/api/Windows.Graphics.Display.ResolutionScale) of the resource. | An optional value. <!-- TODO: Add data type for t:ST_Scale_All --> | No |  |
| **uap:DXFeatureLevel** | The DirectX [feature level](/windows/win32/direct3d11/overviews-direct3d-11-devices-downlevel-intro#overview)  of the resource from the manifest's `Resources\Resource` field. | An optional string that can have one of the following values: *dx9*, *dx10*, *dx11*. | No |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [Resources](element-f-resources.md) | Declares the union of languages, display scales, and DirectX feature levels for the resources that the package contains. For details and examples, see [Resource](element-f-resource.md). |

## Requirements


| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
| **uap** | `http://schemas.microsoft.com/appx/manifest/uap/windows10` |
| **Minimum OS Version** | <!-- TODO: Add minimum OS version --> |


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

## Examples

<!-- Author content goes here -->
