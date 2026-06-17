---
title: desktop7:ShadowCopyExcludeFile
description: Specifies a file to be excluded by the Volume Shadow Copy Service (VSS).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
no-loc: [Package, Applications, Application, Extensions, desktop7:Extension, desktop7:ShadowCopyExcludeFiles, desktop7:ShadowCopyExcludeFile]
---

# desktop7:ShadowCopyExcludeFile

Specifies the source and target for a tile or pin that should be updated as part of a desktop app migration.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop7:Extension>`](element-desktop7-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop7:ShadowCopyExcludeFiles>`](element-desktop7-shadowcopyexcludefiles.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop7:ShadowCopyExcludeFile>`**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop7:Extension>`](element-desktop7-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop7:ShadowCopyExcludeFiles>`](element-desktop7-shadowcopyexcludefiles.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop7:ShadowCopyExcludeFile>`**

## Syntax

```xml
<desktop7:ShadowCopyExcludeFile
  Name = 'A required string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  File = 'A required value. <!-- TODO: Add description for desktop7:ST_ShadowCopyExcludeFile -->'
  Recursive = 'An optional boolean value.' />
```

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | A descriptive name of the file.  This value is not actually used directly by the system but makes it easier to read the entry in the registry. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |  |
| **File** | The file or files to exclude. This can be an absolute path to one file or a path containing wildcards and VSS variables. | A value. <!-- TODO: Add data type for desktop7:ST_ShadowCopyExcludeFile --> | Yes |  |
| **Recursive** | A boolean indicating whether the specified path should be excluded recursively. | An optional boolean value. | No |  |

## Child elements

None.

## Parent elements

| Parent element | Description |
|-|-|
| [desktop7:ShadowCopyExcludeFiles](element-desktop7-shadowcopyexcludefiles.md) | Specifies a set of files to be excluded by the Volume Shadow Copy Service (VSS). |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/7` |
| **Minimum OS Version** | Windows 10 (Build 19645) |

## Remarks

<!-- Author content goes here -->

## Examples

<!-- Author content goes here -->
