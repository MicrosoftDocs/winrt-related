---
author: laurenhughes
title: uap6:BarcodeScannerProvider
description: Specifies the media source and the app service that it exposes.
ms.author: lahugh
ms.date: 03/07/2018
ms.topic: reference
ms.prod: windows
ms.technology: winrt-reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap6:BarcodeScannerProvider

## Description
Used for enabling the support of a barcode scanner.

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
<dt><a href="element-uap6-extension.md">&lt;uap6:Extension&gt;</a></dt>
<dd><b>&lt;uap6:BarcodeScannerProvider&gt;</b></dd>
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
<uap6:BarcodeScannerProvider DisplayName = A string between 1 and 256 characters in length.
                             SupportsVideoPreview? = Boolean >
```

### Key
`?`   optional (zero or one)

## Attrbutes and Elements

### Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| DisplayName | The barcode scanner provider display name. | A string between 1 and 256 characters in length. | No |
| SupportsVideoPreview | A brief description of the media source. | Boolean | No |

### Child Elements

| Child Element | Description |
|---------------|-------------|
| [SupportedFileTypes](element-uap5-SupportedFileTypes.md) | Contains the file types supported by the media source. |
| [SupportedContentTypes](element-uap5-SupportedContentTypes.md) | Contains the media/content types supported by the media source. |



## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/uap/windows10/6</p></td>
</tr>
</tbody>
</table>