---

ms.assetid: 7c6136d7-780e-40a8-b374-f81998dac3f4
title: uap4:CustomCapability
description: Declares a custom capability required by a package.

ms.date: 04/05/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap4:CustomCapability
Declares a custom capability required by a package.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-capabilities.md">&lt;Capabilities&gt;</a></dt>
<dd><b>&lt;uap4:CustomCapability&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<uap4:CustomCapability Name = An alphanumeric string in the form: company.capabilitynamefromstore_publisherId. >
```

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Name | The name of the capability. | An alphanumeric string in the form: company.capabilitynamefromstore_publisherId.  | Yes |


## Requirements

|   |   |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/uap/windows10/4` |
