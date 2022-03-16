---
title: uap8:PosPaymentConnector
description: Contains device information for Point-of-Sale/Point-of-Service devices.
ms.date: 03/14/2022

ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap8:PosPaymentConnector

Contains device information for Point-of-Sale/Point-of-Service devices.

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
<dt><a href="element-uap8-extension.md">&lt;uap8:Extension&gt;</a></dt>
<dd><b>&lt;uap8:PosPaymentConnector&gt;</b></dd>
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
<uap8:POSPaymentConnector DisplayName = A string between 1 and 256 characters in length.>

</uap8:POSPaymentConnector>
```

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| DisplayName | The display name of the device. | A string between 1 and 256 characters in length. | Yes |

## Requirements
|   | Value |
|--|--|
| **uap8** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/8` |