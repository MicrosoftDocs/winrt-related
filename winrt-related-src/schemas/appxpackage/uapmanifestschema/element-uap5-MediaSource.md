---

title: uap5:MediaSource
description: Specifies the media source and the app service that it exposes.

ms.date: 10/10/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap5:MediaSource

## Description
Specifies the media source and the app service that it exposes.

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
<dd><b>&lt;uap5:MediaSource&gt;</b></dd>
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
<uap5:MediaSource DisplayName?    = A string between 1 and 256 characters in length. This string is localizable.
                  Description?    = A string between 1 and 2048 characters in length that cannot include characters such as tabs, carriage returns, and line feeds.
                  AppServiceName  = A string between 2 and 39 characters in length that consists of alphanumeric, period (except for the first character), and dash characters only. >   
  <!-- Child elements -->
  ( uap5:SupportedFileTypes, 
    uap5:SupportedContentTypes )
</uap5:MediaSource>
```

### Key
`?`   optional (zero or one)

## Attrbutes and Elements

### Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| DisplayName | The media source display name. | A string between 1 and 256 characters in length. This string is localizable. | No |
| Description | A brief description of the media source. | A string between 1 and 2048 characters in length that cannot include characters such as tabs, carriage returns, and line feeds. | No |
| AppServiceName | The name of the app service exposed by the media source. Note that an app service is required for a media source. |  A string between 2 and 39 characters in length that consists of alphanumeric, period (except for the first character), and dash characters only. | Yes |

### Child Elements

| Child Element | Description |
|---------------|-------------|
| [SupportedFileTypes](element-uap5-SupportedFileTypes.md) | Contains the file types supported by the media source. |
| [SupportedContentTypes](element-uap5-SupportedContentTypes.md) | Contains the media/content types supported by the media source. |



## Requirements

|   |   |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |
