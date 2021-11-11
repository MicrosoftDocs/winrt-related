---
title: desktop7:ShadowCopyExcludeFiles
description: Specifies a set of files to be excluded by the Volume Shadow Copy Service (VSS).
ms.date: 10/15/2021
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop7:ShadowCopyExcludeFiles

## Description
Specifies a set of files to be excluded by the Volume Shadow Copy Service (VSS).

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
<dd><b>&lt;desktop7:ShadowCopyExcludeFiles&gt;</b></dd>
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
<desktop7:ShadowCopyExcludeFiles>
    desktop7:ShadowCopyExcludeFile{0,1000}
</desktop7:ShadowCopyExcludeFiles>
```

### Key
`{}` specific range of occurrences

## Attributes and Elements

### Attributes

None.

### Child Elements

| Child Element | Description |
|---------------|-------------|
| [desktop7:ShadowCopyExcludeFile](element-desktop7-shadowcopyexcludefile.md) | Specifies a file to be excluded by VSS. |  

### Parent Elements

| Parent Element | Description |
|---------------|-------------|
| [Extension](element-desktop7-extension.md) | Defines an extensibility point for the application. |  


## Remarks

For more information on VSS, see [Volume Shadow Copy Service Overview](/windows/win32/vss/volume-shadow-copy-service-overview).


## Requirements

|               |     Value                                                        |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/7` |