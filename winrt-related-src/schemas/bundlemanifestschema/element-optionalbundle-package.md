---

ms.assetid: ef52c3d3-b112-42a5-b66d-2ab9cf672a5d
title: Package (Bundle schema, child of OptionalBundle)
description: Defines one of the app packages or resource packages in the optional bundle.

ms.date: 04/05/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, optional bundle 
---

# Package (Bundle schema, child of OptionalBundle)

## Description
Defines one of the app packages or resource packages in the optional bundle.

## Element Hierarchy
<dl>
<dt><a href="element-bundle.md">&lt;Bundle&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-optionalbundle.md">&lt;OptionalBundle&gt;</a></dt>
<dd><b>&lt;Package&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<Package Type?         = Specifies the package type as application or resource. : "resource", "application"
         Version       = A version string in quad notation, "Major.Minor.Build.Revision".
         Architecture? = "x86" | "x64" | "arm" | "neutral" 
         ResourceId?   = A string between 1 and 30 characters in length that consists of alpha-numeric, period, and dash characters.
         FileName      = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.
         Offset?       = unsignedLong
         Size?         = unsignedLong >
           
    <!-- Child elements -->
    Resources
```

### Key
`?`   optional (zero or one)  
`{}`  specific range of occurrences

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Type  | Defines the type of package in the bundle. | A string that specifies the type of package. This can be: "resource" or "application" | No |
| Version | Defines the version number of the package. | A version string in quad notation, "Major.Minor.Build.Revision". | Yes |
| Architecture | Describes the architecture of the code contained in the package. A package that includes executable code must include this attribute. | This can be one of the following values: "x86", "x64", "arm", "neutral" | No |
| ResourceId | Describes the type of resource in the package. | A string between 1 and 30 characters in length that consists of alpha-numeric, period, and dash characters. | No |
| FileName | Describes the file name of the package. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *. | Yes |
| Offset |  | unsignedLong | No |
| Size | The size of the package. | unsignedLong | No |

## Child Elements

| Child Element | Description |
|---------------|-------------|
| [Resources](element-optionalbundle-resources.md) | Declares languages, resolution scales, and DirectX feature levels for the resources that the package contains. |

## Remarks

## Examples

## Requirements

|          |         |
|----------|--------------|
| **Namespace** | `http://schemas.microsoft.com/appx/2016/bundle` |