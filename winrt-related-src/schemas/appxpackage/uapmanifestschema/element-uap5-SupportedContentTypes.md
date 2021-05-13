---

title: uap5:SupportedContentTypes
description: Contains the media/content types supported by the media source.

ms.date: 10/10/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap5:SupportedContentTypes

## Description
Contains the media/content types supported by the media source.

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
<dd><b>&lt;uap5:SupportedContentTypes&gt;</b></dd>
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
<uap5:SupportedContentTypes>   
  <!-- Child elements -->
  uap5:ContentType{0,1000}
</uap5:SupportedContentTypes>
```

### Key
`{}` specific range of occurrences

## Attributes and Elements

### Attributes
None


### Child Elements

| Child Element | Description |
|---------------|-------------|
| [ContentType](element-uap5-contenttype.md) | Specifies the media/content type supported by the media source. |


## Requirements

|               | Value                                                       |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |