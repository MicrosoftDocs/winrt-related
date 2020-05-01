---

title: uap5:SupportedFileTypes
description: Contains the file types supported by the media source.

ms.date: 10/10/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap5:SupportedFileTypes

## Description
Contains the file types supported by the media source.

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
<dd>
<dl>
<dt><a href="element-uap5-mediasource.md">&lt;uap5:MediaSource&gt;</a></dt>
<dd><b>&lt;uap5:SupportedFileTypes&gt;</b></dd>
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
```syntax
<uap5:SupportedFileTypes>   
  <!-- Child elements -->
  uap5:FileType{0,1000}
</uap5:SupportedFileTypes>
```

### Key
`{}` specific range of occurrences

## Attributes and Elements

### Attributes
None

### Child Elements

| Child Element | Description |
|---------------|-------------|
| [FileType](element-uap5-filetype.md) | Specifies the file type suppoerted by the media source. |


## Requirements

|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |

