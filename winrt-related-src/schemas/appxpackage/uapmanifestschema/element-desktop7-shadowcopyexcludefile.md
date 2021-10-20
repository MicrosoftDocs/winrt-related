---

title: desktop7:ShadowCopyExcludeFile
description: Specifies a file to be excluded by the Volume Shadow Copy Service (VSS).
ms.date: 10/15/2021
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop7:DesktopApp

## Description
Specifies the source and target for a tile or pin that should be updated as part of a desktop app migration.

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
<dt><a href="element-desktop7-extension.md">&lt;desktop7:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop7-shortcut.md">&lt;desktop7:Shortcut&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop7-shadowcopyexcludefiles.md">&lt;desktop7:ShadowCopyExcludeFiles&gt;</a></dt>
<dd><b>&lt;desktop7:ShadowCopyExcludeFile&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
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

```xml
<desktop7:ShadowCopyExcludeFile Name   = A string between 1 and 256 characters in length.
                        File   = A string between 1 and 256 characters in length that cannot contain these characters: <, >, ", |, or ?.   
                        Recursive?   = Boolean. 
                         >
</desktop7:ShadowCopyExcludeFile>
```

### Key
`?` optional (zero or one) 

## Attributes and Elements

### Attributes

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Name | A descriptive name of the file.  This value is not actually used directly by the system but makes it easier to read the entry in the registry.| A string between 1 and 256 characters in length. | Yes |
| File | The file or files to exclude. This can be an absolute path to one file or a path containing wildcards and VSS variables. | A string between 1 and 256 characters in length that cannot contain these characters: <, >, ", \|, or ?. | Yes |
| Recursive | A boolean indicating whether the specified path should be excluded recursively. | Boolean | No |

### Child Elements

None.

### Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [ShadowCopyExcludeFiles](element-desktop7-shadowcopyexcludefiles.md) | Specifies a set of files to be excluded by the Volume Shadow Copy Service (VSS). |  


## Remarks



## Requirements

|               |     Value                                                        |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/7` |