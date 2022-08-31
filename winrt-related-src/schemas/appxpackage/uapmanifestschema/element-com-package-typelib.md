---
ms.assetid: a3735612-102e-47e2-ba08-a53259edc60a
title: com:TypeLib (in Package/Extensions, child of ComInterface)
description: Registers a type library (in Package/Extensions).
ms.date: 03/29/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, com
---

# com:TypeLib (in Package/Extensions, child of ComInterface)

Registers a type library.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:Extension\>](element-com-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:ComInterface\>](element-com-package-cominterface.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:Interface\>](element-com-package-interface.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com:TypeLib\>**

## Syntax

```xml
<TypeLib
    Id = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.' >

  <!-- Child elements -->
  Version{1,1000}

</TypeLib>
```

## Key

`{}`   specific range of occurrences

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Id** | The ID of the type library. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |

### Child elements

| Child element | Description |
|-|-|
| [Version](element-com-package-version.md) | Version number and additional information about the type library. |

### Parent elements

| Parent element | Description |
|-|-|
| [com:ComInterface](element-com-package-cominterface.md) | Declares a package extension point of type **windows.comInterface**. The comInterface extension may include three types of registrations: *Interface*, *ProxyStub*, or *TypeLib*. |

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/com/windows10` |
