---

title: uap6:BarcodeScannerProvider
description: Used for enabling the support of a barcode scanner.

ms.date: 04/10/2018
ms.topic: reference


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
<uap6:BarcodeScannerProvider DisplayName? = A string between 1 and 256 characters in length.
                             SupportsVideoPreview? = Boolean >
```

### Key
`?`   optional (zero or one)

## Attrbutes and Elements

### Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| DisplayName | The barcode scanner provider display name. | A string between 1 and 256 characters in length. | No |
| SupportsVideoPreview | Specify true or false to indicate whether video preview is supported. | Boolean | No |

### Child Elements
None

## Requirements

|   | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/6` |
