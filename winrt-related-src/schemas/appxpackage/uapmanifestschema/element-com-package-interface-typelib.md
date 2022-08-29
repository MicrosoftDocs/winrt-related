---
ms.assetid: 2fb1ff8b-0c47-44b8-b1c3-b814d10685d1
title: com:TypeLib (in Package/Extensions, child of Interface)
description: A type library for an interface (in Package/Extensions, child of Interface).
ms.date: 03/29/2017
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, com
---

# com:TypeLib (in Package/Extensions, child of Interface)

A type library for an interface.

## Element Hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:Extension\>](element-com-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:ComInterface\>](element-com-cominterface.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<com:Interface\>](element-com-package-interface.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<com:TypeLib\>**

## Syntax

```xml
<com:TypeLib
    Id = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
    VersionNumber = 'An optional value with one to three alphanumeric characters separated by a period followed by one to three more alphanumeric characters (for example, 1.5a).' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| Id | The type library ID. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |
| VersionNumber | The version of the type library. | An optional value with one to three alphanumeric characters separated by a period followed by one to three more alphanumeric characters (for example, 1.5a). | No |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [com:Interface](element-com-package-interface.md) | Declares a package extension point of type **windows.comInterface**. The comInterface extension may include three types of registrations: *Interface*, *ProxyStub*, or *TypeLib*. |

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/com/windows10` |
