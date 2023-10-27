---
title: desktop7:ShadowCopyExcludeFile
description: Specifies a file to be excluded by the Volume Shadow Copy Service (VSS).
ms.date: 10/15/2021
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop7:ShadowCopyExcludeFile

Specifies the source and target for a tile or pin that should be updated as part of a desktop app migration.

## Element Hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop7:Extension\>](element-desktop7-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop7:Shortcut\>](element-desktop7-shortcut.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop7:ShadowCopyExcludeFiles\>](element-desktop7-shadowcopyexcludefiles.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop7:ShadowCopyExcludeFile\>**

## Syntax

```xml
<desktop7:ShadowCopyExcludeFile
  Name = 'A string with a value between 1 and 256 characters in length.'
  File = 'A string with a value between 1 and 256 characters in length that cannot contain these characters: <, >, ", |, or ?.'   
  Recursive = 'An optional boolean value.' />
```

### Key

`?` optional (zero or one)

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | A descriptive name of the file.  This value is not actually used directly by the system but makes it easier to read the entry in the registry. | A string with a value between 1 and 256 characters in length. | Yes |  |
| **File** | The file or files to exclude. This can be an absolute path to one file or a path containing wildcards and VSS variables. | A string with a value between 1 and 256 characters in length that cannot contain these characters: `<`, `>`, `"`, `|`, or `?`. | Yes |  |
| **Recursive** | A boolean indicating whether the specified path should be excluded recursively. | An optional boolean value. | No |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|---------------|-------------|
| [ShadowCopyExcludeFiles](element-desktop7-shadowcopyexcludefiles.md) | Specifies a set of files to be excluded by the Volume Shadow Copy Service (VSS). |  

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/7` |
| Minimum OS Version | Windows 10 (Build 19645) |
